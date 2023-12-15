def find_outlier(integers):
    chet = [i for i in integers if i % 2 == True]
    nechet = [i for i in integers if i % 2 == False]
    return chet[0] if len(chet) == 1 else nechet[0]
