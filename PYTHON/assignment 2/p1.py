# Demonstrating Python OOP Flexibility: Inheritance + Encapsulation

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age         # protected (convention-based)

    def show_details(self):
        print(f"Name: {self.name}, Age: {self._age}")


# Inheritance Example
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.__marks = marks   # private variable

    # Encapsulation using getter-setter
    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks!")

    def show_details(self):
        super().show_details()
        print("Marks:", self.__marks)


s = Student("Rohan", 20, 88)
s.show_details()
