
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import Acciones.objetos as pinta

def pinta_Normal():
    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(1.0, 0.5, 0.0), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(1.0, 0.5, 0.0), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(1.0, 0.0, 1.0))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1.5, color=(1.0, 0.5, 0.0))
    pinta.pinta_prisma(x=-1.0, y=1.0, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 20), color=(1.0, 0.0, 1.0))  # Izquierdo
    pinta.pinta_prisma(x=1.0, y=1.0, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, -20), color=(1.0, 0.0, 1.0))  # Derecho
    pinta.pinta_prisma(x=-0.7, y=-1.5, z=0.5, escala=(0.3, 0.9, 0.3), rotacion=(-45, 0, 0), color=(1.0, 0.0, 1.0))  # Izq
    pinta.pinta_prisma(x=0.7, y=-1.5, z=0.5, escala=(0.3, 0.9, 0.3), rotacion=(-45, 0, 0), color=(1.0, 0.0, 1.0))  # Der
    pinta.pinta_esfera(x=-0.4, y=2.4, z=0.76, radio=0.1, color=(0, 0, 0))  # Ojo izquierdo
    pinta.pinta_esfera(x=0.4, y=2.4, z=0.76, radio=0.1, color=(0, 0, 0))   # Ojo derecho
    pinta.pinta_bocaFeliz(x=0, y=2.0, z=0.76, radio=0.4, angulo_inicio=180, angulo_fin=360, color=(0, 0, 0))
