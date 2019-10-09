import math
import random
import math

# Define an aminoacid class
class Aminoacid:
    def __init__(self, label, abbrevation,coor, radius):
        self.label = label
        self.abbreviation = abbrevation
        self.coor = coor
        self.radius = radius   #3 different sizes
        self.bridgedAcides = None
        self.previousCoor = None

        #angles between bonds 120 degrees
        #angle needs to be maintained, only doable via rotation
        #bonds have a certain length
        #sphere are the amino-acid
        #disulphide bridge
        #bonde stredge model
        #hydrophobic energy


        #maximum: (r1+r2)*1.2
        #minimum: (r1+r2)


        #two options:
        # - 120 degrees
        # - necklace shaped


        #50 enzymes


        self.epsilon = 1
        self.sigma = 2

    def getBridgedAcides(self):
        return self.bridgedAcides

    def setBridgeAcid(self,acid):
        self.bridgedAcides = self.bridgedAcides.add(acid)

    def revertPosition(self):
        self.coor = self.previousCoor
        self.previousCoor = None

    def getPosition(self):
        return self.coor

    def getRadius(self):
        return self.radius

    def getLennartJonesPotential(self,atom):
        coor1 = atom.getPosition()
        coor2 = self.getPosition()
        r = math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2 + (coor1[2] - coor2[2])**2)
        epsilon = 0.5
        sigma = 0.2
        power = 4*epsilon*((sigma/r)**12 - ((sigma/r))**6)
        return power

        #lattice new.


    def getElectricCharge(self):
        if self.label == 'K' or self.label == "R" or self.label == "H":
            return 1
        elif self.label == "D" or self.label == "E":
            return -1
        else:
            return 0

    def translate(self):
        self.previousCoor = self.coor
        x_shift = random.uniform(-0.1, 0.1)
        y_shift = random.uniform(-0.1, 0.1)
        z_shift = random.uniform(-0.1, 0.1)

        delta = (x_shift,y_shift,z_shift)
        self.coor = tuple(sum(t) for t in zip(self.coor, delta))

    def rotate(self):
        #not_necessary
        print("irrelevant")

