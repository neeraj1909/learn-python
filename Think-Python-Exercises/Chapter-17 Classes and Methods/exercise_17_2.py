"""
This exercise is a cautionary tale about one of the most common, and difficult to find,
errors in Python. Write a definition for a class named Kangaroo with the following
methods:

1. An __init__ method that initializes an attribute named pouch_contents to an
empty list.

2. A method named put_in_pouch that takes an object of any type and adds it to
pouch_contents .

3. A __str__ method that returns a string representation of the Kangaroo object
and the contents of the pouch.


Test your code by creating two Kangaroo objects, assigning them to variables named
kanga and roo , and then adding roo to the contents of kanga ’s pouch.
"""


class Kangaroo(object):
    """docstring for Kangaroo"""
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, item):
        return self.pouch_contents.append(item)

    def __str__(self):
        return "I have {} in my pouch".format(self.pouch_contents)

    def __repr__(self):
        return 'Kangaroo <{}>'.format(self.pouch_contents)

obj1 = Kangaroo()
obj2 = Kangaroo()

obj1.put_in_pouch('wallet')
obj1.put_in_pouch('car keys')
# obj2.put_in_pouch('xyz')
obj1.put_in_pouch(obj2)


print(obj1)
print('')

print(obj2)

