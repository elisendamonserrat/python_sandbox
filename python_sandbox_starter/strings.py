# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Brad'
age = 37

# Concatenate strings
# print('Hello, my name is ' + name + ' ' + str(age))

# String Formatting

# Arguments by position
# print('My name is {name} and i am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello again, my name is {name} and I am {age}')

# String Methods

s = 'hello WORLD'

# Capitalize string
print(s.capitalize())
print('upper', s.upper())
print('swapcase', s.swapcase())
print('get length', len(s))
print('replace', s.replace('world', 'developer'))

sub = 'h'
print('Nº of h => return a INT', s.count(sub))

print('starts with => returns a Boolean', s.startswith('o'))

splitS = s.split()
print('split => returns a list (arr) such as [a, b]', splitS)

print('find => return the position of a char', s.find("W"))
# if there is no such character it will return -1