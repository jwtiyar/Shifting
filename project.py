import csv
import datetime
import calendar

days = [i for i in range(1,32,1)]
days = (','.join(map(str,days))).strip()
header = ["Year", "Year", "Month", *range(1,32)]
Year = input("Enter Year: ")
Month = input("Enter Month")
for i in range(4):
    finger1 = input("input the fingerprints: ")
def main():
    with open('shoft.csv', 'w', newline='') as file:
        add = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='/')
        add.writerow(header)
        
    

if __name__ == "__main__":
    main()

