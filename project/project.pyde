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
    
    while mat[int(floor(pos[0]/10))][int(floor(pos[1]/10))] == 0:
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
    vPos = getNonObstacle(terreno.matrixL, width-10, height-10)
    fPos = getNonObstacle(terreno.matrixL, width-10, height-10)
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
        finalPos = PVector(floor(food.position[0]/10), floor(food.position[1]/10))
        initPos = PVector(floor(vehicle.position[0]/10), floor(vehicle.position[1]/10))
        try:
            current = path[finalPos]
            while current != initPos and current != None:
                #print(food.position, vehicle.position)
                pathi.append(current * 10)
                current = path[current]
            currentState = 2
        except:
            print(finalPos)
            currentState=2
    elif currentState == 2:
        for pat in pathi:
            fill(0, 255, 255)
            rect(pat.x, pat.y, 10, 10)
        if len(pathi) != 0:
            going = pathi[len(pathi)-1]
            vehicle.chase(PVector(going.x + 5, going.y + 5))
            #print(vehicle.position.dist(going))
            if vehicle.position == PVector(going.x+5, going.y + 5):
                pathi.pop()
            
        if food.position.dist(vehicle.position) < sqrt(50):
            food.update(getNonObstacle(terreno.matrixL, width, height))
            vehicle.velocity = PVector(0, 0)
            counter += 1
            currentState = 0
        #print('c')
    
    
    
    vehicle.update(terreno.matrixL, terreno.tileSize)
    vehicle.display()
    food.display()
    
