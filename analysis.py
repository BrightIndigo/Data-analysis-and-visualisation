import csv
import numpy as np
import matplotlib.pyplot as plt

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

EmployeeID_arr = np.array(EmployeeID)
FirstName_arr = np.array(FirstName)
LastName_arr = np.array(LastName)
Age_arr = np.array(Age)
Department_arr = np.array(Department)
Salary_arr = np.array(Salary)

mean_salary = np.mean(Salary_arr)
median_salary = np.median(Salary_arr)
std_dev_salary = np.std(Salary_arr)

plt.scatter(Age_arr, Salary_arr, label='Age vs. Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs. Salary')
plt.legend()
plt.show()
