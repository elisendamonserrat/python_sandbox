# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1, 2,3,4]
fruits = [ 'Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numbers2 = list((2,3,4,5,6,7,8))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Wartermelon')

# Remove by a position, with pop
fruits.pop(2)

# Change value
fruits[0] = 'Banana'

# Reverse list
fruits.reverse()

# Sort list alphabetically
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)
print(fruits)