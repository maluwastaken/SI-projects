
from Vehicle import Vehicle
from Food import Food
from Terrain import Terrain
from Bfs import Bfs
from Dijkstra import Dijkstra
from A import A
from Gulosa import Gulosa
from random import randint


def getNonObstacle(mat, w, h):
    pos = [randint(0, w), randint(0, h)]
    
    while mat[int(floor(pos[0]/10))][int(floor(pos[1]/10))] == 0:
        pos = [randint(0, w), randint(0, h)]
        
    return PVector(pos[0], pos[1])

def reset():
    global vehicle, food, search_method
    velocity_v = PVector(0, 0)
    velocity_f = PVector(0, 0)
    vPos = getNonObstacle(terreno.matrixL, width-10, height-10)
    fPos = getNonObstacle(terreno.matrixL, width-10, height-10)
    
    vehicle.reset(vPos, velocity_v)
    food.reset(fPos, velocity_f)

def setup():
    global vehicle, food, counter, printer, terreno, currentState, path, finalPath, search_method, selected_option
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
    #bfs = Dijkstra(vehicle.position, food.getPosition(), terreno)
    selected_option = False
    #frameRate(5)
    #noLoop()
    #x = path.get()
    
def draw(): 
    global currentState, pathi
    global counter
    global path
    global finalPath
    global selected_option

    if(keyPressed and key == '0' and selected_option == True):
        selected_option = False
        
    if selected_option == False:
        draw_menu()
        currentState = 0
        finalPath = []
        path = {}
        counter = 0    
    else:
        terreno.render()
        fill(255)
        if currentState == 0:
            ret = search_method.search()
            #print(bfs.frontier.queue)
            for pathi in list(search_method.frontier.queue):
                fill(170, 200, 255)
                rect(pathi.x * 10, pathi.y * 10, 10, 10)
            if search_method.frontier.empty() or ret == 1:
                path = search_method.came_from
                currentState = 1
        elif currentState == 1:
            foodPos = food.getPosition()
            vehiclePos = vehicle.getPosition()
            finalPos = PVector(floor(foodPos[0]/10), floor(foodPos[1]/10))
            initPos = PVector(floor(vehiclePos[0]/10), floor(vehiclePos[1]/10))
            #print(finalPos)
            current = path[finalPos]
            #print(current, ' olha eu aquiii')
            finalPath.append(finalPos * 10)
            while current != initPos and current != None:
                finalPath.append(current * 10)
                current = path[current]
            currentState = 2
            #print(finalPath)
                #print('remake')
                #food.update(getNonObstacle(terreno.matrixL, width, height))
                #bfs.reset(vehicle.position, food.position, terreno)
                #currentState = 0
        elif currentState == 2:
            for pat in finalPath:
                fill(0, 255, 255)
                rect(pat.x, pat.y, 10, 10)
            if len(finalPath) != 0:
                going = finalPath[len(finalPath)-1]
                vehicle.chase(PVector(going.x + 5, going.y + 5))
                if vehicle.getPosition() == PVector(going.x + 5, going.y + 5):
                    finalPath.pop()
            vehicle.update(terreno.matrixL, terreno.tileSize)
    
            if food.position.dist(vehicle.position) < sqrt(50):
                food.update(getNonObstacle(terreno.matrixL, width, height))
                vehicle.velocity = PVector(0, 0)
                finalPath = []
                counter += 1
                currentState = 0
                search_method.reset(vehicle.getPosition(), food.getPosition(), terreno)
            #print('c')
        
        vehicle.display()
        food.display()

def draw_menu():
    global selected_option
    global search_method
    global vehicle
    global food
    global terreno
    colorMode(RGB, 255);
    background(0)
    fill(255)
    rect(640, 360,0,0)
    textSize(24)
    fill(0, 255, 0)
    text('Projeto de SI - Metodos de busca', width/5, 40)
    textSize(16)
    fill(0, 230, 0)
    text('Selecione qual o algoritmo de busca voce deseja utilizar', 40, 140)
    textSize(12)
    text('1 - Largura', 40, 180)
    text('2 - Profundidade', 40, 200)
    text('3 - Custo Uniforme', 40, 220)
    text('4 - Gulosa', 40, 240)
    text('5 - A*', 40, 260)
    
    if(keyPressed):
        if(key == '1'):
            reset()
            search_method = Bfs(vehicle.getPosition(), food.getPosition(), terreno)
            search_method.reset(vehicle.getPosition(), food.getPosition(), terreno)
            selected_option = True
        elif(key == '2'):
            print(4)
        elif(key == '3'):
            reset()
            search_method = Dijkstra(vehicle.getPosition(), food.getPosition(), terreno)
            search_method.reset(vehicle.getPosition(), food.getPosition(), terreno)
            selected_option = True
        elif(key == '4'):
            reset()
            search_method = Gulosa(vehicle.getPosition(), food.getPosition(), terreno)
            search_method.reset(vehicle.getPosition(), food.getPosition(), terreno)
            selected_option = True
        elif(key == '5'):
            reset()
            search_method = A(vehicle.getPosition(), food.getPosition(), terreno)
            search_method.reset(vehicle.getPosition(), food.getPosition(), terreno)
            selected_option = True
        
