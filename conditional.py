#QUESTION NO 1
marks = int(input("enter student marks:"))

if(marks >= 70):
    grade =" A"
elif(marks >= 60):
    grade =" B"
elif(marks >= 50):
    grade= "C"
else:
    grade = "D"
print("grade of the student->",grade)

#QUESTION NO 2
year = int(input("enter a year:"))
if(year % 4 == 0 ):
    (year % 400 == 0)
    print (year, "is a leap year")

elif(year % 100 != 0):
     print(year,"is not leap year")

     #question no 3
celsius= int(input("enter temperature in celsius:"))
f= celsius *(9/5)+32
print ("fahrenheit",f)

f=int(input("enter a temperature in fahrenhheit:"))
c = 9/5(f-32)
print("celsius",f)

c = int(input("enter a temperature in celsius: "))
k = c+ 273.15
print("kelvin", c)
