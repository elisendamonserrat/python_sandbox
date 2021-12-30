# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
from time import time

# Pip module
from camelcase import CamelCase


# import custome module
from validator import validate_email, validate_user


# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
# print(c.hump('hello world'))

email = 'testtest.com'

if validate_email(email):
    print(f'Your {email} is valid')
else:
    print(f'Your {email} is not valid')

