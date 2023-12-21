def calc_pay(hours, rate):
    if hours <= 40:
        pay = hours * rate
        return pay
    else:
        rem = hours - 40
        bonus = rem * 1.5 * rate
        pay = 40 * rate + bonus
        return pay


h = float(input("enter your hours : "))
r = float(input("enter your rate : "))

print(calc_pay(h, r))
