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


fpexp = '( 12 + ( 6 / ( 2 + 1 ) ) )'
n = evaluate(buildParseTree(fpexp))
print(n)
