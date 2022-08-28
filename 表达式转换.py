from Stack import Stack

# 中缀表达式转后缀表达式
def infixToPostfix(infixexpr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    s = Stack()
    postfixList = []
    tokenList = infixexpr.split(' ')
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            topToken = s.top()
            s.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = s.top()
                s.pop()
        else:
            while (not s.isEmpty()) and prec[s.top()] >= prec[token]:
                postfixList.append(s.top())
                s.pop()
            else:
                s.push(token)
    while not s.isEmpty():
        postfixList.append(s.top())
        s.pop()
    return ' '.join(postfixList)


# 后缀表达式求值
def postfixEval(postfixEvar):
    s = Stack()
    tokenList = postfixEvar.split(' ')
    for token in tokenList:
        if token in '0123456789':
            s.push(int(token))
        else:
            oper2 = s.top()
            s.pop()
            oper1 = s.top()
            s.pop()
            result = doMath(token, oper1, oper2)
            s.push(result)
    return result


def doMath(op, oper1, oper2):
    if op == '*':
        return oper1 * oper2
    elif op == "/":
        return oper1 / oper2
    elif op == "+":
        return oper1 + oper2
    else:
        return oper1 - oper2


result1 = infixToPostfix('( 9 + 1 ) * ( 5 - 3 )')
print(result1)
result2 = postfixEval(result1)
print(result2)
