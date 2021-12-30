# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print(f'Name: {myFile.name}')
print(f'Is closed: {myFile.closed}')
print(f'Opening Mode: {myFile.mode}')

# Write to file
myFile.write('I love Python')
myFile.write(' and JV')
myFile.close()

myFile = open('myfile.txt', 'a')
myFile.write(' I also like CSS')
myFile.close()


myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
