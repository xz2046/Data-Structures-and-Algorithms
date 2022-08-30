import turtle


def draw(points):
    # 根据三个坐标，画一个三角形
    t.penup()
    t.goto(points['left'])
    t.pendown()
    t.goto(points['top'])
    t.goto(points['right'])
    t.goto(points['left'])


def getMid(p1, p2):
    # 获取两个坐标的中点的坐标
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(degree, points):
    draw(points)
    if degree > 0:
        # 以原三角形左边底角坐标为起点，画一个边长为原来三角形边长一半的等边三角形
        sierpinski(
            degree - 1,
            {
                'left': points['left'],
                'top': getMid(points['left'], points['top']),
                'right': getMid(points['left'], points['right']),
            },
        )

        # 以原三角形左边中点坐标为起点，画一个边长为原来三角形边长一半的等边三角形
        sierpinski(
            degree - 1,
            {
                'left': getMid(points['left'], points['top']),
                'top': points['top'],
                'right': getMid(points['top'], points['right']),
            },
        )

        # 以原三角形底边中点坐标为起点，画一个边长为原来三角形边长一半的等边三角形
        sierpinski(
            degree - 1,
            {
                'left': getMid(points['left'], points['right']),
                'top': getMid(points['top'], points['right']),
                'right': points['right'],
            },
        )


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(2)  # 画笔速度
    # 初始的三角形的三个顶点
    points = {'left': (-200, -100), 'top': (0, 200), 'right': (200, -100)}
    sierpinski(3, points)

    turtle.done()
