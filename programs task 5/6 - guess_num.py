def guess(num):
    if num == 6:
        return True
    else:
        return False


n = int(input("enter integer num to guess number : "))
print(guess(n))
