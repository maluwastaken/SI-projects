from Queue import Queue
from Terrain import Terrain
class Bfs():
    
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = Queue()
        self.frontier.put(self.initialPos)
        self.came_from = dict()
        self.came_from[self.initialPos] = None
        
    def reset(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = Queue()
        self.frontier.put(self.initialPos)
        self.came_from = dict()
        self.came_from[self.initialPos] = None
        
    def bfs_search(self):
        current = self.frontier.get()
        if current == self.endPos:
            print('aaa ', current)
            return 1
        for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
            if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                if next not in self.came_from:
                    self.frontier.put(next)
                    self.came_from[next] = current
        return 0
                
    

    
