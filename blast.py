from turtle import Turtle


class Blast(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=1)
        self.up()
        self.y_move = 10
        self.move_speed = 0.025

