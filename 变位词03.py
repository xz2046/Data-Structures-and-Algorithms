def fun(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillok = True
    while j < 26 and stillok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillok = False
    return stillok


def fun2(s1, s2):
    d1 = {}
    d2 = {}
    for key in list(s1):
        d1[key] = d1.get(key, 0) + 1
    for key in list(s2):
        d2[key] = d2.get(key, 0) + 1

    stillok = True if d1 == d2 else False
    return stillok


print(fun('python', 'thonpy'))
print(fun2('apple', 'pplae'))

'''
T(n) = 2n+26
总的时间复杂度为O（n）
通过两个计数器来存储次数换取计算便捷
牺牲存储空间来换取时间
'''

