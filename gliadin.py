import random

from aminoacid import Aminoacid
import math
import numpy as np

# Define an atom class
class Gliadin:
    def __init__(self, chain,config):
        #config = MKTFLILALL

        self.aminoacids = []
        j = 0
        angledistance = 4/math.sqrt(3)
        for i, val in enumerate(chain):
        #for i in chain:
            r=4
            #coor = (0,1*(r-1),0)
            if i%2 == 1:
                coor = (angledistance,r*j,0)
            else:
                coor = (0,r*j,0)
            self.aminoacids.append(Aminoacid(val,config[val]["abbr"],coor,config[val]["radius"]))
            j = j + 1


    def randomTranslate(self,i):
        self.aminoacids[i].translate()
        if not self.validChain():
            self.revertPosition(i)

    def revertPosition(self,i):
        self.aminoacids[i].revertPosition()

    def getAminoAcidAtPosition(self,i):
        return(self.aminoacids[i])

    def getAminoAcids(self):
        return(self.aminoacids)

    def getLength(self):
        return len(self.aminoacids)

    def getEnergy(self):
        energy = [self.aminoacids[i].getLennartJonesPotential(self.aminoacids[j]) for i in range(len(self.aminoacids)) for j in range(len(self.aminoacids)) if i != j ]
        energy = sum(energy)
        return energy

    def getPositions(self):
        return [self.aminoacids[i].getPosition() for i in range(self.getLength())]

    def _unit_vector(self,vector):
        """ Returns the unit vector of the vector.  """
        return vector / np.linalg.norm(vector)

    def getAngle(self,i,j,k):
        #coordinates are (x,y,z) tuples
        p1 = self.aminoacids[i].getPosition()
        p2 = self.aminoacids[j].getPosition()
        p3 = self.aminoacids[k].getPosition()

        v1 = (p2[0] - p1[0],p2[1]-p1[0],p2[2]-p1[2])
        v2 = (p3[0] - p2[0],p3[1]-p2[0],p3[2]-p2[2])

        v1_u = self._unit_vector(v1)
        v2_u = self._unit_vector(v2)
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))



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

        for i in range(len(self.aminoacids)):
            for j in range(i+1,len(self.aminoacids)):
                for k in range(j+1,len(self.aminoacids)):
                    if self.getAngle(i,j,k) > 2.0944:
                        result = False
                        break
        return result