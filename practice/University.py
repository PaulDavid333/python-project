class University:

    def __init__(self, name):
        self.name = name
        self.profile = []
    
    def to_dict(self):
        return{
            "name" : self.name,
            "profile": [profile for profile in self.profile]
        }
