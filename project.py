import csv
import datetime as dt
import calendar


header = ["Fingerprints", "Year", "Month", *range(1,32)]
Year = int(input("Enter Year: "))
Month = int(input("Enter Month: "))

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
            

            cells = [finger,Month , Year, *([dayCell1,dayCell2]*15), dayCell1]
            for day in range(1,31):
                if dt.datetime(Year,Month,day).weekday() == 4:
                    cells[day+2] = 'x'

            add.writerow(cells)
    
if __name__ == "__main__":
    main()

