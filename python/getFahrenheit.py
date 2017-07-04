def getFahrenheit(deg):
    result=round(((deg * 1.8) + 32),1)

    print("The coversion from celsius to Fahrenheit is : " + str(result))
    return result

deg=int(raw_input("Enter the degree in celsius \n"))
Fahrenheit=(getFahrenheit(deg))
#print getFahrenheit(10)
