import csv
import datetime as dt
import datetime
# import calendar

print("""
Shakar Rauf : C875
Omed Salih: C927
Osman Arif: C130
Siamand Dilshad : C796
Wrya Abdullah: C930
""")
print("First and Second Fingerprint is For Oil Lab Employees, Third and Fourth for Sample man's")
header = ["code", "month", "year", *range(1, 32)] # Unpacking 31 days *


def fri_Remove(Year, Month, day):
    try:
        return (
            dt.datetime(Year, Month, day).weekday() == 4
        )  # Friday is number 4 of the week.
    except ValueError:
        return False


# Below Rule works For third and Fourth Fingerprints which stick them with week days not months number of days either even or odd days.
# For example finger print 3 always works in (Sat, Mon, Wed) and 4 will work always in (Sun, Tue, Thu) in The month.
# numbers of week starts from 0 to 6 in otherword Monday is 0 and Tuesday is 1 ..etc.
# As you can see below we didn't used number 4 because it's Friday and we already have function for it.
# Friday remover should be mentioned again to mark fridays and change their value to 'x if its Friday.
def day_inweek(Year, Month, day, f, cells):
    nameDate = datetime.date(Year, Month, day).weekday()
    if f == 2:
        if nameDate in [0, 2, 5]:
            cells[day + 2] = "x"
            if fri_Remove(Year, Month, day):
                cells[day + 2] = "x"
        else:
            cells[day + 2] = 6
            if fri_Remove(Year, Month, day):
                cells[day + 2] = "x"
    elif f == 3:
        if nameDate in [0, 2, 5]:
            cells[day + 2] = 6
            if fri_Remove(Year, Month, day):
                cells[day + 2] = "x"
        else:
            cells[day + 2] = "x"
            if fri_Remove(Year, Month, day):
                cells[day + 2] = "x"

    return cells


def main():
    Year = int(input("Enter Year: "))
    Month = int(input("Enter Month: "))
    # num_days = calendar.monthrange(Year, Month)[1] # determine number of days two make that code works for months that less that 31 days.
    # you can also use above one to bypass these months that less than 31 days, change cells[] and range(1,32). but I was more confident with try-Except.
    with open("shift.csv", "w", newline="") as file:
        add = csv.writer(file)
        add.writerow(header)
        for f in range(4):
            finger = input("input the fingerprints: ").strip()
            # This Rule will work for first and second Fingerprint which decide to make one of them exist in odd days and other one in even dates all over the month.
            if f % 2:
                day_Cell_1, dayCell2 = 6, "x"
            else:
                day_Cell_1, day_Cell_2 = "x", 6
                
            cells = [finger,Month,Year,*([dayCell1, dayCell2] * 15),dayCell1,]  # numdays variable can be used here and divided by two.

            for day in range(1, 32):
                try:
                    if fri_Remove(Year, Month, day):
                        cells[day + 2] = "x"  # Used +2 because 0,1,2 column is reserved for code,month,year.
                    if f >= 2:
                        day_inweek(Year, Month, day, f, cells)  # Cells used as argument to the function because we want it to be available in inWeek func. otherwise gives error.
                except:
                    continue  # continue do the work even the month is less than 31 days.

            add.writerow(cells)
    print("CSV shift File Succefully created")

    return cells, finger


if __name__ == "__main__":
    main()
