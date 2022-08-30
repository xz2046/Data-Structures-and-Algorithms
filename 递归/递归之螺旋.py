import turtle


def drawSpirla(t, linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawSpirla(t, linelen - 5)


t = turtle.Turtle()
drawSpirla(t, 100)
turtle.done()
