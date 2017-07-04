def getCelsius(deg):
    result=round(((deg - 32) / 1.8),2)

    print("The coversion from Fahrenheit to celsius is : " + str(result))
    return result

deg=int(raw_input("Enter the degree in Fahrenheit \n"))
celsius=(getCelsius(deg))
#print getCelsius(55)
