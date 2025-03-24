import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame.locals import *
from Acciones import escenarios as es
import Acciones.objetos as pinta
import Acciones.textos as tx

import threading
import time

"""def animaBrazo2():
    global frame_count, paso
    
    if 'frame_count' not in globals():
        frame_count = 0
    if 'paso' not in globals():
        paso = 0

    frame_count += 1

    if frame_count % 15 == 0:  # Cambia cada 15 frames (ajusta la velocidad según lo desees)
        paso = (paso + 1) % 2  # Cambia entre 0 y 1 únicamente, repitiendo solo esos pasos

    # Dibujar cuerpo 
    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(0.9176, 0.298, 0.2745))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1, color=(0.1764, 0.415, 0.309))
    pinta.pinta_prisma(x=-0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izquierdo
    pinta.pinta_prisma(x=0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der

 
    
    pinta.pinta_esfera(x=0, y=2.4, z=0.76, radio=0.2, color=(0, 0, 0)) 
    pinta.pinta_boca(x=0, y=2.0, z=0.76,  radius= 0.4, segments=20, rotacion=(180, 0, 0), color=(0, 0, 0))
    pinta.pinta_arco(x=0, y=2.3, z=0.76, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7)

    if paso == 0:
        pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(60, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
        pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der

    elif paso == 1:
       pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(60, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
       pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
"""

def levantaBrazo():
    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(0.9176, 0.298, 0.2745))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1, color=(0.1764, 0.415, 0.309))
    pinta.pinta_prisma(x=-0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izquierdo
    pinta.pinta_prisma(x=0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(-90, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der

    pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
    pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_esfera(x=0, y=2.4, z=0.76, radio=0.2, color=(0, 0, 0)) 
    pinta.pinta_boca(x=0, y=2.0, z=0.76,  radius= 0.4, segments=20, rotacion=(180, 0, 0), color=(0, 0, 0))
    pinta.pinta_arco(x=0, y=2.3, z=0.76, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7)
    
def actualizar_brazo(value):
    """Anima el brazo derecho moviéndolo de 0 a 180 grados y de regreso."""
    global angulo_brazo, subiendo

    if subiendo:
        angulo_brazo += 5  # Incrementa el ángulo
        if angulo_brazo >= 180:
            subiendo = False  # Cambia de dirección
    else:
        angulo_brazo -= 5  # Decrementa el ángulo
        if angulo_brazo <= 0:
            subiendo = True  # Vuelve a subir

    glutPostRedisplay()  # Redibuja la escena
    glutTimerFunc(50, actualizar_brazo, 0)  # Vuelve a llamar en 50ms
