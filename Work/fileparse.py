# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=','):
    """
    Reads file into a dictionary
    """
    with open(filename, 'rt') as file:
        rows = csv.reader(file, delimiter=delimiter)
        if has_headers:
            # Read the file headers
            headers = next(rows)
        else:
            headers = []
        #

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []

        for row in rows:
            if not row:
                continue

            if indices:
                row = [row[index] for index in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records


# record = parse_csv('Data/portfolio.csv', select=['shares', 'price'], types = [int, float], has_headers  = True)

#record = parse_csv('Data/prices.csv', types=[str, float])
portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ', has_headers=True)

for rec in portfolio:
    print(rec)
