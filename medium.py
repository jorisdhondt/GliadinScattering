# Define a medium class - medium is a collection of
# atoms
import aminoacid
from gliadin import Gliadin

#collection of gliadins
class Medium:
    def __init__(self, sequence,config):
        self.config = config
        self.sequence = sequence
        self.nbofSequences = 1
        self.sequenceCollection = []
        ##self.natoms = na
        self.COM = [0.0, 0.0, 0.0]

        for i in range(0, self.nbofSequences):
            self.sequenceCollection.append(Gliadin(sequence,config))

    def getEnergy(self):
        energylevel = 0
        for i in self.sequenceCollection:
            energylevel = energylevel + i.getEnergy()
        return energylevel

    def getGliadin(self,i):
        return self.sequenceCollection[i]

    def getNbOfGliadin(self):
        return len(self.sequenceCollection)
