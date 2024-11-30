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
            for day in range(1,31,1):
                if dt.datetime(Year,Month,day).weekday() == 4:
                    cells[day+2] = 'x'
                nameDate = datetime.date(Year, Month, day).weekday()
                if f == 2:
                    if nameDate == 0 :
                        cells[day+2] = 6
                    elif nameDate == 2:
                        cells[day+2] = 6
                    elif nameDate == 5:
                        cells[day+2] = 6
                    elif nameDate == 3:
                        cells[day+2] = 'x'
                    elif nameDate == 1:
                        cells[day+2] = 'x'
                    elif nameDate == 6:
                        cells[day+2] = 'x'
                elif f == 3:
                    if nameDate == 0 :
                        cells[day+2] = 'x'
                    elif nameDate == 2:
                        cells[day+2] = 'x'
                    elif nameDate == 5:
                        cells[day+2] = 'x'
                    elif nameDate == 3:
                        cells[day+2] = 6
                    elif nameDate == 1:
                        cells[day+2] = 6
                    elif nameDate == 6:
                        cells[day+2] = 6

                            
            add.writerow(cells)

    
if __name__ == "__main__":
    main()

