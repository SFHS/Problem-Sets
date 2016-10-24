import turtle
turtle.Screen()
t = turtle.Turtle()

a = 1
b = 2
c = 1
d = 0

for n in range(0, 100):
    c = a + b
    a = b
    b = c
    print(c)
    t.left(90)
    t.forward(c)

t = turtle.pos()
(0,0)
b = 0
for a in range(0,100):
    b = b + 1
    for a in range(1,2):
        t.forward(10*b+10)
    t.left(63)
