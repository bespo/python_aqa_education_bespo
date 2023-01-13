# import datetime as dt
#
# data1 = dt.date(2021, 10, 24)
# print(data1)

# import datetime as dt
#
# data1 = dt.date.today()
# print(data1)

# import datetime as dt
#
# time1 = dt.time(10, 45, 30, 45667)
# print(time1)
#
# print("Hour:", time1.hour)
# print("Minute:", time1.minute)
# print("Second:", time1.second)

# import datetime as dt
#
# datetime_obj = dt.datetime(2021, 11, 28, 23, 55,59)
#
# print(datetime_obj)
# print(datetime_obj.date())
# print(datetime_obj.time())

import datetime as dt

current_datetime = dt.datetime.now()

print(current_datetime)

string_date = current_datetime.strftime("%A, %B, %d, %Y")
#
# print(string_date)

# import sys
#
# print(sys.platform)

# import sys
#
# sys.stdout.write("this is a regular message \n")
# sys.stderr.write("this is an error message \n")

# import sys
#
# a = 15
# b = 12.78
# c = "hello, world"
# d = ['list', 123, 123.123]
#
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# print(sys.getsizeof(d))