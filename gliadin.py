import random

from aminoacid import Aminoacid
import math

# Define an atom class
class Gliadin:
    def __init__(self, chain,config):
        #config = MKTFLILALL

        self.aminoacids = []
        j = 0
        for i in chain:
            r=4
            #coor = (0,1*(r-1),0)
            coor = (0,r*j,0)
            self.aminoacids.append(Aminoacid(i,coor,config[i]["radius"]))
            j = j + 1


    def randomTranslate(self,i):
        self.aminoacids[i].translate()
        if not self.validChain():
            self.revertPosition(i)


    def revertPosition(self,i):
        self.aminoacids[i].revertPosition()

    def getAminoAcidAtPosition(self,i):
        return(self.aminoacids[i])

    def getLength(self):
        return len(self.aminoacids)

    def getEnergy(self):
        energy = [self.aminoacids[i].getLennartJonesPotential(self.aminoacids[j]) for i in range(len(self.aminoacids)) for j in range(len(self.aminoacids)) if i != j ]
        energy = sum(energy)
        return energy

    def getPositions(self):
        return [self.aminoacids[i].getPosition() for i in range(self.getLength())]

    def validChain(self):
        result = True
        for i in range(len(self.aminoacids)):
            for j in range(len(self.aminoacids)):
                if i != j:
                    coor1 = self.aminoacids[i].getPosition()
                    coor2 = self.aminoacids[j].getPosition()
                    radius1 = self.aminoacids[i].getRadius()
                    radius2 = self.aminoacids[j].getRadius()
                    dist = math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2 + (coor1[2] - coor2[2])**2)
                    if dist < radius1 + radius2:
                        result = False
                        break
        return result