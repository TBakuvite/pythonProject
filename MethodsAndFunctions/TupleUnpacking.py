stock_prices = [('APPL', 200),('GOOG',400),('MSFT',100)]

for item in stock_prices:
    print(item)



for ticker, price in stock_prices:
    print(price)


work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if(hours>current_max):
            current_max=hours
            employee_of_month=employee

    return (employee_of_month,current_max)


print(employee_check(work_hours))

result = employee_check(work_hours)

name, hours = employee_check(work_hours)

print(name)

