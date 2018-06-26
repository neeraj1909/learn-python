"""
Research why Python added this strange object class and what that means.
"""

print("A user define type is also called as a class.")
print("A class definition looks like this:\n")
print("class Point(object): ")
print('   """ Represents a point in 2-D space."""\n')
print("This header indicates that the new class is a Point, which is a kind of object, which is a built-in type")

print("_______________________________________________________________________________________________________________\n")

print("OOPs revolves around objects instead of procedures. An object is an entity which contains data")
print("as well as procedures that operates on the data.")
print("Before we create objects, we first have to define a class. A class is just a blueprint.\n")
print("The syntax of defining class is as follows- \n")
print("class class_name(parent_class_name): ")
print("    <method_1_definition>")
print("    . . . .")
print("    <method_2_definition>\n")
print("The class definition is divided into two parts: ")
print("   1. class header    and   2. class body\n")
print("The class header starts with class keyword followed by the optioal parent_class_name inside parenthesis.\n")
print("The parent-class_name class refers to the class you want to inherit from. This is known as Inheritance.\n")
print("If you don't specify parent class name while defininng a class, it will atomatically set to object.")
