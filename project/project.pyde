# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food
from Terrain import Terrain
from random import randint

def setup():
    global vehicle, food, counter, printer, terreno
    size(640, 360)
    terreno = Terrain(width, height) 
    counter = 0
    printer = createFont("Arial", 72, True)
    velocity_v = PVector(1, 0)
    velocity_f = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity_v)
    food = Food(randint(0, width), randint(0, height), velocity_f)

    
def draw(): 
    global counter
    food.update(food.position)
    if food.position == vehicle.position:
        food.update(PVector(randint(0, width), randint(0, height)))
        counter += 1
    fill(255)
    terreno.render()
    vehicle.chase(food)
    vehicle.update(terreno.matrixL, terreno.tileSize)
    vehicle.display()
    food.display()
    
