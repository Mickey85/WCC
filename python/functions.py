'''def multiply(a, b):
    result = a * b
    return result

# Test the function:
'''
'''solution = multiply(4, 5) # Invoke multiply giving it the arguments 4 and 5
print(solution) # Expected: 20
'''
'''print(multiply(4,5))
# Test the function
print(multiply(4,5)) # 20
print(multiply(9,11)) # 99
print(multiply(0,10)) # 0
print(multiply(.5,9)) # 4.5
print(multiply(-1, -55)) # 55
print(multiply(3, 'Hello')) # 'HelloHelloHello'

'''
'''
def cube(a):
    product = a * a * a
    return product
'''

'''def mystery(x, y, z):
    output = x + y * z
    return output

# Test this function:
print mystery('Hello', 3, '!')
print mystery('Goodbye', 2, '@')
'''
def calculate_tip(price,rating):
    price=float(price)
    rating = str(rating)
    if(rating =='A'):
        tip = price * 0.20
        return tip
    elif (rating == 'B'):
        tip = price * 0.18
        return tip
    elif (rating == 'C'):
        tip = price * 0.15
        return tip

print(calculate_tip(30.50, 'C')) # Expected: 4.575
print(calculate_tip(15.00, 'B')) # Expected: 2.7
print(calculate_tip(20.00, 'A')) # Expected: 4
