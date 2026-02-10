from datetime import date
name = input("Name: ")
birth_year = int(input("Birth Year: "))
age = int(date.today().year) - birth_year
print(f"Hello {name}, you are {age} years old")