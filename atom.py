import math
import random

# Define an atom class
class Atom:
    def __init__(self, coor, radius):
        self.coor = coor
        self.radius = radius   #3 different sizes

        #angles between bonds 120 degrees
        #angle needs to be maintained, only doable via rotation
        #bonds have a certain length
        #sphere are the amino-acid
        #


        #two options:
        # - 120 degrees
        # - necklace shaped


        self.epsilon = 1
        self.sigma = 2

    def getCoor(self):
        return self.coor

    def getRadius(self):
        return self.radius

    def getLennartJonesPotential(self,atom):
        #epsilon = 1
        epsilon = 0.156 #epsilon for water
        sigma = 1.25
        coor1 = atom.getCoor()
        coor2 = self.getCoor()
        r = math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2 + (coor1[2] - coor2[2])**2)
        power = 4*epsilon*((sigma/r)**12 - ((sigma/r))**6)
        return power

        #lattice new.


    def translate(self,translate_max):
        self.previousCoor = self.coor
        x_shift = random.uniform(-translate_max, translate_max)
        y_shift = random.uniform(-translate_max, translate_max)
        z_shift = random.uniform(-translate_max, translate_max)
        x = float(self.coor[0])
        y = float(self.coor[1])
        z = float(self.coor[2])

        delta = (x_shift, y_shift, z_shift)
        self.coor = tuple(sum(t) for t in zip(self.coor, delta))
        print(self.coor)

        #self.coor = (x+x_shift,y+y_shift,z+z_shift)
        #self.coor = self.coor + (x_shift,y_shift,z_shift)

    def revertPosition(self):
        self.coor = self.previousCoor
        self.previousCoor = None

    def rotate(self):
        #not_necessary
        print("irrelevant")