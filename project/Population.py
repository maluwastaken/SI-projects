from Vehicle import Vehicle
from random import randrange

class Population():
    def __init__(self, initPos, target):
        self.vehicles = []
        self.initPos = initPos
        self.popsize = 10
        self.target = target
        self.matingpool = []
        
        for i in range(self.popsize):
            self.vehicles.append(Vehicle(self.initPos.copy(), PVector(0, 0)))
            
    def run(self, matrixL, count):
        for i in range(self.popsize):
            self.vehicles[i].update(matrixL, 10, count)
            self.vehicles[i].display()
            
    def evaluate(self):
        maxFit = 0
        for i in range(self.popsize):
            self.vehicles[i].calcFitness(self.target.copy())
            maxFit = max(maxFit, self.vehicles[i].fitness)
        for i in range(self.popsize):
            self.vehicles[i].fitness = float(self.vehicles[i].fitness/maxFit)
        print(maxFit)
        
        self.matingpool = []
        for i in range(self.popsize):
            n = self.vehicles[i].fitness * 100
            for j in range(int(n)):
                self.matingpool.append(self.vehicles[i].clone())
        print(len(self.matingpool))
        
    
    def selection(self):
        newVeh = []
        for i in range(len(self.vehicles)):
            parentA = self.matingpool[randrange(0, len(self.matingpool))].DNA.clone()
            parentB = self.matingpool[randrange(0, len(self.matingpool))].DNA.clone()
            
            child = parentA.crossover(parentB.clone())
            newVeh.append(Vehicle(self.initPos.copy(), dna=child.clone()))
        self.vehicles = newVeh
