def bubbleSort(alist):
    exchanges = True
    i = len(alist) - 1
    while i > 0 and exchanges:
        exchanges = False  # 如果一轮没有进行交换，则完成排序，提前结束
        for j in range(i):
            if alist[j] > alist[j + 1]:
                exchanges = True
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
        i = i - 1
    return alist


alist = [5, 3, 62, 15, 10, 6, 48, 12]
print(bubbleSort(alist))

'''
时间复杂度为O(n^2)
比对时间为n^2
交换时间为n^2
无需额外空间开销，适应性比较广泛
'''
