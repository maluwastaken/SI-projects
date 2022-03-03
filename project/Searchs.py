from Queue import Queue
from Terrain import Terrain
import heapq as hq

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

class Dijkstra():
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = []
        hq.heappush(self.frontier, (0, self.initialPos))
        #self.frontier.put(self.initialPos, 0)
        self.came_from = dict()
        self.cost_so_far = dict()
        self.came_from[self.initialPos] = None
        self.cost_so_far[self.initialPos] = 0
    
    def reset(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = []
        hq.heappush(self.frontier, (0, self.initialPos))
        self.came_from = dict()
        self.cost_so_far = dict()
        self.came_from[self.initialPos] = None
        self.cost_so_far[self.initialPos] = 0
    
    def djikstra_search(self):
        current = hq.heappop(self.frontier)[1]
        if current == self.endPos:
            print(self.cost_so_far[current])
        for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
            if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                new_cost = self.cost_so_far[current] + (self.terreno.matrixCoust[int(next.x)][int(next.y)])
                if next not in self.cost_so_far or new_cost < self.cost_so_far[next]:
                    self.cost_so_far[next] = new_cost
                    priority = new_cost
                    hq.heappush(self.frontier, (priority, next))
                    #self.frontier.put(next, priority)
                    self.came_from[next] = current
        return 0
                
    

    
