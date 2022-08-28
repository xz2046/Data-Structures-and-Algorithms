from Stack import Stack


def divideBy(number, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base

    binString = ''
    while not s.isEmpty():
        binString = binString + digits[s.top()]
        s.pop()
    return binString


print(divideBy(243, 16))
print(divideBy(243, 2))
