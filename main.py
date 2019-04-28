# calculate the old energy
from medium import Medium
import random as rn
import json
import math
import numpy as np
import pandas as pd
from scipy.constants import Boltzmann
#import sys, pygame, math
#from pygame.locals import *

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation


# def init():
#     """initialize animation"""
#     global box, rect
#     particles.set_data([], [])
#     rect.set_edgecolor('none')
#     return particles, rect
#
#
# def animate(i):
#     """perform animation step"""
#     global box, rect, dt, ax, fig
#     box.step(dt)
#
#     ms = int(fig.dpi * 2 * box.size * fig.get_figwidth()
#              / np.diff(ax.get_xbound())[0])
#
#     # update pieces of the animation
#     rect.set_edgecolor('k')
#     particles.set_data(box.state[:, 0], box.state[:, 1])
#     particles.set_markersize(ms)
#     return particles, rect


naccept = 0
nreject = 0
with open('first_setup.json') as json_file:
    input_json = json.load(json_file)

    nbofiterations = 100000

    gliadin_medium = Medium(input_json['sequence'], input_json['aminoacid'])
    mediumSize = gliadin_medium.getNbOfGliadin()
    #water

    old_energy = gliadin_medium.getEnergy()

    for i in range(nbofiterations):
        print("Iteration "+str(i))
        # Pick a random atom (random.randint(x,y) picks a random
        # integer between x and y, including x and y)

        selectedGliadin = rn.randint(0,mediumSize)-1;
        gliadin = gliadin_medium.getGliadin(selectedGliadin)
        print("start posities")
        print(gliadin.getPositions())


        gliadinLength = gliadin.getLength()
        selectedAminoAcid = rn.randint(0, gliadinLength-1);
        gliadin.randomTranslate(selectedAminoAcid)

        new_energy = gliadin_medium.getEnergy()

        accept = False

        # Automatically accept if the energy goes down
        if (new_energy <= old_energy):
            accept = True

        else:
            # Now apply the Monte Carlo test - compare
            # exp( -(E_new - E_old) / kT ) >= rand(0,1)
            x = math.exp(-(new_energy - old_energy) / (Boltzmann*292))

            if (x >= rn.uniform(0.0, 1.0)):
                accept = True
            else:
                accept = False

        if accept:
            # accept the move
            naccept += 1
            total_energy = new_energy
        else:
            # reject the move - restore the old coordinates
            gliadin.revertPosition(selectedAminoAcid)
            nreject += 1
            total_energy = old_energy

        print("Lowest energy: "+str(total_energy))
        print(gliadin.getPositions())

        # fig = plt.figure()
        # fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        # ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
        #                      xlim=(-3.2, 3.2), ylim=(-2.4, 2.4))
        #
        # # particles holds the locations of the particles
        # particles, = ax.plot([], [], 'bo', ms=6)
        #
        # # rect is the box edge
        # rect = plt.Rectangle(box.bounds[::2],
        #                      box.bounds[1] - box.bounds[0],
        #                      box.bounds[3] - box.bounds[2],
        #                      ec='none', lw=2, fc='none')
        # ax.add_patch(rect)
        #
        # ani = animation.FuncAnimation(fig, animate, frames=600,
        #                               interval=10, blit=True, init_func=init)
        #
        # # save the animation as an mp4.  This requires ffmpeg or mencoder to be
        # # installed.  The extra_args ensure that the x264 codec is used, so that
        # # the video can be embedded in html5.  You may need to adjust this for
        # # your system: for more information, see
        # # http://matplotlib.sourceforge.net/api/animation_api.html
        # # ani.save('particle_box.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
        #
        # plt.show()