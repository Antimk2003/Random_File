print("________________________||(1): Program||_______________________")

import datetime

from datetime import datetime
# get current date

now = datetime.now()

# cnvert current date intotimestamp
timestamp = datetime.timestamp(now)
print("Date and Time :",now)

print("Timestamp :",timestamp)


print("________________________||(2): Program||_______________________")

my_string = '2023-2-16'

# Create date object in given time formate yyyy-mm-dd

my_date = datetime.strptime(my_string, "%Y-%m-%d")

print(my_date)
print("Type :",type(my_date))



#



print("________________________||(4): Program||_______________________")

#import datetime

from datetime import timedelta
# Create timedelta object with difference
d = timedelta(weeks=2)
print(d)
print(type(d))
print(d.days)
