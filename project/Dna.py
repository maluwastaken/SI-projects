from random import randrange, uniform

class DNA():
    def __init__(self, g = []):
        if g == []:
            self.genes = []
            for i in range(500):
                self.genes.append(PVector(float(uniform(-1, 1)), float(uniform(-1, 1))))
                self.genes[i].setMag(0.1)
        else:
            self.genes = g
            
    def crossover(self, partner):
        newDna = []
        mid = randrange(len(self.genes))
        for i in range(500):
            if i > mid:
                newDna.append(self.genes[i].copy())
            else:
                newDna.append(partner.genes[i].copy())
        return DNA(newDna)
            
    def clone(self):
        return DNA(g = self.genes)        
    
