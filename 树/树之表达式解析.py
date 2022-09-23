import operator

from Stack import Stack
from 树之链表实现 import BinaryTree


def buildParseTree(fpexp: str):
    fplist = fpexp.split(' ')
    print(fplist)
    pstack = Stack()
    etree = BinaryTree('')
    pstack.push(etree)
    curentTree = etree
    for f in fplist:
        if f == '(':
            curentTree.insertLeft('')
            pstack.push(curentTree)
            curentTree = curentTree.getLeftChild()
        elif f not in ['+', '-', '*', '/', ')']:
            curentTree.setRootVal(int(f))
            curentTree = pstack.pop()
        elif f in ['+', '-', '*', '/']:
            curentTree.setRootVal(f)
            curentTree.insertRight('')
            pstack.push(curentTree)
            curentTree = curentTree.getRightChild()
        elif f == ')':
            curentTree = pstack.pop()
        else:
            raise ValueError

    return etree


# 求值
def evaluate(tree: BinaryTree):
    opers = {
        '+': operator.add,
        '*': operator.mul,
        '-': operator.sub,
        '/': operator.truediv,
    }

    leftroot = tree.getLeftChild()
    rightroot = tree.getRightChild()
    if leftroot and rightroot:
        fn = opers[tree.getRootVal()]
        return fn(evaluate(leftroot), evaluate(rightroot))
    else:
        return tree.getRootVal()


# 后序遍历优化求值
def postordereval(tree: BinaryTree):
    opers = {
        '+': operator.add,
        '*': operator.mul,
        '-': operator.sub,
        '/': operator.truediv,
    }

    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


# 中序遍历生成全括号表达式
def printexp(tree: BinaryTree):
    sVal = ''
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal


fpexp = '( 12 + ( 6 / ( 2 + 1 ) ) )'
tree = buildParseTree(fpexp)
n1 = evaluate(tree)
n2 = postordereval(tree)
print(n1)
print(n2)
print(printexp(tree))
