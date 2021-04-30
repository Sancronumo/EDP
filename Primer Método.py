# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:58:55 2021

@author: yisus
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Definición de Variables
xmin=0
xmax=10
tmin=0
tmax=10

numeroPuntosX=20
numeroPuntosT=50
cambiot=(tmax-tmin)/(numeroPuntosT-1)
cambiox=(xmax-xmin)/(numeroPuntosX-1)

valoresX=np.linspace(xmin,xmax,numeroPuntosX)
valoresT=np.linspace(tmin,tmax,numeroPuntosT)

constantel=1.5
constanteD=0.5
constanteA=2.0
constanteXo=5.0

cantidadIteraciones=10

#Definir la función para calcular la matriz inicial
def CalcularMatriz(valoresX, valoresT,l,A,Xo):
    '''
    Parameters
    ----------
    valoresX : un array con los valores de x
    valoresT : un array con los valores de y
    l : la constante l del problema 
    A : la constante A del problema
    Xo : la constante Xo del problema
    Returns
    -------
    matrizInicial : una matriz con los valores de la matriz inicial

    '''
    matrizInicial=np.zeros([len(valoresT),len(valoresX)])
    for i in range(0,len(valoresX)-1):
        for j in range(0,len(valoresT)-1):
            if j==0:
                matrizInicial[j,i]=A*np.exp(-(valoresX[i]-Xo)**2/l)
    return matrizInicial

matrizInicial=CalcularMatriz(valoresX, valoresT, constantel, constanteA, constanteXo)

# función para iterar sobre la matriz


def IterarDiferencias(matrizInicial,cambiox,cambiot,constanteD,cantidadIteraciones):
    '''
    Parameters
    ----------
    matrizInicial : matriz con valores iniciales
    constanteG : constante G del programa calculada con la otra función
    cambiox : cambio de x
    cambiot : cambio de t
    constanteD : constante del problema
    cantidadIteraciones : cantidad de iteraciones deseada.

    Returns
    -------
    matrizInicial : matriz con los valores ya iterados

    '''
    while cantidadIteraciones>0:       
        for i in range(1,np.shape(matrizInicial)[1]-2):
            for j in range(0,np.shape(matrizInicial)[0]-2):
                matrizInicial[j+1,i]=matrizInicial[j,i]+constanteD*cambiot/cambiox**2*(matrizInicial[j,i+1]+matrizInicial[j,i-1]-2*matrizInicial[j,i])                                    
        cantidadIteraciones-=1
    return matrizInicial

matrizFinal=IterarDiferencias(matrizInicial, cambiox, cambiot, constanteD, cantidadIteraciones)


fig=plt.figure()
ax=Axes3D(fig)
X, T= np.meshgrid(valoresX,valoresT)
ax.plot_surface(X,T,matrizFinal)
ax.set_xlabel('Valores de espacio')
ax.set_ylabel('Valores de tiempo')
ax.set_zlabel('Valores de calor')
plt.show()

            
    
    