"""
write a function called print_time that takes a Time object and prints
it in the form hour:minute:second . Hint: the format sequence '%.2d' prints an inte‐
ger using at least two digits, including a leading zero if necessary.

Write a boolean function called is_after that takes two Time objects, t1 and t2 , and
returns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t
use an if statement.
"""


class Time:
    """Represents time in the form hour:minute:second"""

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))

    def is_after(self, other):
        return (self.hour, self.minute, self.second) > (other.hour, other.minute, other.second)

    def time_to_integer(self, time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def integer_to_time(self, seconds):
        time = Time(0, 0, 0)
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def add_time(self, time, other):
        seconds = self.time_to_integer(time) + self.time_to_integer(other)
        time = self.integer_to_time(seconds)
        return time

if __name__ == '__main__':
    t1 = Time(10, 20, 37)
    t1.print_time()

    t2 = Time(8, 20, 12)
    t3 = Time(11, 10, 18)
    t4 = Time(10, 20, 37)
    result1 =  t1.is_after(t2)
    result2 = t1.is_after(t3)
    result3 = t1.is_after(t4)


    print("result of t2: %s" % result1)
    print("result of t3: %s" % result2)
    print("result of t4: %s" % result3)

    time_after_adding = t2.add_time(t2, t3)

    print("time after adding: %.2d:%.2d:%.2d" %(time_after_adding.hour, time_after_adding.minute, time_after_adding.second))
