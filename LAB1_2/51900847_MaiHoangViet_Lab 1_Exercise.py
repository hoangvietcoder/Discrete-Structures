# Part A: House Hunting
# Retrieve user input.
annual_salary = float(input('Enter your the starting annual salary: '))
portion_saved = float(input('Enter your the portion of salary to be saved (as a decimal): '))
total_cost = float(input('Enter the cost of your dream home: '))

# Initialize some state variables.
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
portion_saved_monthly = portion_saved * monthly_salary

months = 0
while current_savings <= portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += portion_saved_monthly
    months += 1
print('Number of month: ', months)

# Part B: Saving, with a raise
annual_salary = float(input('Enter your the starting annual salary: '))
portion_saved = float(input('Enter your the portion of salary to be saved (as a decimal): '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input("Enter the semiannual raise (as a decimal): "))

# Initialize some state variables.
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
portion_saved_monthly = portion_saved * monthly_salary

months = 0
while current_savings <= portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += portion_saved_monthly
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        portion_saved_monthly = portion_saved * monthly_salary
print('Number of month: ', months)

# Part C: Finding the right amount to save away
starting_salary = input(float('Enter the starting salary: '))
semi_annual_raise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = 0.25 * total_cost
months = 36
current_savings = 0
r = 0.04


