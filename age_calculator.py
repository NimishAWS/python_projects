import datetime 

year = int(input("Please enter the year:- "))
month = int(input("Please enter the month:- "))
day = int(input("Please enter the day:- "))

def age_calc(year,month,day):
    today_date = datetime.datetime.now().date()
    dob = datetime.date(year,month,day)
    age = int((today_date - dob).days/365)
    print(age)

age_calc(year,month,day)