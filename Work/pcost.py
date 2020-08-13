# pcost.py
#
# Exercise 1.27
import gzip
import csv
import sys
import pprint


def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowNo, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            print(record)
            try:
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {rowNo}: Bad row: {row}')

    return total_cost



if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print(f'The cost of the entire portfolio is {cost: .2f}')

