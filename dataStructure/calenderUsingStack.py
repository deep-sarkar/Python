from stack import *
from utilDataStructure import *

class CalenderUsingQueue:
    q = Stack()
    c = UtilDataStructure()
    month = int(input('Month : '))
    year = int(input('Year : '))
    months = ["","January","February","March","April","May","June","July","August","September","Octobar","November","December"]
    days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and c.is_leapyear(year):
        days[month] = 29
    day = c.day_of_week(1,month,year)
    week = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    week.reverse()
    
    
    for i in range(days[month],0,-1):
        q.push(i)                  #pushing days of month in queue
    for i in range(day):
        q.push("   ")              #pushing empty string in queue for no dame month date on day
    for i in week:             
        q.push(i)                  #Pushing week days in queue



    print("   ",months[month],"   ",year)
    count = 1
    while q.size() != 0:
        date = q.pop()                   #Dequeuing queue one by one till size reach to 0
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