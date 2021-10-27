

class Student():

    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Student {self.name} has {self.marks} marks'

    def is_passed(self) -> bool:
        return True if self.marks > 50 else False