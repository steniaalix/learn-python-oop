'''
import datetime as dt

print("Current date and time =",dt.datetime.now())


from datetime import date
print(f"Today's date = {date.today()}")



from datetime import datetime

res=datetime.now()
print(res)
print(res.time())
print(res.date())
print(res.day)
print(res.year)
print(res.month)

from datetime import date
print(f"Today's date ={date.today().day}")


import datetime as dt
d=dt.datetime.now()
print(d.strftime("%a"))



from datetime import datetime
d=datetime.now()
print(d.strftime("%d/%m/%Y"))

print(d.strftime("%Y/%m/%d"))



from datetime import datetime

date_str="27-05-2026"

d=datetime.strptime(date_str,"%d-%m-%Y")
print(d)



from datetime import datetime,timedelta

now=datetime.now()

future= now +timedelta(days=7)
print(future)



from datetime import datetime,timedelta
now=datetime.now()

future= now + timedelta(days=1,hours=2,minutes=30)

print(future)


from datetime import datetime,timedelta

now= datetime.now()

past=now - timedelta(days=1)
print(past)


from datetime import datetime

d1=datetime(2026,5,1)
d2=datetime(2025,4,30)
difference= d1-d2
print(difference.days)



from datetime import datetime

now=datetime.now()
print(now.timestamp())


from datetime import datetime

print(datetime.now()-datetime.utcnow())


from datetime import datetime
class DigitalClock:
    def __init__(self):
        self.now=datetime.now()
        self.curr_date=self.now.strftime("%d-%m-%Y")
        self.curr_time=self.now.strftime("%H:%M:%S")
    def show_time(self):
        print(f"Current Date: {self.curr_date}")
        print(f"Current time : {self.curr_time}")

clock=DigitalClock()
clock.show_time()


from datetime import datetime,timedelta

class Person:
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=datetime.strptime(birthdate,"%d-%m-%Y")
        self.now=datetime.now()

    def calculate_age_days(self):
        return (self.now-self.birthdate).days
    def calculate_age_years(self):
        return (self.now-self.birthdate).days/365
    
p=Person("Steni","07-07-2007")
print(p.calculate_age_days())
print(p.calculate_age_years())



from datetime import datetime

class Exam:
    def __init__(self,exam_date,sub):
        self.exam_date=datetime.strptime(exam_date,"%d-%m-%Y")
        self.sub=sub
        self.now=datetime.now()

    def days_left(self):
        re=(self.exam_date-self.now).days
        if re<0:
            return "Exam is over"
        
        return re
    
    def is_exam_over(self):
        re=(self.exam_date-self.now).days
        if re<0:
            print("Exam is over")
        else:
            print("Exam is not over")


exam=Exam("02-05-2026","maths")
print(exam.days_left())
exam.is_exam_over()


from datetime import datetime
import time

class Session:
    def __init__(self):
        self.__login_time=''
        self.__logout_time=''

    def login(self):
        self.__login_time=datetime.now()
    
    def logout(self):
        self.__logout_time=datetime.now()

    def duration(self):
        return self.__logout_time-self.__login_time

me=Session()
me.login()
time.sleep(3)
me.logout()
print(me.duration())
'''