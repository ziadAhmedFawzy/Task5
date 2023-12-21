# get_inputs
_count_ = 0
_sum_ = 0
ave_and_cou = 10

while _count_ < ave_and_cou:
    # get nums is ADD in sum
    num = int(input(f"enter your num{_count_ + 1}: "))
    # ADD num in sum
    _sum_ += num
    # ADD 1 in count
    _count_ += 1

# do average
print(_sum_ / ave_and_cou)
