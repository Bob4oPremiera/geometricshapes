import turtle as t
def square():
    print("Please write to console size sides (at pixels):")
    side = int(input())
    for i in range(4):
        t.forward(side)
        t.right(90)
def triangle():
    print("Please write to console size sides (at pixels):")
    side = int(input())
    t.forward(side)
    for i in range(2):
        t.left(120)
        t.forward(side)
def rectangle():
    print("Please write to console size sides (at pixels):")
    side = int(input())
    side_ = int(input())
    t.forward(side)
    t.right(90)
def rhombussquare(): #sorry, i dont know how i can create rhombus :)
    print("Please write to console size sides (at pixels):")
    side = int(input())
    t.left(45)
    for i in range(4):
        t.forward(side)
        t.left(90)
def circle():
    print("Please write to console size for circle (at pixels):")
    size = int(input())
    t.circle(size)
def spiralsquares():
    size=int(input())
    while (True):
        t.forward(size)
        t.right(91)
        size = size + 1
def yellowstar():
    t.pen(pencolor='red', fillcolor='yellow')
    t.fill(True)
    while True:
        t.forward(200)
        t.left(170)
        if abs(turtle.pos()) < 1:
            break
    t.fill(False)
t.done()
t.hideturtle()
t.screensize(100,100)
