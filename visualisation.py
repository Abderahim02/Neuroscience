# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:52:34 2022

@author: Amelie_Aussel
"""

import matplotlib.pyplot as plt
import scipy.io
import numpy as np
from mpl_toolkits import mplot3d


def plot_connection_matrix_3d(matrix,positions):
    rows, cols = np.where(matrix > 0)
    print("Nombre d'aretes : "+str(len(rows.tolist())))
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for k in range(len(rows.tolist())) :
        x,y=rows[k],cols[k]
        ax.plot3D([positions[x,0],positions[y,0]],[positions[x,1],positions[y,1]],[positions[x,2],positions[y,2]],'k', zorder=1,lw=matrix[x,y])
    ax.scatter3D(positions[:,0],positions[:,1],positions[:,2], s=40, zorder=2)

def plot_connection_matrix_2d(matrix,positions):
    rows, cols = np.where(matrix > 0)
    print("Nombre d'aretes : "+str(len(rows.tolist())))
    plt.figure()
    for k in range(len(rows.tolist())) :
        x,y=rows[k],cols[k]
        plt.plot([positions[x,0],positions[y,0]],[positions[x,1],positions[y,1]],'k', zorder=1,lw=matrix[x,y])
    plt.scatter(positions[:,0],positions[:,1], s=40, zorder=2)

mat1 = scipy.io.loadmat('Coactivation_matrix.mat')
Coactivation_matrix1=mat1['Coactivation_matrix']
Coordinates1=mat1['Coord']

mat2 = scipy.io.loadmat('GroupAverage_rsfMRI_matrix.mat')
Coactivation_matrix2=mat2['GroupAverage_rsfMRI']
Coordinates2=mat2['Coord']

Nmax=4
Nmax=min(Nmax,Coactivation_matrix.shape[0])
print('Nombre de sommets conserves: '+str(Nmax))
Coactivation_matrix=Coactivation_matrix[:Nmax,:Nmax]
Coordinates=Coordinates[:Nmax,:]
plt.close('all')
plot_connection_matrix_3d(Coactivation_matrix,Coordinates)
plot_connection_matrix_2d(Coactivation_matrix,Coordinates)
print(Coactivation_matrix)
print(len(Coactivation_matrix))
#plt.show()
print(Coactivation_matrix2)
print(Coactivation_matrix1)

def visualation(n):  
    print('Nombre de sommets total : '+str(Coactivation_matrix2.shape[0]))
    Nmax=n
    Nmax=min(Nmax,Coactivation_matrix2.shape[0])
    print('Nombre de sommets conserves: '+str(Nmax))
    Coactivation_matrix2=Coactivation_matrix[:Nmax,:Nmax]
    Coordinates2=Coordinates2[:Nmax,:]
    plt.close('all')
    plot_connection_matrix_3d(Coactivation_matrix2,Coordinates2)
    plot_connection_matrix_2d(Coactivation_matrix2,Coordinates2)
    plt.show()

import time

def calcul_max_sommets_1minute():
    n=50
    # Mesurer le temps d'exécution de la fonction
    start_time = time.time()
    visualation(n)
    end_time = time.time()
    # Calculer le temps d'exécution
    execution_time = end_time - start_time
    while execution_time < 60 : 
        n+=200
        start_time = time.time()
        visualation(n)
        end_time = time.time()
        execution_time = end_time - start_time
    print("le nombre de sommets visulisés: ", n)
    return None
#calcul_max_sommets_1minute()

def rich_club_coefficient(G):
    return 0