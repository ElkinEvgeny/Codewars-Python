import itertools
def latest_clock(a, b, c, d):
    time= max([str(i[0]) + str(i[1]) +str(i[2])+str(i[3]) for i in list(itertools.permutations([a, b, c, d], 4)) if (int(str(i[0]) + str(i[1]))<24 and int(str(i[2]) + str(i[3]))<60)])             
    timing = f"{time[:2]}:{time[2:]}"
    return timing
 