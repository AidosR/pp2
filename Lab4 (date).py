# Python date

# 1. Write a Python program to subtract five days from current date.
import datetime

# Get the current date
current_date = datetime.date.today()

# Subtract 5 days from the current date
new_date = current_date - datetime.timedelta(days=5)

# Print the new date
print(current_date)
print(new_date)

# 2. Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.date.today()
yesterday = today.replace(day = today.day - 1)
tomorrow = today.replace(day = today.day + 1)
print("yesterday: ", yesterday)
print("today: ", today)
print("tomorrow: ", tomorrow)


# 3. Write a Python program to drop microseconds from datetime.
import datetime
print(datetime.datetime.now().replace(microsecond = 0))


# 4. Write a Python program to calculate two date difference in seconds.
import datetime
today = datetime.datetime.today()
date = datetime.datetime(2021, 1, 11)
diff = today - date
print(diff.total_seconds())


