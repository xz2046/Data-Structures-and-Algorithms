def orderSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True  # 增加了提前结束条件
            else:
                pos = pos + 1

    return found


alist = [1, 2, 3, 4, 5, 66, 88, 95]
print(orderSequentialSearch(alist, 3))
print(orderSequentialSearch(alist, 77))

'''
循序查找时间复杂度为O(n)
目标存在：最好为1，最差为n，平均为n/2
目标不存在：最好为1，最差为n，平均为n/2
'''
