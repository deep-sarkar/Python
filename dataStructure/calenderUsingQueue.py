from queue import *
class CalenderUsingQueue:
    def day_of_week(self,day,month,year):
        y1 = year - (14-month)//12
        x = y1 + y1//4 - y1//100 + y1//400
        m1 = month + 12 * ((14-month)//12) - 2
        d1 = (day + x + (31 * m1)//12) % 7
        return d1

    def is_leapyear(self,year):
        if year%400 == 0 or year%100 != 0 and year%4 == 0:
            return True
        return False

q = Queue()
c = CalenderUsingQueue()
month = int(input('Month : '))
year = int(input('Year : '))
months = ["","January","February","March","April","May","June","July","August","September","Octobar","November","December"]
days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if month == 2 and c.is_leapyear(year):
    days[month] = 29
day = c.day_of_week(1,month,year)
week = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
for i in week:
    q.enqueue(i)
for i in range(day):
    q.enqueue("   ")
for i in range(1,days[month]+1):
    q.enqueue(i)


print("   ",months[month],"   ",year)
count = 1
while q.size() != 0:
    date = q.dequeue()
    if type(date) != int:
        if type(date) == "   ":
            print(date,end=" ")
        else:
            print(date,end=" ")
    if count > 7:
        if type(date) == int:
            if date <= 5:                               
                print("", date, " ", end="")
            if 5 < date < 10:                            
                print("", date, " ", end="")
            if date > 9:                                  
                print("", date, "", end="")
    if count % 7 == 0:
        print()
    count += 1