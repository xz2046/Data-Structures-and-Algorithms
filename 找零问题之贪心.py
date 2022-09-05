par = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]  # 存储每种硬币，从小到大排列
sum = float(input("请输入需要找的零钱:"))
# 从面值最大的开始遍历
i = len(par) - 1
while i >= 0:
    if sum >= par[i]:
        n = int(sum // par[i])
        change = n * par[i]
        sum = float("%.6f" % (sum - change))
        print(f"用了{n}个{par[i]}元硬币")
    i -= 1
