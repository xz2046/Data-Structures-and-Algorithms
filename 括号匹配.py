from Stack import Stack


def parcheCker(symbolString):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        elif symbol in ')]}':
            if s.isEmpty():
                balanced = False
            else:
                top = s.top()
                if not matches(top, symbol):
                    balanced = False
                else:
                    s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = '{[('
    closes = '}])'
    return opens.index(open) == closes.index(close)


print(parcheCker('{([(a+b)=(a+c)])}'))
print(parcheCker('[{()()(()(()))())]}'))
