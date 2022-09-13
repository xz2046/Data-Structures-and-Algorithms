def go_upstairs(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return go_upstairs(num - 1) + go_upstairs(num - 2)


num = input("请输入台阶数：")
try:
    num = int(num)
    steps = go_upstairs(num)
    print(steps)
except Exception as e:
    print("不是数字")
