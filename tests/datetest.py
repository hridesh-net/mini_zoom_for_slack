import datetime
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
scheduled_time = datetime.time(hour=9, minute=35)
schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time)

str_timestamp = schedule_timestamp.strftime('%m%d%Y, %H:%M:%S')
print(str_timestamp)
print(scheduled_time)

print(schedule_timestamp)

print(tomorrow)