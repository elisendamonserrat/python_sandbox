# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1

# Extend class

class Customer(User):
    def __init__(self, name, email, age):
        super().__init__(name, email, age)
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
    
    # def greeting(self):
    #     return f'My name is {self.name} and I am {self.age}. My balance is {self.balance}'

# Init user object
brad = User('Brad', 'eli@test.com', 30)

# Init Customer
janet = Customer('Janet', 'janet@gmil.com', '40')

print('Customer class', janet.greeting())
