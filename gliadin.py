import random

from aminoacid import Aminoacid
from atom import Atom
import math
import numpy as np

# Define an atom class
class Gliadin:
    def __init__(self, sequence):
        self.atoms = []
        initialCoor = coor = (0,0,0)
        j=0
        for i in sequence:
            if j == 0:
                newAtom = Atom(initialCoor, 0.3)
                self.addAtom(newAtom)
            else:
                if j%2 == 1:
                    coor = (j*1.299,-0.75,0)
                else:
                    coor = (j * 1.299, 0 , 0)
                newAtom = Atom(coor, 0.3)
                self.addAtom(newAtom)
            j = j+1

        #config = MKTFLILALL

        #self.aminoacids = []
        #j = 0
        #angledistance = 4/math.sqrt(3)
        #for i, val in enumerate(chain):
        #for i in chain:
        #    r=4
            #coor = (0,1*(r-1),0)
        #    if i%2 == 1:
        #        coor = (angledistance,r*j,0)
        #    else:
        #        coor = (0,r*j,0)
        #    self.aminoacids.append(Aminoacid(val,coor,config[val]["radius"]))
        #    j = j + 1
        self.disulfideBonds = None

        #self.disulfideBonds = config["disulfideBonds"]


    def addAtom(self,atom):
        self.atoms.append(atom)
        #find suitable position

    #def addAminoAcid(self,amino):
    #    self.aminoacids.append(Aminoacid(val, coor, config[val]["radius"]))

    def addAASideChain(self,sidechain):
        self.atom.setSideChain(sidechain)

    def addDisulfideBonds(self,position1,position2):
        self.disulfideBonds.append([position1,position2])

    def randomTranslate(self,i):
        #self.aminoacids[i].translate()
        self.atoms[i].translate(1.5)
        if not self.validChain():
            self.revertPosition(i)

    def revertPosition(self,i):
        self.atoms[i].revertPosition()

    def getAminoAcidAtPosition(self,i):
        return(self.atoms[i])

    def getAtoms(self):
        return(self.atoms)

    def getLength(self):
        return len(self.atoms)

    def getEnergy(self):
        energy = [self.atoms[i].getLennartJonesPotential(self.atoms[j]) for i in range(len(self.atoms)) for j in range(len(self.atoms)) if i != j ]
        energy = sum(energy)
        return energy

    def getPositions(self):
        return [self.atoms[i].getCoor() for i in range(self.getLength())]

    def _unit_vector(self,vector):
        """ Returns the unit vector of the vector.  """
        return vector / np.linalg.norm(vector)

    def getAngle(self,i,j,k):
        #coordinates are (x,y,z) tuples
        p1 = self.atoms[i].getCoor()
        p2 = self.atoms[j].getCoor()
        p3 = self.atoms[k].getCoor()

        v1 = (p2[0] - p1[0],p2[1]-p1[0],p2[2]-p1[2])
        v2 = (p3[0] - p2[0],p3[1]-p2[0],p3[2]-p2[2])

        v1_u = self._unit_vector(v1)
        v2_u = self._unit_vector(v2)
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))



    def validChain(self):
        result = True
        for i in range(len(self.atoms)):
            for j in range(len(self.atoms)):
                if i != j:
                    coor1 = self.atoms[i].getCoor()
                    coor2 = self.atoms[j].getCoor()
                    radius1 = self.atoms[i].getRadius()
                    radius2 = self.atoms[j].getRadius()
                    dist = math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2 + (coor1[2] - coor2[2])**2)
                    if dist < radius1 + radius2:
                        result = False
                        break

        for i in range(len(self.atoms)):
            for j in range(i+1,len(self.atoms)):
                for k in range(j+1,len(self.atoms)):
                    if self.getAngle(i,j,k) > 2.0944:
                        result = False
                        break
        return result