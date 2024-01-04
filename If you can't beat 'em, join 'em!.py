def cant_beat_so_join(numbers):
    list = []
    while len(numbers) > 0:
        a = max(numbers, key=lambda x: sum(x))
        list = list+a
        numbers.remove(a)
    return list
