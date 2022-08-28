from Deque import Deque


def palchecker(aString):
    d = Deque()
    for s in aString:
        d.addFront(s)

    flag = True
    while d.size() > 1 and flag:
        start = d.removeFront()
        end = d.removeRear()
        if start != end:
            flag = False

    return flag


print(palchecker('上海自来水来自海上'))
print(palchecker('apple'))
