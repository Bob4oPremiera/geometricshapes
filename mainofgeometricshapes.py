import turtle as t
def square():
    print("Please write to console size sides (at pixels):")
    side = input()
    for i in range(4):
        t.forward(side)
        t.right(90)
def triangle():
    print("Please write to console size sides (at pixels):")
    side = input()
    for i in range(3):
        t.forward(side)
        t.right(60)
def rectangle():
    print("Please write to console size sides (at pixels):")
    side = input()
    side_ = input()
    t.forward(side)
    t.right(90)

t.hideturtle()
t.done()
t.screensize(100,100)
