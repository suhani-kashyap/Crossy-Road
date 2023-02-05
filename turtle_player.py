from turtle import Turtle

class TurtlePlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(0, -280)

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def go_to_start_position(self):
        self.goto(0,-280)

    def is_at_end_line(self):
        if self.ycor() > 280:
            return True
        return False