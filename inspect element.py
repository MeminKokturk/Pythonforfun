import datetime
import inspect


date = datetime.datetime.now()

for i in inspect.getmembers(date):
    print(i)
