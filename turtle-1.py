import turtle as tur

tur.color('red')
tur.penup()
tur.goto(0, -200)
tur.pendown()
tur.begin_fill()
tur.circle(200)
tur.end_fill()

def black_circle():
    tur.begin_fill()
    tur.color('black')
    tur.circle(160, -160)
    tur.end_fill()

def eye(a):
    tur.begin_fill()
    tur.goto(a * 40, 0)
    tur.color('white')
    tur.pendown()
    tur.goto(a * 140, 45)
    tur.goto(a * 120, 10)
    tur.goto(a * 40, 0)
    tur.end_fill()
    tur.penup()

tur.goto(0, -160)
tur.circle(160, -10)
black_circle()

tur.color('red')

tur.goto(25, 160)
tur.rt(20)
black_circle()

eye(1)
eye(-1)

tur.hideturtle()
tur.done()