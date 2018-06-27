"""
Do this same kind of mapping with cities and states/regions in your country or some other
country.
"""

states = {
    'uttar pradesh': 'up',
    'bihar': 'br',
    'delhi': 'dl',
    'hariyana': 'hr',
    'madhya pradesh': 'mp'
}

cities = {
    'up': 'allahabad',
    'mp': 'vidisha',
    'dl': 'north-delhi',
    'hr': 'chandigarh',
    'br': 'buxar'
}

print("up state has: " + cities['up'])
print("mp state has: " + cities['mp'])
print("br state has: " + cities['br'])
print('-' * 10)

print("uttar pradesh's abbreviation is: " + states['uttar pradesh'])
print("bihar's abbreviation is: " + states['bihar'])
print("hariyana's abbreviation is: " + states['hariyana'])
print("-" * 10)

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has the city {city}")

