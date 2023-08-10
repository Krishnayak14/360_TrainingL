# 4. Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

class Time:
    def __init__(self, hours, minutes):
         self.hours = hours
         self.minutes = minutes


    def addTime(self , other_time):
        hours = self.hours + other_time.hours
        mins = self.minutes + other_time.minutes
        if (mins >= 60):
            carryHours = mins // 60
            hours = hours + carryHours
            mins = mins % 60
        addedTime = Time(hours, mins)
        return addedTime


    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")


    def displayMinute(self):
        total_time = self.hours * 60 + self.minutes
        print(total_time, "minutes")

time1 = Time(10,40)
time2 = Time(5,50)

result = time1.addTime(time2)


print("Time 1:")
time1.displayTime()
time1.displayMinute()

print("Time 2:")
time2.displayTime()
time2.displayMinute()

print("Sum:")
result.displayTime()
result.displayMinute()
