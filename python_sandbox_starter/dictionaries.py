# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age': 30
}

# Constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get a value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '1234 55'

# Get dict Keys
print(person.keys())

# Get dic items
items = person.items()
print(person.items(), type(items), len(items))

# Copy a dict
person2 = person.copy()
person2['city'] = 'Barcelona'

# Remove item
del(person['age'])
person.pop('phone')

# Clear 
person.clear()

# Get length
#print(len(person2))

# List of dict
people = [
    { 'name': 'Martha', 'age': 25},
    { 'name': 'Penny', 'age': 1}
]

print(people[0]['name'])





