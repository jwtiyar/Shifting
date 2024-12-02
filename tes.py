import csv
import datetime as dt

FRIDAY = 4

# 34 columns total indexed 0-33
# The * expands the range in-place as 1,2,3...31
header = ['fingerprint', 'month', 'year', *range(1,32)]

year = int(input('Enter year: '))
month = int(input('Enter month: '))

with open('shoft.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for f in range(4):
        finger = input('input the fingerprints: ')
        # How 6,x order was determined wasn't specified.
        # I chose alternating the output
        if f % 2:
            d1, d2 = 6, 'x'
        else:
            d1, d2 = 'x', 6
        # Again, * expands [d1,d2]*15 in-place.
        # e.g. 6,x,6,x...6 or x,6,x,6...x
        # creates a length 34 list for row.
        row = [finger, month, year, *([d1, d2] * 15), d1]
        # Make all Fridays an x
        for day in range(1, 31):
            if dt.datetime(year, month, day).weekday() == FRIDAY:
                # Day 1 is column 3, Day 2 is column 4, etc.
                row[day + 2] = 'x'
        writer.writerow(row)