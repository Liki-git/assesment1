value = float(input("Enter temperature value: "))
unit = input("Enter unit (C/F/K): ").upper()

if unit == "C":
    print("Fahrenheit:", (value * 9/5) + 32)
    print("Kelvin:", value + 273.15)

elif unit == "F":
    print("Celsius:", (value - 32) * 5/9)
    #print("Kelvin:", (value - 32) * 5/9 + 273.15)

elif unit == "K":
    print("Celsius:", value - 273.15)
    #print("Fahrenheit:", (value - 273.15) * 9/5 + 32)

else:
    print("Invalid unit! Use C, F, or K.")
