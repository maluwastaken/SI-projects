from Queue import Queue
from Terrain import Terrain
class Bfs():
    
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector(int(floor(initialPos.x/10)), int(floor(initialPos.y/10))) #PVector
        self.endPos = PVector(int(floor(endPos.x/10)), int(floor(endPos.y/10))) #PVector
        self.terreno = terreno 
        
        
    def search(self):
        frontier = Queue()
        frontier.put(self.initialPos)
        came_from = dict()
        came_from[self.initialPos] = None
        while not frontier.empty():
            current = frontier.get()
            if current == self.endPos:
                print(current)
                break
            for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
                if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                    if next not in came_from:
                        frontier.put(next)
                        came_from[next] = current
                        
            for path in list(frontier.queue):
                fill(0, 255, 255, 0.5)
                rect(path.x * 10, path.y * 10, 10, 10)
        
        return came_from
    
