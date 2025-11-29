class Staff:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Name: {self.name}, ID: {self.id}")


class Doctor(Staff):
    def duty(self):
        print("Doctor: Treats patients.")

class Nurse(Staff):
    def duty(self):
        print("Nurse: Assists doctor & manages ward.")

class Surgeon(Staff):
    def duty(self):
        print("Surgeon: Performs surgeries.")

class LabTechnician(Staff):
    def duty(self):
        print("Lab Tech: Conducts lab tests.")


employees = [Doctor("Dr. Amit", 101),
             Nurse("Neha", 102),
             Surgeon("Dr. Raj", 103),
             LabTechnician("Arun", 104)]

for e in employees:
    e.show()
    e.duty()
    print()
