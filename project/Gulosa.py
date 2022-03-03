from Queue import PriorityQueue
from Terrain import Terrain

class Gulosa():
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = PriorityQueue()
        self.frontier.put(self.initialPos, 0)
        self.came_from = dict()
        self.came_from[self.initialPos] = None
    
    def reset(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = PriorityQueue()
        self.frontier.put(self.initialPos, 0)
        self.came_from = dict()
        self.came_from[self.initialPos] = None
        
    def heuristic(self,ax,ay,bx,by):
        print(ax,ay,bx,by)
        return abs(ax - bx) + abs(ay - by)  
    
    def search(self):
        current = self.frontier.get()
        if current == self.endPos:
            return 1
        for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
            if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                if next not in self.came_from:
                    priority = self.heuristic(self.endPos[0], self.endPos[1], next[0], next[1])
                    self.frontier.put(next, priority)
                    self.came_from[next] = current
        return 0
