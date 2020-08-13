# report.py
#
# Exercise 2.4

from pprint import pprint
import csv


def read_portfolio_to_tuple(filename):
    '''Reads a portfolio file'''

    portfolio = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

    return portfolio


def read_portfolio_to_dict(filename):
    portfolio = []

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)

    return portfolio


my_stocks = read_portfolio_to_dict('Data/portfoliodate.csv')

total_cost = 0.0
for stock in my_stocks:
    total_cost += stock['shares'] * stock['price']


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


stock_prices = read_prices('Data/prices.csv')

total_value = 0
for stock in my_stocks:
    total_value += stock['shares'] * stock_prices[stock['name']]


# print(f'Total Cost: {total_cost: .2f}')
# print(f'Current Value: {total_value: .2f}')
# print(f'Gain: {(total_value - total_cost): .2f}')


def make_report(portfolio, prices):
    entries = []
    for a_stock in portfolio:
        current_price = prices[a_stock['name']]
        cost = a_stock['price']
        change = (current_price - cost).__round__(2)
        row = (a_stock['name'], a_stock['shares'], current_price, change)
        entries.append(row)

    return entries


report = make_report(my_stocks, stock_prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)

print(('-'*10 + ' ')*4)

for entry in report:
    print(f'{entry[0]: >10s} {entry[1]: >10d} {entry[2]: >10.2f} {entry[3]:>10.2f}')



















