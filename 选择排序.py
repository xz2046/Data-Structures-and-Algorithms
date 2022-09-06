def selectionSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        posittionofMax = 0
        for j in range(1, i + 1):
            if alist[j] > alist[posittionofMax]:
                posittionofMax = j

        alist[posittionofMax], alist[i] = alist[i], alist[posittionofMax]

    return alist


alist = [5, 3, 62, 15, 10, 6, 48, 12]
print(selectionSort(alist))
'''
比对时间为n^2
交换时间为n
'''

