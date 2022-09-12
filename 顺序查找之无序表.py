def sequentialSearch(alist: list, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


alist = [1, 23, 5, 4, 78, 9, 62, 13]
print(sequentialSearch(alist, 13))
print(sequentialSearch(alist, 77))

'''
循序查找时间复杂度为O(n)
目标存在时最好为1，最差为n，平均为n/2
目标不存在都为n
'''
