import datetime

# 1. Symbol
symbol = input("Enter Symbol: ")
if symbol.isalpha() == True and len(symbol) == 7 and symbol.isupper() == True:
  print("Valid Symbol")
else:
  print("Invalid Symbol")


# 2. Chart Type
try:
  chart_type = int(input("Enter Chart Type: "))
  if chart_type == 1 or chart_type == 2:
    print("Valid Chart Type")
  else:
    print("Invaild Chart Type")
except ValueError:
  print("Invaild Chart Type")


# 3. Time Series
try:
  time_series = int(input("Enter Time Series: "))
  if time_series > 0 and time_series < 5:
    print("Valid Time Series")
  else:
    print("Invaild Time Series")
except ValueError:
  print("Invaild Time Series")


# 4. Start Date
date_string = input("Enter start date in the format YYYY-MM-DD: ")
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print("Vaild date format")
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format")


# 5. End Date
date_string = input("Enter end date in the format YYYY-MM-DD: ")
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print("Vaild date format")
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format")