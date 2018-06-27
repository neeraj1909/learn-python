"""
Is it possible to use a class like it’s an object?
"""

print("Everything in Python is an object, including classes.")
print("This means you can reference classes, passing them around like arguments, store them in attributes,")
print("(extra) names, lists, dictionaries etc.")

print("\nThis is perfectely normal in Python:  \n")
print("class_map = {")
print("    'foo': A,")
print("    'bar': SomeOtherClass,")
print("    'baz': YetAnother")
print("}\n")
print("instance = class_map[some_variable]()\n")

print("Now it depends on the some_variable what class was picked to create an instance;")
print("the class_map dictionary values are all classes.\n")

print("Classes are themselves instance of their type; this is called the metaclass.")
print("You can produce a new class by calling type() with a name, a sequence of base classes,")
print("and a mapping defining the attributes of the class:\n")

print("type('DynamicClass', (), { 'foo': 'bar'})\n")
print("cretae a new class object , with a foo attibute set to bar.")
