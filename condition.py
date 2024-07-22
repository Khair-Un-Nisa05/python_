temp =float(input("enter temperature:"))
unit = input("enter unit(C,F,K):")

if unit =="C":
    fahrenheit = 5/9*temp+32
    kelvin=temp+273.15
    print("[temp]C is equal to [fahrenheit]F and [kelvin]K")
elif unit == "K":
    celsius = temp -273.15
    fahrenhiet = (temp - 273.15)*95 +32 
    print("[temp]K is equal to [celsius]C and [fahrenheit]F")
elif unit == "F":
    celsius = (temp -32)*5/9
    kelvin = (temp -32)*5/9+273.1
    print("[temp]F is equal to [celsius]C and [kelvin]K")
else:
    print("invalid unit")
