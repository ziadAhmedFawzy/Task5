def score(scr):
    if scr > 1.0:
        return "please enter numbers only between 0.0 and 1.0"
    elif scr < 0:
        return "please enter numbers only between 0.0 and 1.0"
    elif scr >= 0.9:
        return "your score({}) is A".format(scr)
    elif scr >= 0.8:
        return "your score({}) is B".format(scr)
    elif scr >= 0.7:
        return "your score({}) is C".format(scr)
    elif scr >= 0.6:
        return "your score({}) is D".format(scr)
    elif scr < 0.6:
        return "your score({}) is F".format(scr)
    else:
        return "please enter numbers only between 0.0 and 1.0"


# get score
num_of_score = float(input("enter the score here between 0.0 and 1.0 : "))

print(score(num_of_score))
