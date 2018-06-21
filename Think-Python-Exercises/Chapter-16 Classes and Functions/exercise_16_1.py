"""
Write a function called mul_time that takes a Time object and a number and returns a
new Time object that contains the product of the original Time and the number.

Then use mul_time to write a function that takes a Time object that represents the
finishing time in a race, and a number that represents the distance, and returns a
Time object that represents the average pace (time per mile).
"""

class Time:
    """Represents time in the form hour:minute:second"""

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_integer(self, time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def integer_to_time(self, seconds):
        time = Time(0, 0, 0)
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def mul_time(self, time, number):
        seconds = self.time_to_integer(time)
        new_seconds = seconds * number
        new_time = self.integer_to_time(new_seconds)
        return new_time

    def calculate_average_pace(self, time, number):
        seconds = self.time_to_integer(time)
        time_per_mile_in_seconds = seconds // number
        average_pace_time = self.integer_to_time(time_per_mile_in_seconds)
        return average_pace_time

if __name__ == '__main__':
    t = Time(5, 20, 30)
    number = 5
    new_time = t.mul_time(t, number)
    print("new time object is: %.2d:%.2d:%.2d\n" % (new_time.hour, new_time.minute, new_time.second))

    average_pace_time = t.calculate_average_pace(t, number)
    print("average pace time: %.2d:%.2d:%.2d \n" % (average_pace_time.hour, average_pace_time.minute, average_pace_time.second))
