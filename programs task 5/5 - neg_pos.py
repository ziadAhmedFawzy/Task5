def check_num(num):
    if num > 0:
        return "positive"
    else:
        return "negative"


# get number you want check it
n = int(input("enter your number : "))

print(check_num(n))
