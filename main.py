from turtle import *
import time
from ship import Ship
from blast import Blast
from invaders import Invaders


def strike():
    if not blast.isvisible():
        blast.setheading(90)
        blast.goto(x=ship.xcor(), y=-250)
        blast.showturtle()


screen = Screen()
screen.setup(width=800, height=600)
screen.register_shape('img/alien.gif')
screen.register_shape('img/ship.gif')
screen.register_shape('img/back.gif')
screen.bgpic("img/back.gif")
screen.title("SpaceInvaders")
screen.tracer(0)
ship = Ship()
aliens = Invaders()
blast = Blast()
blast.hideturtle()
screen.listen()
screen.onkeypress(fun=ship.move_left, key="Left")
screen.onkeypress(fun=ship.move_right, key="Right")
screen.onkeypress(fun=strike, key="Up")
game_is_on = True
invader_speed = 6
score = 0

while game_is_on:
    time.sleep(blast.move_speed)
    screen.update()
    blast.forward(15)
    for m in aliens.all_invaders:
        m.forward(invader_speed)

    if blast.ycor() > 280:
        blast.hideturtle()

    for j in aliens.all_invaders:
        if j.xcor() > 360 or j.xcor() < -360:
            y = j.ycor()
            y -= 80
            j.right(180)
            j.sety(y)
        if j.distance(blast) < 40:
            j.hideturtle()
            j.goto(-1000, 1000)
            score += 100
            blast.hideturtle()
            blast.goto(-1000, 1000)
        if j.distance(ship) < 45:
            you_lose = Turtle()
            you_lose.color("red")
            you_lose.up()
            you_lose.hideturtle()
            you_lose.goto(0, 0)
            you_lose.write(arg="Game is over!", align="center", font=('Distant Galaxy', 24, 'normal'))
            game_is_on = False
            time.sleep(1)
            print("Game is over start app again!")
            exit()

    if score == 3300:
        you_won = Turtle()
        you_won.color("green")
        you_won.up()
        you_won.hideturtle()
        you_won.goto(0, 0)
        game_is_on = False
        you_won.write(arg="You win!", align="center", font=('Distant Galaxy', 24, 'normal'))
        time.sleep(2)
        print("You win! Restart app if you wanna play again!")
        exit()
screen.exitonclick()
