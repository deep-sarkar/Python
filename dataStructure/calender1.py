from utilDataStructure import *
class Calender:
    c = UtilDataStructure()
    month = int(input('Month : '))
    year = int(input('Year : '))
    months = ["","January","February","March","April","May","June","July","August","September","Octobar","November","December"]
    days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and c.is_leapyear(year):
        days[month] = 29
    print("   ",months[month],"   ",year)
    day = c.day_of_week(1,month,year)
    print(day)

    print("Sun Mon Tue Wed Thu Fri Sat")
    for i in range(day):
        print("   ",end=" ")
    for i in range(1,days[month]+1):
        if i <= 5:                               
            print("", i, " ", end="")
        if 5 < i < 10:                            
            print("", i, " ", end="")
        if i > 9:                                  
            print("", i, "", end="")
        if (i + day) % 7 == 0:                     
            print()


