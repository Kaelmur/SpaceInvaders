from turtle import Turtle


class Invaders:
    def __init__(self):
        self.all_invaders = []
        x_pos = range(-355, 365, 70)
        y_pos = [270, 240, 210]
        for i in range(3):
            for m in range(11):
                self.invader = Turtle()
                self.invader.color("grey")
                self.invader.shape("img/alien.gif")
                self.invader.up()
                self.invader.setheading(0)
                self.invader.shapesize(stretch_wid=1, stretch_len=2, outline=0)
                self.invader.goto(x_pos[m], y_pos[i])
                self.all_invaders.append(self.invader)






