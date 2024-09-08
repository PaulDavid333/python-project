class Students:
    def __init__(self, name, email ,id):
        self.name = name
        self.email = email
        self.id = id

    def to_dict(self):
        return {
            "name": self.name, 
            "email": self.email, 
            "id": self.id
        } 