tr = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}  # 集合
max_weight = 20

m = {}  # 记忆表格m


def thief(tr, w):
    # 终止条件
    if tr == set() or w == 0:
        m[(tuple(tr), w)] = 0
        return 0
    elif (tuple(tr), w) in m:
        return m[(tuple(tr), w)]
    # 递归调用
    else:
        vmax = 0
        for t in tr:
            if t[0] <= w:
                v = thief(tr - {t}, w - t[0]) + t[1]
                vmax = max(vmax, v)
        m[(tuple(tr), w)] = vmax  # 记录
        return vmax


print(thief(tr, max_weight))
