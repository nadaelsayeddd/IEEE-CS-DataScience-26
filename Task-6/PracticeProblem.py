import json
import os
FILE = "C:/Users/Nada/Documents/IEEE-CS-DataScience-26/Task-6/employees.json"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_annual_salary(self):
        annual_salary = self.salary * 12
        return annual_salary
    
    def display_info(self):
        return f"Employee name: {self.name}\nMonthly Salary: {self.salary}$\nAnnual Salary: {self.get_annual_salary()}$"
    def to_dict(self):
        return {"name": self.name, "salary": self.salary}

def load_employees():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [Employee(**e) for e in json.load(f)]
    
def save_employees(employees):
    with open(FILE, "w") as f:
        json.dump([e.to_dict() for e in employees], f, indent=2)
        print(f"Saved to {FILE}")


def main():
    employees = load_employees()
    while True:
        print("Enter your choice")
        print("1. Add employee")
        print("2. Show all employees")
        print("3. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            name = input("Employee Name: ").strip()
            salary = float(input("Monthly Salary: "))
            emp = Employee(name, salary)
            employees.append(emp)
            save_employees(employees)
            print(f"'{name}'added")

        elif choice == "2":
            if not employees:
                print("No employees")
            else:
                for emp in employees:
                    print(emp.display_info())

        elif choice == "3":
            print("bye")
            break

        else:
            print("Invalid choice")
main()