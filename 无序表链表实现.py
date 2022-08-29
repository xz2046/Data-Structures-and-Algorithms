# 节点Node
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


# 无序表
class UnorderedList:
    def __init__(self):
        self.head = None

    def IsEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()

        current.setNext(temp)

    def index(self, item):
        current = self.head
        count = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count = count + 1
        return self.length() - 1 - count

    def insert(self, pos, item):
        pos = self.length() - pos
        current = self.head
        count = 0
        temp = Node(item)
        previous = None
        while count != pos:
            previous = current
            current = current.getNext()
            count = count + 1

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def printAll(self):
        current = self.head
        alist = ''
        while current != None:
            alist = str(current.getData()) + ' ' + alist
            current = current.getNext()
        print('[' + alist + ']')

    def pop(self, pos=0):
        current = self.head
        count = 0
        previous = None
        while count != pos:
            previous = current
            current = current.getNext()
            count = count + 1

        data = current.getData()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return data


myList = UnorderedList()
print(myList.IsEmpty())
myList.add(0)
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
print(myList.length())
myList.printAll()
print(myList.search(2))
print(myList.index(4))
myList.insert(5, 100)
print(myList.index(100))
myList.insert(0, 66)
myList.printAll()
print(myList.length())
myList.add(20)
myList.printAll()
print(myList.pop())
myList.printAll()
print(myList.pop(5))
myList.printAll()
