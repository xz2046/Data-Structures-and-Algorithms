def insertionSort(alist):
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentValue

    return alist


alist = [5, 3, 62, 15, 10, 6, 48, 12]
print(insertionSort(alist))
'''
时间复杂度为O(n^2)
'''
