# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food
from Terrain import Terrain
from Bfs import Bfs
from random import randint

def setup():
    global vehicle, food, counter, printer, terreno, bfs, x, path
    size(640, 360)
    terreno = Terrain(width, height) 
    counter = 0
    printer = createFont("Arial", 72, True)
    velocity_v = PVector(0, 0)
    velocity_f = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity_v)
    food = Food(randint(0, width), randint(0, height), velocity_f)
    bfs = Bfs(vehicle.position, food.getPosition(), terreno)
    path = bfs.search()
    x = path.get()
def draw(): 
    global counter
    global x
    global path
    food.update(food.position)
    if food.position == vehicle.position:
        food.update(PVector(randint(0, width), randint(0, height)))
        counter += 1
        bfs = Bfs(vehicle.position, food.getPosition(), terreno)
        path = bfs.search()
        x = path.get()
    fill(255)
    terreno.render()
    for i in range(path.qsize()):
        print(path[i])
    #try:
    if(vehicle.position == x):
        x = path.get()
    else:
        vehicle.chase(x)
    #except:
        #x+=1
    vehicle.update(terreno.matrixL, terreno.tileSize)
    vehicle.display()
    food.display()
    
