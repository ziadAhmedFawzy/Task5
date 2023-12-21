def pay(hour, rate):
    return hour * rate


h = int(input("please enter your hours : "))
r = float(input("please enter your rate : "))

print(f"the pay should be {pay(h, r)}")
