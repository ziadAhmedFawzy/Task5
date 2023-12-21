nums = [5, 15, 3, 20, 74, 90, 80, 13]

smallest_num = -1
largest = 0
for num in nums:
    if smallest_num < num:
        smallest_num = num
        largest = num

print(largest)
