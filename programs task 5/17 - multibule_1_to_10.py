num = int(input("enter your num : "))

counter = 1
result = 0

while counter <= 10:
    result = num * counter
    print("{} * {} = {}".format(num, counter, result))
    counter = counter + 1
