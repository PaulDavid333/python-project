from Profile import ProfileManager
from students import Students
from teachers import Teachers

def main_menu():
    profile_manager = ProfileManager()

    while True:
        print("\n=== Main Menu ===")
        print("1. Add University")
        print("2. Select University")
        print("3. Display All Data")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            university_name = input("Enter university name: ")
            profile_manager.add_university(university_name)

        elif choice == '2':
            university_name = input("Select University: ")
            profile_manager.select_university(university_name)

            while True:
                print("\n=== Profile Menu ===")
                print("1. Add Profile")
                print("2. Select Profile")
                print("3. Return to Main Menu..")

                profile_choice = input("Enter your choice (1-4): ")

                if profile_choice == '1':
                    profile_name = input("Enter profile name: ")
                    profile_id = int(input("Enter profile ID: "))
                    profile_manager.add_profile(profile_name, profile_id)

                elif profile_choice == '2':
                    profile_name_or_id = input("Enter profile name: ")
                    profile_manager.select_profile(profile_name_or_id) 

                    while True:
                        print("\n=== Teachers/Students Menu ===")
                        print("1. Add Student")
                        print("2. Update Student")
                        print("3. Delete Student")
                        print("4. Add Teacher")
                        print("5. Update Teacher")
                        print("6. Delete Teacher")
                        print("7. Return to Profile Menu..")

                        student_teacher_choice = input("Enter your choice (1-4): ")

                        if student_teacher_choice == '1':
                            name = input("Enter student name: ")
                            email = input("Enter student email: ")
                            student_id = input("Enter student ID: ")
                            student = Students(name, email, student_id)
                            profile_manager.add_student(student, student_id)

                        elif student_teacher_choice == '2':
                            student_id = int(input("Enter student ID to update: "))
                            new_name = input("Enter new student name: ")
                            new_email = input("Enter new student email: ")
                            profile_manager.update_student(student_id, new_name, new_email)

                        elif student_teacher_choice == '3':
                            student_id = int(input("Enter student ID to delete: "))
                            profile_manager.delete_student(student_id)

                        elif student_teacher_choice == '4':
                            name = input("Enter teacher name: ")
                            email = input("Enter teacher email: ")
                            teacher_id = int(input("Enter teacher ID: "))
                            teacher = Teachers(name, email, teacher_id)
                            profile_manager.add_teacher(teacher, teacher_id)

                        elif student_teacher_choice == '5':
                            teacher_id = int(input("Enter teacher ID to update: "))
                            new_name = input("Enter new teacher name: ")
                            new_email = input("Enter new teacher email: ")
                            profile_manager.update_teacher(teacher_id, new_name, new_email)

                        elif student_teacher_choice == '6':
                            teacher_id = int(input("Enter teacher ID to delete: "))

                        elif student_teacher_choice == '7':
                            print("Exiting program.")
                            break

                elif profile_choice == '3':
                    print("Exiting program.")
                    break                                    

        elif choice == '3':
            profile_manager.display_data()
        
        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main_menu()