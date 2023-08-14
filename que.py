employees = [
    {'name': 'john', 'salary': 3000, 'designation': 'developer'},
    {'name': 'emma', 'salary': 4000, 'designation': 'manager'},
    {'name': 'kelly', 'salary': 3500, 'designation': 'tester'}
]

max_salary = float('-inf')  
max_employee = None  

for employee in employees:
    if employee['salary'] > max_salary:
        max_salary = employee['salary']
        max_employee = employee

print(max_employee) 
