def getCelsius(deg):
    result=round(((deg - 32) / 1.8),2)

    print("The coversion from Fahrenheit to celsius is : " + str(result))
    return result

#deg=int(raw_input("Enter the degree in Fahrenheit \n"))
#celsius=(getCelsius(deg))
#print getCelsius(55)
def getFahrenheit(deg):
    result=round(((deg * 1.8) + 32),1)

    print("The coversion from celsius to Fahrenheit is : " + str(result))
    return result

#deg=int(raw_input("Enter the degree in celsius \n"))
#Fahrenheit=(getFahrenheit(deg))
#print getFahrenheit(10)

def temperatureConverter(deg,converter):

    if (converter == 'C'):
        celsius = getCelsius(deg)
        return celsius
    elif(converter == 'F'):
        Fahrenheit = getFahrenheit(deg)
        return Fahrenheit
    elif((converter != 'C') and (converter !='F')):
        return "Invalid temperature Scale ; Must be 'F' or 'C'"


print temperatureConverter(55, 'C') # 12.7777777778
print temperatureConverter(10, 'F') # 50.0
print temperatureConverter(55, 'X')
