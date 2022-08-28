#比较字符串字母是否相等
def fun(s1, s2):
    ls2 = list(s2)
    pos1 = 0
    stillok = True
    while pos1 < len(s1) and stillok:
        pos2 = 0
        found = False
        while pos2 < len(ls2) and not found:
            if s1[pos1] == ls2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            ls2[pos2] = None
        else:
            stillok = False
        pos1 = pos1 + 1
    return stillok


print(fun('python', 'thonpy'))

'''
两个循环，时间复杂度为O(n^2)
'''
