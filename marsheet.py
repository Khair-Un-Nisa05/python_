#QUESTION NO 1
print("marksheet")
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
print("grade of the student:",grade)