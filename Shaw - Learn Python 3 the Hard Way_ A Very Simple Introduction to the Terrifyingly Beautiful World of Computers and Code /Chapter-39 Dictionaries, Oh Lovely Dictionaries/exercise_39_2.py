"""
Find the Python documentation for dictionaries and try to do even more things to them.
"""

for i, v in enumerate(['a', 'b', 'c']):
    print(i , v)


states = ['bihar', 'hariyana', 'jharkhand']
cities = ['patna', 'chandigarh', 'ranchi']

for state, city in zip(states, cities):
    print("Your state is {0} and city is {1}.".format(state , city))

