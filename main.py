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
from mpl_toolkits import mplot3d
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


# ax = plt.axes(projection='3d')
#
# # Data for a three-dimensional line
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')
#
# # Data for three-dimensional scattered points
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd


#a = np.random.rand(2000, 3)*10
#t = np.array([np.ones(100)*i for i in range(20)]).flatten()
#df = pd.DataFrame({"time": t ,"x" : a[:,0], "y" : a[:,1], "z" : a[:,2]})

def update_graph(num):
    data=positionsHistory[positionsHistory['time']==num]
    graph._offsets3d = (data.x, data.y, data.z)
    title.set_text('3D Test, time={}'.format(num))



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
title = ax.set_title('3D Test')

naccept = 0
nreject = 0
with open('first_setup.json') as json_file:
    input_json = json.load(json_file)

    nbofiterations = 1000

    gliadin_medium = Medium(input_json['sequence'], input_json['aminoacid'])
    mediumSize = gliadin_medium.getNbOfGliadin()
    #water

    old_energy = gliadin_medium.getEnergy()
    positionsHistory = pd.DataFrame()

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
        positions = gliadin.getPositions()
        df = pd.DataFrame(positions, columns=['x', 'y', 'z'])
<<<<<<< HEAD
        graph = ax.scatter(df.x, df.y, df.z)

        ani = matplotlib.animation.FuncAnimation(fig, update_graph, 19,interval=40, blit=False)

        plt.show()
=======
        df['time'] = i
        if i ==0:
            df['time'] = i
            positionsHistory = df
            #positionsHistory = pd.DataFrame({"time": i, "x": df[:, 'X'], "y": df[:, 'Y'], "z": df[:, 'Z']})
        else:
            positionsHistory = pd.concat([positionsHistory, df])

        i = i+1
        #ax.scatter3D(df['X'], df['Y'],df['Z'], c=df['Z'], cmap='Greens');
>>>>>>> 54c07ba3f68e80e4e6b33bfa9854fa9451eaaddf


        #plt.pause(10)

        # plt.figure()
        # plt.ylim((-10, +10))
        # plt.xlim((-10, +10))
        # for i in range(len(positions)):
        #     point = positions[i]
        #     plt.plot(point[0], point[1], '*')
        #     plt.show()
        #     #time.sleep(1)

        # plt.pause(1)

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

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    title = ax.set_title('3D Test')

    data = positionsHistory[positionsHistory['time'] == 0]
    graph = ax.scatter(data.x, data.y, data.z)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    ani = matplotlib.animation.FuncAnimation(fig, update_graph, nbofiterations,
                                             interval=400, blit=False)

    plt.show()