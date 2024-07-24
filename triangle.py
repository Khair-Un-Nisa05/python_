a = int(input("enter the length:"))
b =int(input("enter the length:"))
c =int(input("enter the length:"))

if a == b == c:
    print("Equilateral Triangle")
elif a== b or b == c or c == a:
    print("Isosceles Triangle")
else:
    print("Scalene triangle")