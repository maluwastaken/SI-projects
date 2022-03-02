from Queue import PriorityQueue
from Terrain import Terrain

class Dijkstra():
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = PriorityQueue()
        self.frontier.put(self.initialPos, 0)
        self.came_from = dict()
        self.cost_so_far = dict()
        self.came_from[self.initialPos] = None
        self.cost_so_far[self.initialPos] = 0
    
    def reset(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = PriorityQueue()
        self.frontier.put(self.initialPos, 0)
        self.came_from = dict()
        self.cost_so_far = dict()
        self.came_from[self.initialPos] = None
        self.cost_so_far[self.initialPos] = 0
    
    def djikstra_search(self):
        while not self.frontier.empty():
            current = self.frontier.get()
            #if current == self.endPos:
                #break
            for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
                if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                    new_cost = self.cost_so_far[current] + (self.terreno.matrixCoust[int(next.x)][int(next.y)])
                    if next not in self.cost_so_far or new_cost < self.cost_so_far[next]:
                        self.cost_so_far[next] = new_cost
                        priority = new_cost
                        self.frontier.put(next, priority)
                        self.came_from[next] = current
        return self.came_from
