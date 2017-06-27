print(1==1)
print(1 == 2) # Expected output: False

print(1 > 2) # Expected output: false

print(2 > 1) # Expected output: True

print(1 >= 1) # Expected output: True

print(2 == 2) # Expected output: true

print(2 != 2) # Expected output: false

age = 30

print(age > 10) # Expected outcome: True

print(10 < age) # Expected outcome: True

print(age > 10 + 20) # Expected outcome: false

print(age + 20 > 10) # Expected outcome: True


print ("alphabetical order ")

print('a' > 'z') # Expected outcome: false

print('z' > 'a') # Expected outcome: True

print('apples' > 'oranges') # Expected outcome: false

print('oranges' > 'apples') # Expected outcome: True

print('cat' > 'car') # Expected outcome: True

print('car' > 'cat') # Expected outcome: false

#logical operators

age = 1
print(age > 12 and age < 19) # Expected outcome: false

age = 14
print(age > 12 and age < 19) # Expected outcome:True

age = 19
print(age > 12 and age < 19) # Expected outcome: false

age = 18
print(age > 12 and age < 19 and age != 5) # Expected outcome: True

age = 5
print(age > 12 and age < 19 and age != 5) # Expected outcome: false

age = -1
print(age > 12 and age < 19) # Expected outcome: False

age = 10
print(age > 25 and age < 15) # Expected outcome:   false


# Could the above expression ever be True?





gesture = 'rock'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome:True

gesture = 'pape'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome:False





# test
age = int(raw_input('How old are you?'))
#print((age >= 5)and (age <=10))

#print ((age >4) and (age<11))
