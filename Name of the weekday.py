import datetime
import calendar

tdy = datetime.date.today()
dnm = calendar.day_name[tdy.weekday()]
print(tdy)
print(dnm)