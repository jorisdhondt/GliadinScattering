class pdbParser:
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
        coor1 = atom.getCoor()
        coor2 = self.getCoor()
        r = sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2 + (coor1[2] - coor2[2])**2)
        power = 4*epsilon*((sigma/r)**12 - ((sigma/r))**6)
        return power

        #lattice new.


    def translate(self,translate_max):
        x_shift = random.uniform(-translate_max, translate_max)
        y_shift = random.uniform(-translate_max, translate_max)
        z_shift = random.uniform(-translate_max, translate_max)

        self.coor = self.coor + (x_shift,y_shift,z_shift)

    def rotate(self):
        #not_necessary
        print("irrelevant")