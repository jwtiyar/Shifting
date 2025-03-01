#!/usr/bin/env python3
import csv
import datetime as dt
import datetime
import tkinter as tk
from tkinter import ttk, messagebox

class ShiftGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Shift Generator")

        # Employee data
        self.employees = {
            "Shakar Rauf": "C875",
            "Omed Salih": "C927",
            "Osman Arif": "C130",
            "Siamand Dilshad": "C796",
            "Wrya Abdullah": "C930"
        }

        # Header for CSV
        self.header = ["code", "month", "year", *range(1, 32)]  # Unpacking 31 days

        # Apply styles
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TEntry", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        self.style.configure("TCombobox", font=("Helvetica", 12))

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Year input
        ttk.Label(self.root, text="Year:").grid(row=0, column=0, padx=5, pady=5, sticky="W")
        self.year_var = tk.StringVar()
        self.year_entry = ttk.Entry(self.root, textvariable=self.year_var)
        self.year_entry.grid(row=0, column=1, padx=5, pady=5, sticky="EW")

        # Month input
        ttk.Label(self.root, text="Month:").grid(row=1, column=0, padx=5, pady=5, sticky="W")
        self.month_var = tk.StringVar()
        self.month_entry = ttk.Entry(self.root, textvariable=self.month_var)
        self.month_entry.grid(row=1, column=1, padx=5, pady=5, sticky="EW")

        # Fingerprint selection
        self.fingerprint_vars = []
        for i in range(4):
            ttk.Label(self.root, text=f"Fingerprint {i+1}:").grid(row=i+2, column=0, padx=5, pady=5, sticky="W")
            fingerprint_var = tk.StringVar()
            fingerprint_combobox = ttk.Combobox(self.root, textvariable=fingerprint_var, values=list(self.employees.keys()))
            fingerprint_combobox.grid(row=i+2, column=1, padx=5, pady=5, sticky="EW")
            self.fingerprint_vars.append(fingerprint_var)

        # Generate button
        self.generate_btn = ttk.Button(self.root, text="Generate Shifts", command=self.generate_shifts)
        self.generate_btn.grid(row=6, column=0, columnspan=2, pady=10)

        # Copyright button
        self.copyright_btn = ttk.Button(self.root, text="© 2025 Jwtyar Nariman", command=self.open_github)
        self.copyright_btn.grid(row=7, column=0, columnspan=2, pady=10)

        # Configure grid weights for responsive layout
        self.root.grid_columnconfigure(1, weight=1)

    def generate_shifts(self):
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            # Make the name of the generated csv file same as the month name
            month_name = dt.datetime(year, month, 1).strftime("%B")
            with open(f"{month_name}.csv", "w", newline="") as file:
                add = csv.writer(file)
                add.writerow(self.header)
                for f in range(4):
                    fingerprint_name = self.fingerprint_vars[f].get()
                    if fingerprint_name not in self.employees:
                        raise ValueError(f"Invalid fingerprint: {fingerprint_name}")
                    finger = self.employees[fingerprint_name]
                    
                    # Change day_Cell_1 and day_Cell_2 to day_cell_1 and day_cell_2
                    if f % 2:
                        day_cell_1, day_cell_2 = 6, "x"
                    else:
                        day_cell_1, day_cell_2 = "x", 6
                    
                    cells = [finger, month, year, *([day_cell_1, day_cell_2] * 15), day_cell_1]  # numdays variable can be used here and divided by two.
                                        
                    for day in range(1, 32):
                        try:
                            if fri_Remove(year, month, day):
                                cells[day + 2] = "x"
                            if f >= 2:
                                day_inWeek(year, month, day, f, cells)
                        except ValueError:
                            continue
                    
                    add.writerow(cells)
            
            messagebox.showinfo("Success", "CSV shift file successfully created!")
            self.root.destroy()
            
            
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def get_fingerprint(self, f):
        return list(self.employees.values())[f]

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/jwtiyar")

def fri_Remove(Year, Month, day):
    try:
        return (
            dt.datetime(Year, Month, day).weekday() == 4
        )  # Friday is number 4 of the week.
    except ValueError:
        return False

def day_inWeek(Year, Month, day, f, cells):
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
    root = tk.Tk()
    app = ShiftGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
