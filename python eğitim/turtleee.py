import turtle
import time
kalem=turtle.Turtle()
kalem.speed(10)
kalem.pensize(3)
class Oghan:
    def __init__(self):
        pass
    def düzcizgi(self):
        kalem.up()
        kalem.goto(0,200)
        kalem.down()
        kalem.right(90)
        kalem.forward(400)
    def harfler(self):
                
        kalem.goto(0,190)
        kalem.left(90)
        kalem.forward(10)
        kalem.backward(20)

        kalem.up()
        kalem.goto(0,170)
        kalem.down()
        kalem.right(135)
        kalem.forward(20)
        kalem.backward(40)
        kalem.up()
        kalem.goto(0,170)
        kalem.down()
        kalem.right(90)
        kalem.forward(20)
        kalem.backward(40)
        kalem.up()
        kalem.goto(0,145)
        kalem.down()
        k=0
        kalem.right(150)

        for i in range(5):
            kalem.up()
            kalem.goto(-30,140+k)
            kalem.down()
            kalem.forward(60)
            k-=10

        m=0
        kalem.left(15)

        for j in range(3):
            kalem.up()
            kalem.goto(-20,80+m)
            kalem.down()
            kalem.forward(40)
            m-=10
        p=0
        for k in range(3):
            kalem.up()
            kalem.goto(-40,50+p)
            kalem.down()
            kalem.forward(40)
            p-=10

        kalem.up()
        kalem.goto(0,0)
        kalem.down()
        kalem.right(15)
        kalem.forward(30)
        kalem.backward(60)

        kalem.left(15)
        o=0
        for j in range(3):
            kalem.up()
            kalem.goto(-20,-20+o)
            kalem.down()
            kalem.forward(40)
            o-=10
        kalem.right(15)
        ı=0
        for i in range(2):
            kalem.up()
            kalem.goto(-30,-50+ı)
            kalem.down()
            kalem.forward(60)
            ı-=10
        kalem.left(15)
        ğ=0
        for k in range(4):
            kalem.up()
            kalem.goto(-20,-90+ğ)
            kalem.down()
            kalem.forward(40)
            ğ-=10
        kalem.up()
        kalem.goto(0,-140)
        kalem.down
        kalem.forward(40)

ogham=Oghan()
ogham.düzcizgi()
ogham.harfler()