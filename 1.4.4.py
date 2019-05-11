from datetime import date, time , datetime , timedelta
today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(datetime.today())

# 使用 timedelta 函数来对data对象进行时间加减操作

one_day = timedelta(days=-1)
yesterday = today + one_day
print(yesterday)
eight_hours = timedelta(hours=-8)
print(eight_hours.days, eight_hours.seconds)