from turtle import *

t = Turtle()
t.speed(5)
t.screen.setup(1200, 800)

def sq_cr(side):
    for i in range(1):
        t.circle(side / 3, 360)
        t.left(180)
        t.circle(side / 2, 360)
        t.fd(300)
        t.bk(600)
        t.left(90)
        t.fd(300)
        t.bk(500)
        t.right(150)
        t.fd(150)
        t.bk(150)
        t.right(10)
        t.fd(150)
        t.bk(150)
        t.right(10)
        t.fd(150)
        t.bk(150)
        t.right(10)
        t.fd(150)
        t.bk(150)
        t.right(10)
        t.fd(150)
        t.bk(150)
        t.right(10)
        t.fd(150)
        t.bk(150)
        t.right(10)
        t.fd(150)
        t.bk(150)
        t.right(10)
        t.fd(150)
        t.bk(150)
        t.right(230)
        t.up()
        t.fd(200)
        t.down()
        t.begin_fill()
        t.fd(200)
        t.right(110)
        t.fd(150)
        t.right(70)
        t.fd(100)
        t.right(70)
        t.fd(150)
        t.end_fill()
        t.up()
        t.right(70)
        t.fd(70)
        t.down()
        t.fillcolor("red")
        t.begin_fill()
        t.circle(side / 6, 360)
        t.end_fill() 
        t.up()
        t.left(80)
        t.fd(60)
        t.down()
        t.fillcolor("black")
        t.begin_fill()
        t.circle(side / 15, 360)
        t.end_fill()
        t.up()
        t.right(140)
        t.fd(150)
        t.down()
        t.fillcolor("red")
        t.begin_fill()
        t.circle(side / 6, 360)
        t.end_fill() 
        t.up()
        t.left(80)
        t.fd(60)
        t.down()
        t.fillcolor("black")
        t.begin_fill()
        t.circle(side / 15, 360)
        t.end_fill()

        


sq_cr(350)


t.screen.exitonclick()
t.screen.mainloop()