
class Terrain():
    def __init__(self, width, height):
        self.tileSize = 10
        self.scl = 0.1
        self.matrixC = []
        self.matrixL = []
        self.w = width
        self.h = height
        self.start()
        
    def start(self):
        for i in range(0, self.w/self.tileSize):
            aux = []
            aux2 = []
            for j in range(0, self.h/self.tileSize):
                retUple = self.getColor(i, j)
                aux.append(retUple[0])
                aux2.append(retUple[1])
            self.matrixC.append(aux2)
            self.matrixL.append(aux)

    def render(self):
        for i in range(0, self.w/self.tileSize):
            for j in range(0, self.h/self.tileSize):
                fill(self.matrixC[i][j])
                rect(i * self.tileSize, j * self.tileSize, self.tileSize, self.tileSize)
    
    def getColor(self, i, j):
        colorMode(HSB)
        value = noise(i * self.scl, j * self.scl)
        if value < 0.3: # Water
            return (1, color(155, 255, 255))
        elif value < 0.4: # Sand
            return (1, color(30, 255, 255))
        elif value < 0.6: # Grass
            return (2, color(66, 255, 255))
        else: # Obstacle
            return (0, color(0, 0, 0))
        
    def getNeighbors(self, i, j):
        neighbors = []
        for u in range(i-1, i+2):
            for v in range(j-1, j+2):
                if(u == i and v == j):
                    continue
                elif(u < 0 or v < 0):
                    continue
                elif(u >= self.w/10 or v >= self.h/10):
                    continue
                else:
                    neighbors.append(PVector(u,v))               
        return neighbors
            
    def validPosition(self, position):
        x = int(position.x / 10)
        y = int(position.y / 10)
        
        if self.matrixL[x][y] == 0:
            return False
        
        return True

        
