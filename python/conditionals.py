temp = int(raw_input('What is the temperature?'))

print('You should bring the following items:')
if temp <= 40:
    print('Coat')
    print('Hat')
    print('Gloves')
elif temp <= 70:
    print('Coat')
    print('Hat')
else:
    print('Nothing!')


age = int(raw_input('How old are you?'))

if age > 16:
    print('You can drive')
if age > 18:
    print('You can vote')
if age > 21:
    print('You can join the military')
if age > 75:
    print('You can retire')
