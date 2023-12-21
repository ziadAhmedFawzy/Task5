def odd_eve(num):
    num = int(num)
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


# get number you check it even or odd
n = input("enter your num here : ")

print(odd_eve(n))
