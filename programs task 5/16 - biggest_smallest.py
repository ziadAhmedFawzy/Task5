n1 = int(input("enter num1 : "))
n2 = int(input("enter num2 : "))
n3 = int(input("enter num3 : "))

if n1 > n2 and n1 > n3:
    print("the biggest is ", n1)
elif n2 > n1 and n2 > n3:
    print("the biggest is ", n2)
else:
    print("the biggest is ", n3)

if n1 < n2 and n1 < n3:
    print("the smallest is ", n1)
elif n2 < n1 and n2 < n3:
    print("the smallest is ", n2)
else:
    print("the smallest is", n3)
