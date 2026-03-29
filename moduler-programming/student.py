class Student:
    def __init__(self, std_id, name, class_name):
        self.std_id = std_id
        self.name = name
        self.class_name = class_name

    def __str__(self):
        return f"ID: {self.std_id}, Name: {self.name}, Class: {self.class_name}"