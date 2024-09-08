import json
import os
from students import Students
from teachers import Teachers

class ProfileManager:
    def __init__(self, filename="practice/data.json"):
        self.filename = filename
        self.data = self.load_data()
        self.current_university = None
        self.current_profile = None

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {"Universities": []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
        print("Data saved.")
    
    def add_university(self, university_name):
        university = {
            "name": university_name, 
            "profile": []
        }
        
        self.data["Universities"].append(university)
        print(f"University '{university_name}' added successfully.")
        self.save_data()

    def select_university(self, university_name):
        university = next((u for u in self.data["Universities"] if u["name"] == university_name), None)
        if university:
            self.current_university = university
            print(f"University '{university_name}' selected.")
        else:
            print(f"University '{university_name}' not found.")


    def add_profile(self, profile_name, profile_id):
        if not self.current_university:
            print("No university selected. Please select a university first.")
            return
        
        profile = {
            "name": profile_name,
            "id": profile_id,
            "student": [],   
            "teacher": []    
        }

        self.current_university["profile"].append(profile)
        print(f"Profile '{profile_name}' added successfully.")
        self.save_data()
    
    def select_profile(self, profile_name_or_id):
        
        if not self.current_university:
            print("No university selected. Please select a university first.")
            return

        profile = next((p for p in self.current_university["profile"]
                    if p["name"] == profile_name_or_id or p["id"] == profile_name_or_id), None)
        if profile:
            self.current_profile = profile
            print(f"Profile '{profile_name_or_id}' selected.")
        else:
            print(f"Profile '{profile_name_or_id}' not found.")

    def add_student(self, student, student_id):
        if any(s["id"] == student_id for s in self.current_profile["student"]):
            print(f"This ID: {student_id} was assigned to a student. Please choose another ID.")
        else:    
            self.current_profile["student"].append(student.to_dict())
            print(f"Student {student.name} added successfully.")
            self.save_data()

    def add_teacher(self, teacher, teacher_id):
         if any(t["id"] == teacher_id for t in self.current_profile["teacher"]):
            print(f"This ID: {teacher_id} was assigned to a teacher. Please choose another ID.")
         else:    
            self.current_profile["teacher"].append(teacher.to_dict())
            print(f"Student {teacher.name} added successfully.")
            self.save_data()

    def update_student(self, student_id, new_name, new_email):
        for student in self.data["Students"]:
            if student["id"] == student_id:
                student["name"] = new_name
                student["email"] = new_email
                print(f"Student {student_id} updated successfully.")
                self.save_data()
                return
        print(f"Student with ID {student_id} not found.")

    def update_teacher(self, teacher_id, new_name, new_email):
        for teacher in self.data["Teachers"]:
            if teacher["id"] == teacher_id:
                teacher["name"] = new_name
                teacher["email"] = new_email
                print(f"Teacher {teacher_id} updated successfully.")
                self.save_data()
                return
        print(f"Teacher with ID {teacher_id} not found.")

    def delete_student(self, student_id):
        """Delete a student by ID and update profiles."""
        self.data["Students"] = [s for s in self.data["Students"] if s["id"] != student_id]
        self.data["Profiles"] = [p for p in self.data["Profiles"] if p["student"]["id"] != student_id]
        print(f"Student {student_id} deleted successfully, and profiles updated.")
        self.save_data()

    def delete_teacher(self, teacher_id):
        self.data["Teachers"] = [t for t in self.data["Teachers"] if t["id"] != teacher_id]
        self.data["Profiles"] = [p for p in self.data["Profiles"] if p["teacher"]["id"] != teacher_id]
        print(f"Teacher {teacher_id} deleted successfully, and profiles updated.")
        self.save_data()

    def display_data(self):
        print("\n === Universities ===:")
        for university in self.data["Universities"]:
            print(f"Universitiy: {university['name']}")

        print("\nProfiles:")
        for profile in university["profile"]:
            print(f"Profiles: {profile['name']} (ID: {profile['id']})")
            print(f"    Students: {', '.join([s['name'] for s in profile['student']])}")
            print(f"    Teachers: {', '.join([t['name'] for t in profile['teacher']])}")
