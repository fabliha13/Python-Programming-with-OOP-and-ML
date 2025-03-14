from tkinter import *
import random

#declaring constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 300
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake") #drawing the square


class Food:

    def __init__(self):
        x = random.randit(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = x = random.randit(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x, y, x+ SPACE_SIZE, y+ SPACE_SIZE, fill = FOOD_COLOR, tag = "food") #drawing the food


def next_turn(snake,food):
    x,y = snake.coordinates[0]

    direction = None ##

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x, y, x+ SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.square.insert(0,square)