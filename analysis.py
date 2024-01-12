import csv

with open("data.csv", "r") as f: 
    reader = csv.reader(f)
    for row in reader:
        EmployeeID = 0
        FirstName = 1
        LastName = 2
        Age = 3
        Department = 4
        Salary = 5
        
        print(row[EmployeeID], row[FirstName], row[LastName], row[Age], row[Department], row[Salary])
