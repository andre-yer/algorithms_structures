import sys


def sales(transactions):
    sales_dict = {}
    for name, thing, price in transactions:
        if name not in sales_dict:
            sales_dict[name] = {}
        if thing not in sales_dict[name]:
            sales_dict[name][thing] = 0
        sales_dict[name][thing] += int(price)
    for name in sorted(sales_dict.keys()):
        print(name + ':')
        for thing in sorted(sales_dict[name].keys()):
            print(thing, sales_dict[name][thing])


transactions = []
for line in sys.stdin:
    transactions.append((tuple(line.split())))
sales(transactions)
