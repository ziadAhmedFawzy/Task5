def greatest(num1, num2):
    if num1 > num2:
        return "the %.2f is greatest" % num1
    else:
        return "the %.2f is greatest" % num2


# get numbers
n1 = float(input("enter your num : "))
n2 = float(input("enter your num : "))

print(greatest(n1, n2))
