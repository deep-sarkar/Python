class Calender:
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

c = Calender()
month = int(input('Month : '))
year = int(input('Year : '))
months = ["","January","February","March","April","May","June","July","August","September","Octobar","November","December"]
weeks = []
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


