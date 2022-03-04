
from Vehicle import Vehicle;
from Food import Food;
from Terrain import Terrain;
from Searchs import BFS, DFS, Dijkstra, Gulosa, A;
from random import randint;

def getNonObstacle(mat, w, h):
    pos = [randint(0, w/10), randint(0, h/10)]
    while mat[int(floor(pos[0]))][int(floor(pos[1]))] == 0:
        pos = [randint(0, w/10), randint(0, h/10)]
  
    return PVector(pos[0] * 10 + 5, pos[1] * 10 + 5)

def reset():
    global vehicle, food
    velocity_v = PVector(0, 0)
    velocity_f = PVector(0, 0)
    vPos = getNonObstacle(terreno.matrixL, width-10, height-10)
    fPos = getNonObstacle(terreno.matrixL, width-10, height-10)
    
    vehicle.reset(vPos, velocity_v)
    food.reset(fPos, velocity_f)

def setup():
    global vehicle, food, counter, printer, printer2, terreno, currentState, path, finalPath, search, selected_option, search_method
    size(640, 360)
    background(0)
    finalPath = []
    path = {}
    currentState = -1
    terreno = Terrain(width, height)
    counter = 0
    printer = createFont("Arial Black", 18, True)
    printer2 = createFont("Arial Black", 11, True)
    velocity_v = PVector(0, 0)
    velocity_f = PVector(0, 0)
    vPos = getNonObstacle(terreno.matrixL, width-10, height-10)
    fPos = getNonObstacle(terreno.matrixL, width-10, height-10)
    vehicle = Vehicle(vPos, velocity_v)
    food = Food(fPos, velocity_f)
    selected_option = False
    
def draw(): 
    global currentState, pathi
    global counter
    global path
    global finalPath
    global selected_option
    global search_method
    global search
    global visited
    
    if(keyPressed and key == '0' and selected_option == True):
        selected_option = False
    if(keyPressed and key != '0'):
        if(key == '1'):
            search_method = BFS
        elif(key == '2'):
            search_method = DFS
        elif(key == '3'):
            search_method = Dijkstra
        elif(key == '4'):
            search_method = Gulosa
        elif(key == '5'):
            search_method = A
       
    if selected_option == False:
        draw_menu()
        currentState = -1
        finalPath = []
        path = {}
        counter = 0    
    else:
        terreno.render()
        fill(255)
        if currentState == -1:
            search = search_method(vehicle.getPosition(), food.getPosition(), terreno)
            currentState = 0
            visited = set()
        elif currentState == 0:
            for pathi in list(search.frontier):
                fill(0, 255, 255)
                rect(pathi[1].x * 10, pathi[1].y * 10, 10, 10)
                visited.add(pathi)
            for pathi in list(visited):
                fill(0, 255, 255, 100)
                rect(pathi[1].x * 10, pathi[1].y * 10, 10, 10)
            ret = search.search()
            if search.frontier == [] or ret == 1:
                path = search.came_from
                currentState = 1
        elif currentState == 1:    
            finalPos = PVector(floor(food.position[0]/10), floor(food.position[1]/10))
            initPos = PVector(floor(vehicle.position[0]/10), floor(vehicle.position[1]/10))
            try:
                current = path[finalPos]
                finalPath.append(finalPos * 10)
                while current != initPos and current != None:
                    finalPath.append(current * 10)
                    current = path[current]
                    currentState = 2
            except:
                food.update(getNonObstacle(terreno.matrixL, width-10, height-10))
                vPos = getNonObstacle(terreno.matrixL, width-10, height-10)
                vehicle.velocity = PVector(0, 0)
                finalPath = []
                counter += 1
                currentState = -1
                vehicle.setPosition(vPos)
                
        elif currentState == 2:
            for pat in finalPath:
                fill(0, 255, 255)
                rect(pat.x, pat.y, 10, 10)
            if len(finalPath) != 0:
                going = finalPath[-1]
                vehicle.chase(PVector(going.x + 5, going.y + 5))
                if vehicle.position == PVector(going.x + 5, going.y + 5):
                    finalPath.pop()
            
            if food.position.dist(vehicle.position) < sqrt(50):
                food.update(getNonObstacle(terreno.matrixL, width-10, height-10))
                vehicle.velocity = PVector(0, 0)
                finalPath = []
                counter += 1
                currentState = -1
                
            vehicle.update(terreno.matrixL, terreno.tileSize)
        vehicle.display()
        food.display()
        textFont(printer)
        fill(149, 85, 232)
        text("Comidas comidas: " + str(counter), 10, 20)
        text("Aperte 0 para voltar", 440, 350)
        textFont(printer2)
        text("1-Largura, 2-Profundidade, 3-Uniforme, 4-Guloso, 5-A*", 0, 350)
        
        

def draw_menu():
    global selected_option
    global search_method
    global vehicle
    global food
    global terreno
    
    img = loadImage("menu.png")
    image(img, 0,0)
    
    if(keyPressed):
        if(key == '1'):
            reset()
            search_method = BFS
            selected_option = True
        elif(key == '2'):
            reset()
            search_method = DFS
            selected_option = True
        elif(key == '3'):
            reset()
            search_method = Dijkstra
            selected_option = True
        elif(key == '4'):
            reset()
            search_method = Gulosa
            selected_option = True
        elif(key == '5'):
            reset()
            search_method = A
            selected_option = True
        
