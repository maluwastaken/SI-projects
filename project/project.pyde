from Population import Population
from Vehicle import Vehicle;
from Food import Food;
from Terrain import Terrain;
from random import randint;

global lifespan, count

def getNonObstacle(mat, w, h):
    pos = [randint(0, w/10), randint(0, h/10)]
    while mat[int(floor(pos[0]))][int(floor(pos[1]))] == 0:
        pos = [randint(0, w/10), randint(0, h/10)]
  
    return PVector(pos[0] * 10 + 5, pos[1] * 10 + 5)

def setup():
    global terreno, food, popu, initPos, count, lifespan
    lifespan = 200
    count = 0
    size(640, 360)
    background(0)
    finalPath = []
    path = {}
    currentState = -1
    terreno = Terrain(width, height)
    velocity_v = PVector(0, 0)
    velocity_f = PVector(0, 0)
    vPos = getNonObstacle(terreno.matrixL, width - 10, height - 10)
    fPos = getNonObstacle(terreno.matrixL, width - 10, height - 10)

    food = Food(fPos, velocity_f)
    initPos = getNonObstacle(terreno.matrixL, width - 10, height - 10)
    popu = Population(initPos, food.position)

    selected_option = False
    
def draw(): 
    global count
    terreno.render()
    food.display()
    popu.run(terreno.matrixL, count)
    count += 1
    if count == lifespan:
        popu.evaluate()
        popu.selection()
        count = 0
