
from Vehicle import Vehicle
from Food import Food
from Terrain import Terrain
from Bfs import Bfs
from Dijkstra import Dijkstra
from random import randint


def getNonObstacle(mat, w, h):
    pos = [randint(0, w), randint(0, h)]
    
    while mat[int(floor(pos[0]/10))][int(floor(pos[1]/10))] == 0:
        pos = [randint(0, w), randint(0, h)]
        
    return PVector(pos[0], pos[1])

def setup():
    global vehicle, food, counter, printer, terreno, currentState, path, finalPath, bfs
    size(640, 360)
    background(0)
    finalPath = []
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
    #bfs = Bfs(vehicle.position, food.getPosition(), terreno)
    bfs = Dijkstra(vehicle.position, food.getPosition(), terreno)
    #frameRate(5)
    #noLoop()
    #x = path.get()
def draw(): 
    global currentState, pathi
    global counter
    global path
    global finalPath
    terreno.render()
    fill(255)
    if currentState == 0:
        ret = bfs.djikstra_search()
        for pathi in list(bfs.frontier.queue):
            fill(170, 200, 255)
            rect(pathi.x * 10, pathi.y * 10, 10, 10)
        if bfs.frontier.empty() or ret == 1:
            path = bfs.came_from
            currentState = 1
    elif currentState == 1:    
        finalPos = PVector(floor(food.position[0]/10), floor(food.position[1]/10))
        initPos = PVector(floor(vehicle.position[0]/10), floor(vehicle.position[1]/10))
        current = path[finalPos]
        finalPath.append(finalPos * 10)
        while current != initPos and current != None:
            finalPath.append(current * 10)
            current = path[current]
        currentState = 2
    elif currentState == 2:
        for pat in finalPath:
            fill(0, 255, 255)
            rect(pat.x, pat.y, 10, 10)
        if len(finalPath) != 0:
            going = finalPath[len(finalPath)-1]
            vehicle.chase(PVector(going.x + 5, going.y + 5))
            if vehicle.position == PVector(going.x + 5, going.y + 5):
                finalPath.pop()
        vehicle.update(terreno.matrixL, terreno.tileSize)

        if food.position.dist(vehicle.position) < sqrt(50):
            food.update(getNonObstacle(terreno.matrixL, width, height))
            vehicle.velocity = PVector(0, 0)
            finalPath = []
            counter += 1
            currentState = 0
            bfs.reset(vehicle.position, food.position, terreno)
    
    vehicle.display()
    food.display()
    
