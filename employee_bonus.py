import csv

employees = open('EmployeePay.csv', 'r')
employee_file = csv.reader(employees, delimiter = ',')

next(employee_file)

for employee in employee_file:
    first_name = employee[1]
    last_name = employee[2]
    salary = int(employee[3])
    bonus = float(employee[4])*salary
    total_pay = salary + bonus

    print('First Name: ', first_name, sep = '')
    print('Last Name:  ', last_name, sep = '')
    print('Salary:     $', format(salary, '<,.2f'), sep = '')
    print('Bonus:      $', format(bonus, '<,.2f'), sep = '')
    print('Total Pay:  $', format(total_pay, '<,.2f'), sep = '')

    print()
    input('Press enter to continue >>> ')
    print()

