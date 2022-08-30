def listSum(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + listSum(l[1:])


l = [1, 2, 3, 4, 5, 6]
print(listSum(l))
