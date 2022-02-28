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


def getNonObstacle(mat, w, h):
    pos = [randint(0, w), randint(0, h)]
    
    while mat[int(pos[0]/10)][int(pos[1]/10)] == 0:
        pos = [randint(0, w), randint(0, h)]
        
    return PVector(pos[0], pos[1])

def setup():
    global vehicle, food, counter, printer, terreno, currentState, path, pathi
    size(640, 360)
    background(0)
    pathi = []
    path = {}
    currentState = 0
    terreno = Terrain(width, height)
    counter = 0
    printer = createFont("Arial", 72, True)
    velocity_v = PVector(0, 0)
    velocity_f = PVector(0, 0)
    vPos = getNonObstacle(terreno.matrixL, width, height)
    fPos = getNonObstacle(terreno.matrixL, width, height)
    vehicle = Vehicle(vPos, velocity_v)
    food = Food(fPos, velocity_f)
    #noLoop()
    #x = path.get()
def draw(): 
    global currentState, pathi
    global counter
    global path
    global pathi
    terreno.render()
    fill(255)
    if currentState == 0:
        bfs = Bfs(vehicle.position, food.getPosition(), terreno)
        path = bfs.search()
        currentState = 1
        print('a')
    elif currentState == 1:    
        finalPos = PVector(round(food.position[0]/10), round(food.position[1]/10))
        initPos = PVector(round(vehicle.position[0]/10), round(vehicle.position[1]/10))
        #try:
        current = path[finalPos]
        #except:
        #    pass
        while current != initPos and current != None:
            print(food.position, vehicle.position)
            pathi.append(current * 10)
            current = path[current]
        currentState = 2
    elif currentState == 2:
        for pat in pathi:
            fill(0, 255, 255)
            rect(pat.x, pat.y, 10, 10)
        if len(pathi) != 0:
            going = pathi[len(pathi)-1]
            vehicle.chase(PVector(going.x + 5, going.y + 5))
            if vehicle.position.dist(going) < 10:
                pathi.pop()
            
        if food.position.dist(vehicle.position) < 10:
            food.update(getNonObstacle(terreno.matrixL, width, height))
            vehicle.velocity = PVector(0, 0)
            counter += 1
            currentState = 0
        print('c')
    
    
    
    vehicle.update(terreno.matrixL, terreno.tileSize)
    vehicle.display()
    food.display()
    
