import csv
import datetime as dt
import datetime

header = ["code", "month", "year", *range(1,32)]

def fri_Remove(Year,Month,day):

    return dt.datetime(Year,Month,day).weekday() == 4
             # Changing All fridays to 'X' 

# Below Rule works For third and Fourth Fingerprints which stick them with week days not months number of days either even or odd days.
# For example finger print 3 always works in (Sat, Mon, Wed) and 4 will work always in (Sun, Tue, Thu) in The month.
def day_inWeek(Year, Month, day, f,cells):
    # cells = [None] * 34
    nameDate = datetime.date(Year, Month, day).weekday()
    # cells = [0] * 34
    if f == 2:
        if nameDate == 0:  # Monday
            cells[day + 2] = 6
        elif nameDate == 2:  # Wednesday
            cells[day + 2] = 6
        elif nameDate == 5:  # Saturday
            cells[day + 2] = 6
        else:
            cells[day + 2] = 'x' # Mark other days as 'x'
    elif f == 3:
        if nameDate == 0:  # Monday
            cells[day + 2] = 'x'
        elif nameDate == 2:  # Wednesday
            cells[day + 2] = 'x'
        elif nameDate == 5:  # Saturday
            cells[day + 2] = 'x'
        else:
            cells[day + 2] = 6  # Mark other days as 6 (e.g., Sunday, Tuesday, Thursday)
    
    return cells
 
def main():
    Year = int(input("Enter Year: "))
    Month = int(input("Enter Month: "))

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
            cells = [finger, Month, Year, *([dayCell1, dayCell2] * 15), dayCell1]
            
            for day in range(1,32):  
                if fri_Remove(Year, Month , day):
                    cells[day+2] = 'PUM' 
                    print(f)  
                if f >= 2:
                    day_inWeek(Year, Month, day,f,cells)

            add.writerow(cells)

    return cells, finger


if __name__ == "__main__":
    main()

