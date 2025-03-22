import pygame
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import src.pinta as pinta
import Acciones.colores as color
import Acciones.objetos as obj



def enojado():
    color.colorNaranja1()
    pinta.parteSuperior(1, 1, 20)
    pinta.parteInferior(1, 1, 20)
    color.colorRojo2()
    pinta.cabeza(0.7)
    color.colorAzulado()
    pinta.sombrero(.8, .8, 4)
    pinta.pieIzq(.2,0.9,0.2)
    pinta.pieDer(.2,0.9,0.2)
    pinta.manoIzq(0.9,0.2,0.2)
    pinta.manoDer(0.9,0.2,0.2)
    pinta.bocaTriste()
    color.colorVerde()
    glTranslatef(0, 0.7, -0.02)
    obj.ojo(.2,20,50)
    glTranslatef(0, 0.2, 5) 
    pinta.cejaEnojado()

def sorprendido():
    color.colorNaranja1()
    pinta.parteSuperior(1, 1, 20)
    pinta.parteInferior(1, 1, 20)
    color.colorRojo2()
    pinta.cabeza(0.7)
    color.colorAzulado()
    pinta.sombrero(.8, .8, 4)
    pinta.pieIzq(.2,0.9,0.2)
    pinta.pieDer(.2,0.9,0.2)
    pinta.manoIzq(0.9,0.2,0.2)
    pinta.manoDer(0.9,0.2,0.2)
    color.colorNegro()
    pinta.bocaSorp(0.2,100)
    color.colorVerde()
    glTranslatef(0, .5, -0.02)
    obj.ojo(.2,20,50)
    glTranslatef(0, -0.2,-0.02 )
    pinta.cejaSorp()


def feliz():
    color.colorNaranja1()
    pinta.parteSuperior(1, 1, 20)
    pinta.parteInferior(1, 1, 20)
    color.colorRojo2()
    pinta.cabeza(0.7)
    color.colorAzulado()
    pinta.sombrero(.8, .8, 4)
    pinta.pieIzq(.2,0.9,0.2)
    pinta.pieDer(.2,0.9,0.2)
    pinta.manoIzq(0.9,0.2,0.2)
    pinta.manoDer(0.9,0.2,0.2)

    glPushMatrix()
    glTranslatef(0.9, 1, 0.72)
    color.colorAzulado()
    obj.ojo(.2,20,50)
    pinta.cejaSorp()
 

    glTranslatef(0, -0.3, 0)
    pinta.bocaFeliz()

    glPopMatrix()



def asustado():
    color.colorNaranja1()
    pinta.parteSuperior(1, 1, 20)
    pinta.parteInferior(1, 1, 20)
    color.colorRojo2()
    pinta.cabeza(0.7)
    color.colorAzulado()
    pinta.sombrero(.8, .8, 4)
    pinta.pieIzq(.2,0.9,0.2)
    pinta.pieDer(.2,0.9,0.2)
    pinta.manoIzq(0.9,0.2,0.2)
    pinta.manoDer(0.9,0.2,0.2)
    pinta.bocaTriste()
    color.colorNegro()
    obj.ojo(.2,20,50)
    
    glTranslatef(0, -0.1, 0)
    pinta.cejaSorp()

def triste():
    color.colorNaranja1()
    pinta.parteSuperior(1, 1, 20)
    pinta.parteInferior(1, 1, 20)
    color.colorRojo2()
    pinta.cabeza(0.7)
    color.colorAzulado()
    pinta.sombrero(.8, .8, 4)
    pinta.pieIzq(.2,0.9,0.2)
    pinta.pieDer(.2,0.9,0.2)
    pinta.manoIzq(0.9,0.2,0.2)
    pinta.manoDer(0.9,0.2,0.2)

    color.colorNegro()
    obj.ojo(.2,20,50)
    
    glTranslatef(0, -0.8, 0)
    pinta.cejaEnojado()
    