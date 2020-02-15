import datetime
class StopWatch:
    #Method to start STOPWATCH
    def start_stopWatch(self) :
        a = str(input("Enter \'S\' to start : "))
        start_timer = a.upper()
        if start_timer == "S":
            print('Stop watch started !!!')
            return datetime.datetime.now()
        else :
            print('Wrong input....!!!!!!')
            return self.start_stopWatch()
    #Method to stop STOPWATCH
    def stop_stopWatch(self) :
        b = str(input('Enter \'T\' to stop : '))
        stop_timer = b.upper()
        if stop_timer == "T":
            print('Stop watch stoped !!!')
            return datetime.datetime.now()
        else :
            print('Wrong input...!!!!!!')
            return self.stop_stopWatch()
    #Method calculating ELAPSED time
    def elapsed_time(self) :
        __start_time = self.start_stopWatch()
        print(__start_time)
        __stop_time = self.stop_stopWatch()
        print(__stop_time)
        print('Elapsed time is : ', __stop_time - __start_time)

ref = StopWatch()
ref.elapsed_time()