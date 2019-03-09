import datetime

''' F-STRING METHOD: which are new to python 3.6+'''

first_name = 'Corey'
last_name = 'Schafer'

# Old way using the format method
sentence = 'FORMAT METHOD: My name is {} {}'.format(first_name, last_name)
print(sentence)

# New way using f-strings.
sentence = f'F-STRINGS: My name is {first_name} {last_name}'
print(sentence)

# Can also run functions within F-Strings
sentence = f'F-STRINGS: My name is {first_name.upper()} {last_name.upper()}'
print(sentence)

# Working with dictionary
person = {'name': 'Jenn', 'age': 23}

# This wont compile due to single quote used more than once:
# sentence = f'My name is {person['name']} and I am {person['age']} years old.''age'])

sentence = f"My name is {person['name']} and I am {person['age']} years old."
print(sentence)

# Working with numbers
calculation = f"4 times 11 is equal to {4 * 11}"
print(calculation)

for n in range(1, 11):
    sentence = f'The value is {n:02}'   # Pad by three digits
    print(sentence)

# Working with dates
birthday = datetime.datetime(1990, 1, 1)
sentence = f"Jenn had a birthday on {birthday}"
print(sentence)

sentence = f"Jenn had a birthday on {birthday:%B %d, %Y}"
print(sentence)

'''USING THE FORMAT METHOD'''

person = {'name': 'Jenn', 'age': 23}

# Bad way
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

# Better way
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)

# Clearer Way.  Also access values of a list this way.
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)


tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')

# Printing class attributes
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

# Using placeholder
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print(sentence)

# Using keyword arguments to unpack  from a dictionary
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

# Best way to format numbers - note ':' denotes you want to do some formatting
for i in range(1, 11):
    sentence = 'The value is {:03}'.format(i)   # pad numbers
    print(sentence)

# specify decimal places
pi = 3.14159265
sentence = 'Pi is equal to {:.3f}'.format(pi)
print(sentence)

# Add a comma separator to large number
sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)

# Formatting and printing out dates


my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

# This format - March 01, 2016
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.  '0' used to indicate single placeholder
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)

