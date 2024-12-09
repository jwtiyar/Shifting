import csv
import datetime as dt

header = ["code", "month", "year", *range(1, 32)]  # Add days from 1 to 31 as columns


# Function to check if a given day is a Friday
def fri_Remove(Year, Month, day):
    return dt.datetime(Year, Month, day).weekday() == 4  # Friday is 4


# Function that assigns day values for fingerprints (2 and 3) based on the day of the week
def day_inWeek(Year, Month, day, f):
    cells = [None] * 32  # Initialize cells list with placeholders (32 columns)
    nameDate = dt.date(Year, Month, day).weekday()  # Get the weekday of the given day


    return cells


def main():
    Year = int(input("Enter Year: "))
    Month = int(input("Enter Month: "))
    
    with open('shift1.csv', 'w', newline='') as file:
        add = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='/')
        add.writerow(header)  # Write the header row with days of the month (1-31)

        # Loop through 4 fingerprints
        for f in range(4):
            finger = input("Input the fingerprint: ")

            # Handle odd/even days for fingerprints
            if f % 2:  # If fingerprint index is odd
                dayCell1, dayCell2 = 6, "x"
            else:  # If fingerprint index is even
                dayCell1, dayCell2 = "x", 6

            # Initialize cells for the month, first column is the fingerprint, followed by month, year, and days
            cells = [finger, Month, Year, *([dayCell1, dayCell2] * 15), dayCell1]

            # For each day in the month (1-31), mark Fridays and other conditions
            for day in range(1, 32):
                if fri_Remove(Year, Month, day):  # Check if the day is a Friday
                    cells[day + 2] = 'x'  # Set the appropriate cell to 'x' for Fridays

                # Optionally handle day-in-week logic for fingerprints 2 and 3
                if f == 2 or f == 3:
                    cells = day_inWeek(Year, Month, day, f)

            add.writerow(cells)  # Write the row to the CSV file for each fingerprint

    return cells, finger


if __name__ == "__main__":
    main()
