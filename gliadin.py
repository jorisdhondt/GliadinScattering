import random
import aminoacid

# Define an atom class
class Gliadin:
    def __init__(self, chain,config):
        #config = MKTFLILALL

        self.aminoacids = []
        for i in range(0, chain):
            self.aminoacids.append(Aminoacid())