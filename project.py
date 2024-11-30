import csv
import datetime as dt
import calendar

days = [i for i in range(1,32,1)]
days = (','.join(map(str,days))).strip()
header = ["Fingerprints", "Year", "Month", *range(1,32)]
Year = input("Enter Year: ")
Month = input("Enter Month: ")
def main():
    with open('shoft.csv', 'w', newline='') as file:
        add = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='/')
        add.writerow(header)
        for i in range(4):
            finger = input("input the fingerprints: ")
            if i % 2:
                dayCell1, dayCell2 = 6 , "x"
            else:
                dayCell1, dayCell2 = "x" , 6
            for day in range(1,31):
                if dt.datetime(Year,Month,day).weekday() == friday
            cells = [finger,Month , Year, *([dayCell1,dayCell2]*15), dayCell1]
            add.writerow(cells)
    
if __name__ == "__main__":
    main()

