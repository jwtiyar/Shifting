import datetime
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
nameDate= datetime.date(2024,2,28).weekday()
print(nameDate)
print(weekDays[nameDate])

# import pandas as pd
# from project import main
# hey = main()

# pd.read_csv("shoft.csv")
# print(pd.array(hey))