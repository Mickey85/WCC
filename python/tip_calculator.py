amount=raw_input("How much was your meal? ")

tip = float(amount) * 0.20
print("you should tip $" + str(tip))

total_cost = float(tip) + float(amount)

print('your total cost would be $' + str(total_cost))
