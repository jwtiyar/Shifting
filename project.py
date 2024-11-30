import csv
import datetime
import calendar

days = [i for i in range(1,32,1)]
days = (','.join(map(str,days))).strip()

for i in range(4):
    finger1 = input("input the fingerprints: ")
    finger = ''.join(finger1)
year = input("Enter Year: ")
month = input("Enter Month")
field = ['fingerprints', 'month', 'year',days]

def main():
    with open('shoft.csv', 'w', newline='') as file:
        add = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='/')
        add.writerow(field)
        add.writerows(finger)
    
def addRow():
    pass
    
def addColumn():
    pass

if __name__ == "__main__":
    main()

