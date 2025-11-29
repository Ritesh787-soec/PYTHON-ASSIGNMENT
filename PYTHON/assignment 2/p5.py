class Student:
    def __init__(self, name, marks, medical_leaves, discipline_flag):
        self.name = name
        self.__marks = marks
        self.__medical_leaves = medical_leaves
        self.__discipline_flag = discipline_flag

    def get_academic_record(self):
        return {
            "Marks": self.__marks,
            "Medical Leaves": self.__medical_leaves,
            "Discipline": self.__discipline_flag
        }

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks!")

s = Student("Aman", 85, 2, "Good")
print(s.get_academic_record())
