from Queue import Queue
from Terrain import Terrain
import heapq as hq

class BFS():
    
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = [(0, self.initialPos)]
        self.came_from = dict()
        self.came_from[self.initialPos] = None
        
    def search(self):
        current = self.frontier.pop(0)[1]
        if current == self.endPos:
            return 1
        for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
            if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                if next not in self.came_from:
                    self.frontier.append((0, next))
                    self.came_from[next] = current
        return 0
                
class DFS():
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = [(0, self.initialPos)]
        self.came_from = dict()
        self.came_from[self.initialPos] = None
    
    def search(self):
        current = self.frontier.pop(-1)[1]
        if current == self.endPos:
            return 1
        for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
            if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                if next not in self.came_from:
                    self.frontier.append((0, next))
                    self.came_from[next] = current
        return 0
    
class Dijkstra():
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = []
        hq.heappush(self.frontier, (0, self.initialPos))
        self.came_from = dict()
        self.cost_so_far = dict()
        self.came_from[self.initialPos] = None
        self.cost_so_far[self.initialPos] = 0
    
    def search(self):
        current = hq.heappop(self.frontier)[1]
        if current == self.endPos:
            return 1
        for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
            if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                new_cost = self.cost_so_far[current] + 1/float(0.5 * self.terreno.matrixL[int(next.x)][int(next.y)])
                if next not in self.cost_so_far or new_cost < self.cost_so_far[next]:
                    self.cost_so_far[next] = new_cost
                    priority = new_cost
                    hq.heappush(self.frontier, (priority, next))
                    self.came_from[next] = current
        return 0

        
class Gulosa():
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = []
        hq.heappush(self.frontier, (0, self.initialPos))
        self.came_from = dict()
        self.came_from[self.initialPos] = None

    def heuristic(self,ax,ay,bx,by):
        return abs(ax - bx) + abs(ay - by)  
    
    def search(self):
        current = hq.heappop(self.frontier)[1]
        if current == self.endPos:
            return 1
        for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
            if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                if next not in self.came_from:
                    priority = self.heuristic(self.endPos[0], self.endPos[1], next[0], next[1])
                    hq.heappush(self.frontier, (priority, next))
                    self.came_from[next] = current
        return 0


class A():
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        self.frontier = []
        hq.heappush(self.frontier, (0, self.initialPos))
        self.came_from = dict()
        self.cost_so_far = dict()
        self.came_from[self.initialPos] = None
        self.cost_so_far[self.initialPos] = 0
        
    def heuristic(self,ax,ay,bx,by):
        return abs(ax - bx) + abs(ay - by)
    
    def search(self):
        current = hq.heappop(self.frontier)[1]
        if current == self.endPos:
            return 1
        for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
            if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                new_cost = self.cost_so_far[current] + 1/float(self.terreno.matrixL[int(next.x)][int(next.y)])
                if next not in self.cost_so_far or new_cost < self.cost_so_far[next]:
                    self.cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(self.endPos[0], self.endPos[1], next[0], next[1])
                    hq.heappush(self.frontier, (priority, next))
                    self.came_from[next] = current
        return 0
    
