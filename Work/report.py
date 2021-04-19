# report.py
#
# Exercise 2.4

import csv


def read_portfolio_to_tuple(filename):
    """Reads a portfolio file"""

    portfolio = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

    return portfolio


def read_portfolio_to_dict(filename):
    """Reads a portfolio file to a list of dictionaries"""

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


def read_prices(filename):
    """Reads file containing current stock share prices"""

    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


def compute_stock_summary(portfolio, stock_prices):
    """Calculates portfolio costs and current value"""

    total_cost = 0.0
    for stock in portfolio:
        total_cost += stock['shares'] * stock['price']

    total_value = 0
    for stock in portfolio:
        total_value += stock['shares'] * stock_prices[stock['name']]

    return total_cost, total_value


def make_report(portfolio, prices):
    """Creates a portfolio report"""

    entries = []
    for a_stock in portfolio:
        current_price = prices[a_stock['name']]
        cost = a_stock['price']
        change = (current_price - cost).__round__(2)
        row = (a_stock['name'], a_stock['shares'], current_price, change)
        entries.append(row)

    return entries


def print_report(report):
    """Prints current portfolio report"""

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * 4)
    for entry in report:
        print(f'{entry[0]: >10s} {entry[1]: >10d} {entry[2]: >10.2f} {entry[3]:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    my_stocks = read_portfolio_to_dict(portfolio_filename)
    stock_prices = read_prices(prices_filename)
    report = make_report(my_stocks, stock_prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')


