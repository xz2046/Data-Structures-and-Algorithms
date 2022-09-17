class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentsize = 0

    # 和父节点比较，如果大便上浮
    def percUP(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = (
                    self.heapList[i // 2],
                    self.heapList[i],
                )
            else:
                break
            i = i // 2

    # 添加到堆末尾
    def insert(self, key):
        self.heapList.append(key)
        self.currentsize = self.currentsize + 1
        self.percUP(self.currentsize)

    def percDown(self, i):
        while i * 2 <= self.currentsize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = (
                    self.heapList[mc],
                    self.heapList[i],
                )
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # 返回堆中的最小项，最小项仍保留在堆中
    def findMin(self):
        return self.heapList[1]

    # 返回堆中的最小项，同时从堆中删除
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    # 从一个包含节点的列表里创建新堆
    def buildHaep(self, alist: list):
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while i > 0:
            print(self.heapList, i)
            self.percDown(i)
            i = i - 1
        print(self.heapList, i)

    def isEmpty(self):
        return bool(self.currentsize)

    def size(self):
        return self.currentsize


b = BinHeap()

b.insert(12)
b.insert(3)
b.insert(18)
b.insert(2)
b.insert(66)

print(b.heapList)
print(b.size())
print(b.isEmpty())
print(b.delMin())
print(b.delMin())
print(b.findMin())

'''
堆排序 时间复杂度O(nlog n)
'''
