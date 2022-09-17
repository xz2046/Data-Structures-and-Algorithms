def build(arr: list[int], root, end):
    while True:
        child = 2 * root + 1  # 左子节点的位置
        if child > end:  # 若左子节点超过了最后一个节点，则终止循环
            break
        if (child + 1 <= end) and (
            arr[child + 1] > arr[child]
        ):  # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
            child += 1
        if arr[child] > arr[root]:  # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
            arr[child], arr[root] = arr[root], arr[child]
            root = child
        else:
            break


def heap_sort(arr: list[int]):
    n = len(arr)
    first_root = n // 2 - 1  # 确认最深最后的那个根节点的位置
    for root in range(first_root, -1, -1):  # 由后向前遍历所有的根节点，建堆并进行调整
        build(arr, root, n - 1)

    for end in range(n - 1, 0, -1):
        # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，然后重新调整堆，将最大的元素冒到堆顶。
        arr[0], arr[end] = arr[end], arr[0]
        build(arr, 0, end - 1)
    return arr


alist = [1, 56, 89, 3, 6, 45, 66, 99, 88, 102, 32, 16]
print("排序后：", heap_sort(alist))

"""
堆排序，属于选择排序类，不稳定排序
时间复杂度O(n*logn)
"""
