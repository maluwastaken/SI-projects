from Queue import Queue
from Terrain import Terrain
class Bfs():
    
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = initialPos #PVector
        self.endPos = endPos #PVector
        self.terreno = terreno 
        
        
    def search(self):
        frontier = Queue()
        frontier.put(self.initialPos)
        came_from = dict()
        came_from[self.initialPos] = None
        while not frontier.empty():
            current = frontier.get()
            #n = 0
            if current == self.endPos:
                break
            for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
                if(self.terreno.getColor(next.x, next.y)[0]!=0):
                #next = next.mult(10)
                    if next not in came_from:
                        frontier.put(next)
                        came_from[next] = current
                    #n+=1
            came_from[self.endPos] = self.endPos.div(10)
        
        return frontier
    
