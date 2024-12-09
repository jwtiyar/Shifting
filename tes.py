# import csv
# import datetime as dt

# FRIDAY = 4

# # 34 columns total indexed 0-33
# # The * expands the range in-place as 1,2,3...31
# header = ['fingerprint', 'month', 'year', *range(1,32)]

# year = int(input('Enter year: '))
# month = int(input('Enter month: '))

# with open('shoft.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(header)
#     for f in range(4):
#         finger = input('input the fingerprints: ')
#         # How 6,x order was determined wasn't specified.
#         # I chose alternating the output
#         if f % 2:
#             d1, d2 = 6, 'x'
#         else:
#             d1, d2 = 'x', 6
#         # Again, * expands [d1,d2]*15 in-place.
#         # e.g. 6,x,6,x...6 or x,6,x,6...x
#         # creates a length 34 list for row.
#         row = [finger, month, year, *([d1, d2] * 15), d1]
#         # Make all Fridays an x
#         for day in range(1, 31):
#             if dt.datetime(year, month, day).weekday() == FRIDAY:
#                 # Day 1 is column 3, Day 2 is column 4, etc.
#                 row[day + 2] = 'x'
#         writer.writerow(row)


# import csv
# import datetime as dt
# import datetime

# header = ["code", "month", "year", *range(1,32)]

# def fri_Remove(Year,Month,day):

#     return dt.datetime(Year,Month,day).weekday() == 4
#              # Changing All fridays to 'X' 

# # Below Rule works For third and Fourth Fingerprints which stick them with week days not months number of days either even or odd days.
# # For example finger print 3 always works in (Sat, Mon, Wed) and 4 will work always in (Sun, Tue, Thu) in The month.
# def day_inWeek(Year, Month, day, f):
#     nameDate = datetime.date(Year, Month, day).weekday()
#     cells = [] * 34
#     if f == 2:
#         if nameDate == 0:  # Monday
#             cells[day + 2] = 77
#         elif nameDate == 2:  # Wednesday
#             cells[day + 2] = 77
#         elif nameDate == 5:  # Saturday
#             cells[day + 2] = 77
#         else:
#             cells[day + 2] = 00 # Mark other days as 'x'
#     elif f == 3:
#         if nameDate == 0:  # Monday
#             cells[day + 2] = 'x'
#         elif nameDate == 2:  # Wednesday
#             cells[day + 2] = 'x'
#         elif nameDate == 5:  # Saturday
#             cells[day + 2] = 'x'
#         else:
#             cells[day + 2] = 6  # Mark other days as 6 (e.g., Sunday, Tuesday, Thursday)
    
#     return cells
 
# def main():
#     Year = int(input("Enter Year: "))
#     Month = int(input("Enter Month: "))

#     with open('shift.csv', 'w', newline='') as file:
#         add = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='/')
#         add.writerow(header)
#         for f in range(4):
#             finger = input("input the fingerprints: ")
#             # This Rule will work for first and second Fingerprint which decide to make one of them exist in odd days and other one in even dates all over the month.
#             if f % 2:
#                 dayCell1, dayCell2 = 6 , "x"
#             else:
#                 dayCell1, dayCell2 = "x" , 6
#             cells = [finger, Month, Year, *([dayCell1, dayCell2] * 15), dayCell1]
            
#             for day in range(1,32):  
#                 if fri_Remove(Year, Month , day):
#                     cells[day+2] = 'PUM' 
#                     print(f)  
#                 if f >= 2:
#                     day_inWeek(Year, Month, day,f)

                        
#             add.writerow(cells)

#     return cells, finger


# if __name__ == "__main__":
#     main()

import csv
import datetime as dt

# Header for CSV
header = ["code", "month", "year"] + [str(day) for day in range(1, 32)]

# Function to determine if a date is a Friday
def fri_Remove(year, month, day):
    return dt.datetime(year, month, day).weekday() == 4


# Handle fingerprint logic based on weekdays
def day_inWeek(year, month, day, f):
    """
    Determines a weekday fingerprint (cells) based on the specific weekday logic.
    """
    name_date = dt.date(year, month, day).weekday()
    cells = [0] * 31  # Create a list of 31 zeros for 31 possible days
    if f == 2:
        if name_date in [0, 2, 5]:  # Monday, Wednesday, Saturday
            cells[day - 1] = 6
        else:
            cells[day - 1] = 'x'
    elif f == 3:
        if name_date in [0, 2, 5]:  # Monday, Wednesday, Saturday
            cells[day - 1] = 'x'
        else:
            cells[day - 1] = 6
    return cells


def main():
    # User input
    year = int(input("Enter Year: "))
    month = int(input("Enter Month: "))

    # Prepare CSV file
    with open("shift.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)  # Write the header row

        # Loop through fingerprint logic
        for f in range(4):
            # Default behavior for alternate days
            if f % 2:
                day_cell_odd, day_cell_even = 6, "x"
            else:
                day_cell_odd, day_cell_even = "x", 6

            # Generate fingerprints for all 31 days
            cells = [f, month, year] + [day_cell_odd if i % 2 == 0 else day_cell_even for i in range(31)]

            # Adjust for Friday and weekday logic
            for day in range(1, 32):
                if fri_Remove(year, month, day):
                    cells[day + 2] = "PUM"  # Replace Friday logic
                    print(f"Friday found on day {day}")
                
                if f >= 2:
                    weekday_cells = day_inWeek(year, month, day, f)
                    cells[day - 1] = weekday_cells[day - 1]  # Overwrite with weekday logic

            # Write adjusted logic to CSV
            writer.writerow(cells)

    print("CSV creation completed.")
    return


if __name__ == "__main__":
    main()
