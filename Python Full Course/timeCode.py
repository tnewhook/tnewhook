import timeCode             #   https://docs.python.org/3/library/time.html

print(time.ctime(0))    #   convert a time expressed in seconds since epoch to a readable string
#                           epoch = when your computer thinks time began (reference point)

# print(time.time()) # return current seconds since epoch

# print(time.ctime(time.time()))

time_object = time.localtime()
UTC = time.gmtime() #UTC Time
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)                        #   time.strftime(format,time)
print("Local Time: " + local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string,"%d %B, %Y") #Parse string as datetime
print(time_object)

# convert date-format tuple to datetime
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

#mktime = number of seconds since epoch