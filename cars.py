from turtle import Turtle
import random

COLORS = ['red', 'green', 'yellow', 'blue', 'orange', 'purple']

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)

    def level_up(self):
        self.car_speed += 5
