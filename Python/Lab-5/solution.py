import math as math
print("="*36)
print("          ENGINEERING CALCULATION TOOL")
print("="*36)
num=float(input("Enter a numerical value:"))
exp=float(input("Enter an exponent:"))
decimal_val=float(input("Enter a Decimal Measuarement:"))

power= math.pow(num, exp)
square= math.sqrt(num)
ceil_val= math.ceil(decimal_val)
floor_val= math.floor(decimal_val)

print("\n--- Results ---")
print("Value: ", num)
print("Exponent: ", exp)
print("Poer(pow): ", power)
print("Squareroot(sqrt): ", square)
print("Decimal Value: ", decimal_val)
print("Ceil Value: ", ceil_val)
print("Floor Value: ", floor_val)

print("="*26)