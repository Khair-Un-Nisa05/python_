n = int(input("enter a number:"))
fac = 1
for i in range(1, n+1):
    fac *= i
    print("factorial=",fac)