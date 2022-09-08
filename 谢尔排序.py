def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startpatition in range(sublistcount):
            getInsertionSort(alist, startpatition, sublistcount)
        print(f'序列间隔为{sublistcount},序列为{alist}')
        sublistcount = sublistcount // 2


def getInsertionSort(alist, start, gap):
    for index in range(start + gap, len(alist), gap):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentValue


alist = [18, 56, 32, 4, 88, 23, 66, 12, 7, 31]
shellSort(alist)
'''
时间复杂度在O(n)到O(n^2)之间
'''
