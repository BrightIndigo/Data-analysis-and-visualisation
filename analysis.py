import csv

EmployeeID = []
FirstName = []
LastName = []
Age = []
Department = []
Salary = []

with open("data.csv", newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    for row in reader:
        EmployeeID.append(row[0])
        FirstName.append(row[1])
        LastName.append(row[2])
        Age.append(int(row[3]))  # Convert age to integer
        Department.append(row[4])
        Salary.append(int(row[5]))  # Convert salary to integer

# Example: Find the average salary
average_salary = sum(Salary) / len(Salary)

print(f"Average Salary: {average_salary}")
