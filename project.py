import csv
import datetime as dt
import datetime

header = ["Fingerprints", "Month", "Year", *range(1,32)]
Year = int(input("Enter Year: "))
Month = int(input("Enter Month: "))
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

def main():
    with open('shift.csv', 'w', newline='') as file:
        add = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='/')
        add.writerow(header)
        for f in range(4):
            finger = input("input the fingerprints: ")
            # This Rule will work for first and second Fingerprint which decide to make one of them exist in odd days and other one in even dates all over the month.
            if f % 2:
                dayCell1, dayCell2 = 6 , "x"
            else:
                dayCell1, dayCell2 = "x" , 6
                    
            cells = [finger,Month , Year, *([dayCell1,dayCell2]*15), dayCell1]
            for day in range(1,31,1):
                if dt.datetime(Year,Month,day).weekday() == 4: # Changing All fridays to 'X' 
                    cells[day+2] = 'x' # Because Column 3 starts the day.
                nameDate = datetime.date(Year, Month, day).weekday()
                # Below Rule works For third and Fourth Fingerprints which stick them with week days not months number of days either even or odd days.
                # For example finger print 3 always works in (Sat, Mon, Wed) and 4 will work always in (Sun, Tue, Thu) in The month.
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

