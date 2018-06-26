"""
Fill out the animals, fish, and people in this exercise with functions that make them do things.
See what happens when functions are in a “base class” like Animal versus in, say, Dog.
"""


## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ??dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Person has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):

    def __init__(self, name):
        self.name = name

## Salmaon is-a Fish
class Salmon(Fish):

    def __init__(self, color, geographic_region):
        self.color = color
        self.geographic_region = geographic_region

## Halibut is-a Fish
class Halibut(Fish):

    def __init__(self, color, geographic_region):
        self.color = color
        self.geographic_region = geographic_region

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Fish
mary = Person("Mary")

## mary has-a pet attibute
mary.pet = satan

## frank is-a instance of Employee
frank = Employee("Frank", 120000)

## frank has-a pet attribute
frank.pet = rover

## flipper is-a instance of Fish
flipper = Fish('name')

## crouse is-a instance of Salmaon
crouse = Salmon('color', 'geographic_region')

## harry is-a instance of Halibut
harry = Halibut('color', 'geographic_region')
