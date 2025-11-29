# COVID Vaccination Record System

def add_record():
    try:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        vaccine = input("Enter Vaccine Name: ")
        dose = input("Enter Dose Number (1 or 2): ")

        with open("vaccination_records.txt", "a") as file:
            file.write(f"{name:<15}{age:<10}{vaccine:<15}{dose:<10}\n")

        print("Record added successfully!\n")

    except Exception as e:
        print("Error occurred:", e)


def display_records():
    try:
        print("\n--- COVID Vaccination Records ---")
        print(f"{'Name':<15}{'Age':<10}{'Vaccine':<15}{'Dose':<10}")
        print("-" * 50)

        with open("vaccination_records.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No records found.\n")
            else:
                for line in data:
                    print(line, end="")

        print("\n")

    except FileNotFoundError:
        print("No record file exists. Add a record first.\n")
    except Exception as e:
        print("Error occurred:", e)


# Menu Driven Program
while True:
    print("1. Add New Record")
    print("2. Display All Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_record()
    elif choice == '2':
        display_records()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid input! Try again.\n")
