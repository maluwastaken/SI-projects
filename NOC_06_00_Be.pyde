# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food
from random import randint

def setup():
    global vehicle, food, counter
    counter = 0
    size(640, 360)
    velocity_v = PVector(randint(0, 1), randint(0,1))
    velocity_f = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity_v)
    food = Food(randint(0, width), randint(0, height), velocity_f)

def draw():
    background(253)
    global counter
    mouse = PVector(mouseX, mouseY)
    food.update(food.position)
    if food.position == vehicle.position:
        food.update(PVector(randint(0, width), randint(0, height)))
        counter += 1
        print("Bites eaten: " + str(counter))
    food.display()
    vehicle.chase(food)
    vehicle.update()
    vehicle.display()
    
