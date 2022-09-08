def mergeSort(alist):
    if len(alist) <= 1:
        return alist

    middle = len(alist) // 2
    left = mergeSort(alist[:middle])
    right = mergeSort(alist[middle:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)

    return merged


alist = [18, 56, 32, 4, 88, 23, 66, 12, 7, 31]
print(mergeSort(alist))
'''
时间复杂度为:O(nlog n)
会使用额外一倍的存储空间，在面对大数据集时，需要考虑空间问题
'''
