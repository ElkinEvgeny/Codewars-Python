def order_weight(strng):
    a = sorted(strng.split(' '))
    s = sorted(a, key=ram)
    return " ".join(s)


def ram(n):
    return sum([int(item) for item in n])
