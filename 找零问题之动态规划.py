def dpMakeChange(coinValueList, change, mincoins):
    # 从一分开始逐个计算到change的硬币数
    for cents in range(1, change + 1):
        # 初始化一个最大值
        coinCount = cents
        # 减少每个硬币，向后查最小硬币数，同时记录总的最小数
        for j in [c for c in coinValueList if c < cents]:
            if mincoins[cents - j] + 1 < coinCount:
                coinCount = mincoins[cents - j] + 1
            # 得到当前最小硬币数，记录到表中
        mincoins[cents] = coinCount

    return mincoins[change]


print(dpMakeChange([1, 5, 10, 20, 50], 63, [0] * 64))
