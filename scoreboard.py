from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def update_scorebpard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scorebpard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))