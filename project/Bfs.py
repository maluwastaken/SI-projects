from Queue import Queue
from Terrain import Terrain
class Bfs():
    
    def __init__(self, initialPos, endPos, terreno):
        self.initialPos = PVector.div(initialPos, 10) #PVector
        self.endPos = PVector.div(endPos, 10) #PVector
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
                print('aaa')
                break
            for next in self.terreno.getNeighbors(int(current.x), int(current.y)):
                if(self.terreno.matrixL[int(next.x)][int(next.y)]!=0):
                #next = next.mult(10)
                    if next not in came_from:
                        frontier.put(next)
                        came_from[next] = current
                    #n+=1
            for path in list(frontier.queue):
                fill(0, 255, 255, 0.5)
                rect(path.x * 10, path.y * 10, 10, 10)
            #came_from[self.endPos] = self.endPos.div(10)
        
        return came_from
    
