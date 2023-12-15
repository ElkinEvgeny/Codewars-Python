def next_bigger(number):
    number_1 = number
    if list(str(number_1)) == list(reversed(sorted(str(number_1)))):
        return -1
    qwer = number + 9
    while sorted(str(number)) != sorted(str(qwer)):
        qwer += 9
    return qwer
