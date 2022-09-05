def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height - 1, withPole, fromPole, toPole)


def moveDisk(disk, fromPole, toPole):
    print(f'盘{disk} 从 {fromPole} 移动到 {toPole}')


moveTower(5, '1杆', '2杆', '3杆')

