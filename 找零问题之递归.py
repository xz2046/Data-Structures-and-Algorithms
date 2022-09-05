def recMc(valueList, change, knownResult):
    minCoins = change
    if change in valueList:
        knownResult[change] = 1
        return 1
    elif knownResult[change] > 0:
        return knownResult[change]
    else:
        for i in [ch for ch in valueList if ch <= change]:
            numCoins = 1 + recMc(valueList, change - i, knownResult)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResult[change] = minCoins
    return minCoins


# 利用表记录最优解，减少重复计算。
print(recMc([1, 5, 10, 25], 63, [0] * 64))

