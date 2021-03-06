#variables
'''
x = 4
y = x + 1

print(x)
print(y)
'''
#Datatypes

#integers and float
'''
x = 4.5
y = x + 1.0

print(x)
print(y)
'''

#Strings

# Strings can contain letters, a-z:
example1 = 'Ariel'
print(example1)

# Strings can be indicated using single or double quotes:
example2 = 'Ariel'
example3 = "Ariel"
print(example2)
print(example3)

# Strings can also contain numbers and letters:
example4 = 'Ariel is 30 years old'
print(example4)

# Or numbers and letters and symbols:
example5 = 'Ariel stubbed her toe and exclaimed f00b@r!'
print(example5)

# Or, just numbers:
example6 = '30'
print(example6)

#Lists

# A list can contain strings:
shopping_list = ['apples','oranges','pears']
print(shopping_list)

# Integers:
prices1 = [4, 9, 5]
print(prices1)

# Floats:
prices2 = [4.0, 9.99, 5.02]
print(prices2)

# Integers and floats:
prices = [4.0, 9, 5]

# Or integers, and strings, and floats
randomness = ['apples', 4.0, 9, 'huh?']
print(randomness)

# Or even other lists!
roster = [['Ariel', 4.0, 42], ['Jill', 3.1, 99]]
print(roster)

#Concatenation operation

first_name = 'Ariel'
last_name = 'Brewer'

# Join a String and a variable that contains a String
print('Student first name: ' + first_name)
print('Student last name: ' + last_name)

# Join a couple strings and a couple variables
print('Student name: ' + first_name + ' ' + last_name)
# Note how the empty space is created between the first and last name

age = 30
first_name = 'Ariel'
print(first_name + ' is ' + str(age) + ' years old.')
