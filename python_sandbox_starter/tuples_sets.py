# A Tuple is a collection which is ordered and **unchangeable**. Allows duplicate members.
 
# Creat tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Single value needs trailing comma
fruits2 = ('Apple',)

# Get value
value1 = fruits[0]

# Can't change value ==> values are unchangeable
# fruits[0] = 'Pears'

# Delete tuple
# del fruits

# Get length
# print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'apple', 'orange', 'mango'}

# Check if sth in a set
print('apple' in fruits_set)

# Add to set
fruits_set.add('grape')

# Remove from set
fruits_set.remove('grape')

# Clear set
fruits_set.clear()

# Delete set
del fruits_set

print(fruits_set)
