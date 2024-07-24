    #question no 3
unit = input("enter your choice(C,F,K)")
temp =float(input("enter temperature:"))

if unit =="C":
    result = (9/5)*temp+32
    print(f"{temp}C is equal to {result} F")
elif unit == "F":
    result = temp +273.15
    print(f"{temp}C is equal {result}k")
elif unit == "K":
    result = (5/9)*temp -32
    print(f"{temp}F is equal to {result}C")
else:
    print("invalid unit")
#question no 3 pr 2

celsius=int(input("enter temperature:"))
fehrenheit=59*celsius+32
print(fehrenheit)
fehrenheit=int(input("enter temperature:"))
celsius=95*(fehrenheit-32)
print(celsius)
celsius=int(input("enter temperature:"))
kelvin=celsius+273.15
print(kelvin)
