import csv
import datetime as dt
import datetime
header = ["Fingerprints", "Year", "Month", *range(1,32)]
Year = int(input("Enter Year: "))
Month = int(input("Enter Month: "))
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
def main():
    with open('shoft.csv', 'w', newline='') as file:
        add = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='/')
        add.writerow(header)
        for f in range(4):
            finger = input("input the fingerprints: ")
            if f % 2:
                dayCell1, dayCell2 = 6 , "x"
            else:
                dayCell1, dayCell2 = "x" , 6
                    
            cells = [finger,Month , Year, *([dayCell1,dayCell2]*15), dayCell1]
            for day in range(1,31):
                if dt.datetime(Year,Month,day).weekday() == 4:
                    cells[day+2] = 'x'
                if f >= 2:
                    nameDate= datetime.date(Year, Month, day).weekday()
                    print(nameDate)
                    if nameDate == weekDays[0]:
                        cells[day+2], cells[day+3] = 'x' , 6
                    elif nameDate == weekDays[1]:
                        cells[day+2], cells[day+3] = 6 , 'x'
                
            print(weekDays[0])
            add.writerow(cells)

    
if __name__ == "__main__":
    main()

