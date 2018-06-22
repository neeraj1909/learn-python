"""
The datetime module provides time objects that are similar to the Time objects in
this chapter, but they provide a rich set of methods and operators. Read the docu‐
mentation at http://docs.python.org/3/library/datetime.html.

1. Use the datetime module to write a program that gets the current date and prints
the day of the week.

2. Write a program that takes a birthday as input and prints the user’s age and the
number of days, hours, minutes and seconds until their next birthday.

3. For two people born on different days, there is a day when one is twice as old as
the other. That’s their Double Day. Write a program that takes two birthdays and
computes their Double Day.

4. For a little more challenge, write the more general version that computes the day
when one person is n times older than the other.
"""

from datetime import date, timedelta, datetime
import calendar


def calculate_day_of_week():
        my_date = date.today()
        week_day = calendar.day_name[my_date.weekday()]
        print(week_day)

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def calculation_of_next_birthday(self):
        birth = datetime(self.year, self.month, self.day)
        current_time = datetime.now()

        current_age = current_time.year - birth.year - ((current_time.month, current_time.day) < (birth.month, birth.day))
        # print("Current age of the user is: %s\n" % current_age)

        if (current_time.month, current_time.day) < (birth.month, birth.day):
            next_bday = (current_time.year, birth.month, birth.day)
        else:
            next_bday = (current_time.year + 1, birth.month, birth.day)

        time_to_next_bday = datetime(*next_bday) - current_time
        return time_to_next_bday


    def double_day_calculation(self, bday2):
        person1 = date(self.year, self.month, self.day)
        person2 = date(bday2.year, bday2.month, bday2.day)

        age_differece =  person2 - person1

        p1 = int(age_differece.days)
        p2 = 0

        while (2 * p2) != p1:
            p1 += 1
            p2 += 1

        date_at_twice_age = person2 + timedelta(days = p2)
        return (date_at_twice_age, p1, p2)


    def nth_time_older_calculation(self, bday2, n):
        person1 = date(self.year, self.month, self.day)
        person2 = date(bday2.year, bday2.month, bday2.day)

        age_differece =  person2 - person1

        p1 = int(age_differece.days)
        p2 = 0

        while (n * p2) != p1:
            p1 += 1
            p2 += 1

        date_at_nth_times_age = person2 + timedelta(days = p2)
        return (date_at_nth_times_age, p1, p2)

if __name__ == '__main__':
    calculate_day_of_week()
    print("\n")

    b_day = Date(2012, 12, 3)
    next_bday = b_day.calculation_of_next_birthday()
    print("The next birthday will be: %s\n" % (next_bday))

    bday1 = Date(2000, 2, 1)
    bday2 = Date(2002, 3, 29)

    (date_at_twice_age, p1, p2) = bday1.double_day_calculation(bday2)
    print("Date at twice age will be: %s\nAt double day, Person1 will be %d days old and Person2 will be %d days old\n" % (date_at_twice_age, p1, p2))

    n = int(input("Enter the value of n: "))
    (date_at_nth_times_age, p1, p2) = bday1.nth_time_older_calculation(bday2, n)
    print("Date at nth times age will be: %s\nAt that time day, Person1 will be %d days old and Person2 will be %d days old\n" %(date_at_nth_times_age, p1, p2))
