# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
number_of_months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    number_of_months += 1
    principal = principal * (1 + rate / 12) - payment
    if principal < 0:
        total_paid += payment - abs(principal)
        principal = 0
    else:
        total_paid += payment

    if (extra_payment_start_month <= number_of_months <= extra_payment_end_month) and principal > extra_payment:
        principal -= extra_payment
        total_paid += extra_payment

    print(f'{number_of_months:5d} Paid: {total_paid: 0.2f} \t Remaining: {principal:0.2f}')

print(f'Total paid:  {total_paid:.2f}')
print(f'Number of Months: {number_of_months}')
