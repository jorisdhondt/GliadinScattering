class pdbParser:
    def __init__(self, moleculeRepresentation):
        self.moleculRepresentation = moleculeRepresentation
        self.pdbRepresentation = None

    def parse(self,molecule):

        aminoacids = molecule.getAminoAcids()

        self.content = None
        s = ["ATOM".ljust(6)+i.rjust(5)+"N".center(4)+aminoacids[i].getAbbrevation().ljust(3)+"A".rjust(1)+"1".rjust(4)+ \
            str('%8.3f' % (float(aminoacids[i].getPositionX())).rjust(8))+str('%8.3f' % (float(aminoacids[i].getPositionY())).rjust(8))+str('%8.3f' % (float(aminoacids[i].getPositionZ())).rjust(8)) + \
            " ".rjust(6) + " ".ljust(6) for i in range(len(self.aminoacids))]

        file = '\n'.join(s)
        # j[0] = j[0].ljust(6)  # atom#6s
        # j[1] = j[1].rjust(5)  # aomnum#5d
        # j[2] = j[2].center(4)  # atomname$#4s
        # j[3] = j[3].ljust(3)  # resname#1s
        # j[4] = j[4].rjust(1)  # Astring
        # j[5] = j[5].rjust(4)  # resnum
        # j[6] = str('%8.3f' % (float(coords[i][0]))).rjust(8)  # x
        # j[7] = str('%8.3f' % (float(coords[i][1]))).rjust(8)  # y
        # j[8] = str('%8.3f' % (float(coords[i][2]))).rjust(8)  # z\
        # j[9] = str('%6.2f' % (float(j[9]))).rjust(6)  # occ
        # j[10] = str('%6.2f' % (float(j[10]))).ljust(6)  # temp
        # j[11] = j[11].rjust(12)  # elname
        # f1.write("%s%s %s %s %s%s    %s%s%s%s%s%s\n" % j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9],
        #          j[10], j[11]))


