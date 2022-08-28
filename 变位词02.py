def fun(s1, s2):
    ls1 = list(s1)
    ls2 = list(s2)
    ls1.sort()
    ls2.sort()

    pos = 0
    found = True
    while pos < len(ls1) and found:
        if ls1[pos] == ls2[pos]:
            pos = pos + 1
        else:
            found = False
    return found


print(fun('python', 'thonpy'))

'''
主导步骤是排序时间。
sort（）没有返回值，不能赋值。
'''
