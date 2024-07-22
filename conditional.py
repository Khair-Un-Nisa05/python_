#QUESTION NO 1
studentname = (input("enter your name:"))
marks = int(input("enter student marks:"))

if(marks >= 90 ):
    grade =" A"
elif(marks >= 70):
    grade =" B"
elif(marks >= 60):
    grade= "C"
elif(marks >= 50):
    grade = "D"
else:
    grade = "F"
print("Marksheet:")
print("grade of the student:",grade)

#QUESTION NO 2
year = int(input("enter a year:"))

if(year % 4 == 0 ) and (year % 100 == 0):
    print (year, "is a leap year")
elif (year % 4 == 0) or (year % 100!= 0):
    print(year, "is a leap year")
else:
     print(year,"is not leap year")

     #question no 3
unit = input("enter your choice(C,F,K)")
temp =float(input("enter temperature:"))

if unit =="C":
    result = (9/5)*temp+32
    print(f"{temp}C is equal to{result} F")
elif unit == "F":
    result = temp +273.15
    print(f"{temp}C is equal {result}k")
elif unit == "K":
    result = (5/9)*temp -32
    print(f"{temp}F is equal to {result}C")
else:
    print("invalid unit")

#QUESTION NO 4

a = int(input("enter the length:"))
b =int(input("enter the length:"))
c =int(input("enter the length:"))

if a == b == c:
    print("Equilateral Triangle")
elif a== b or b == c or c == a:
    print("Isosceles Triangle")
else:
    print("Scalene triangle")


