import csv

file = open('employees.csv')
salary = []
name = []
lname = []
manager_salaries = []
sum = 0
qty = 0

try:
    csv_read = csv.reader(file)

    for row in csv_read:
        if csv_read.line_num > 1:
            # Skip the first row as it contains string for numerical values salary
            salary.append(float(row[2]))
            # Add salary column for all the rows into a list
            name.append(row[0])
            # Add first name column for all the rows into a list
            lname.append(row[1])
            # Add last name column for all the rows into a list
            if row[3] == "Manager":
                manager_salaries.append(float(row[2]))
                # Add manager salary to array
    for sal in manager_salaries:
        sum += sal
        qty += 1
        # Add manager salary to total sum and increment control variable
finally:
    file.close()

minimum = min(salary)
# Return minimum value of the salary list
index = salary.index(minimum)
# Index returns the position of the lowest salary in the list
first_name = name[index]
# name[index] return the 13th value in the name list
last_name = lname[index]
# lname[index] return the 13th value in the name list
print(first_name, last_name, 'has lowest salary')

