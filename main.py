from turtle import Turtle, Screen
from turtle_player import TurtlePlayer
from cars import CarManager
from scoreboard import Scoreboard
import time

# Creating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Road")
screen.tracer(0)

turtle_player = TurtlePlayer()

screen.listen()
screen.onkey(turtle_player.go_up, "Up")
screen.onkey(turtle_player.go_down, "Down")

car_manager = CarManager()

scoreboard = Scoreboard()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            scoreboard.game_over()
            is_game_on = False


    # Detecting successful crossing
    if turtle_player.is_at_end_line():
        turtle_player.go_to_start_position()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
