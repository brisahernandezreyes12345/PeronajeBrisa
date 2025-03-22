import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image
 
pygame.init()
pygame.mixer.init()
 
def carga_textura(filename):
    img=Image.open(filename)
    ix,iy,image=img.size[0], img.size[1], img.tobytes("raw","RGBX",0,-1)
    texturas_id=glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D,texturas_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,ix,iy,0,GL_RGBA,GL_UNSIGNED_BYTE,image)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    return texturas_id
 
"""
def pinta_escenario(fileimage):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, carga_textura(fileimage))

    #glColor(1, 1, 1)  # Asegurar que el color no afecte la textura

    # >>>>> CARA FRONTAL <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-50, 0, 50)  # Inferior izquierda
    glTexCoord2f(1, 0); glVertex3f(50, 0, 50)   # Inferior derecha
    glTexCoord2f(1, 1); glVertex3f(50, 100, 50)  # Superior derecha
    glTexCoord2f(0, 1); glVertex3f(-50, 100, 50) # Superior izquierda
    glEnd()

    # >>>>> CARA TRASERA <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(50, 0, -50)
    glTexCoord2f(1, 0); glVertex3f(-50, 0, -50)
    glTexCoord2f(1, 1); glVertex3f(-50, 100, -50)
    glTexCoord2f(0, 1); glVertex3f(50, 100, -50)
    glEnd()

    # >>>>> CARA IZQUIERDA <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-100, 0, -100)
    glTexCoord2f(1, 0); glVertex3f(-100, 0, 100)
    glTexCoord2f(1, 1); glVertex3f(-100, 200, 100)
    glTexCoord2f(0, 1); glVertex3f(-100, 200, -100)
    glEnd()

    # >>>>> CARA DERECHA <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(50, 0, 50)
    glTexCoord2f(1, 0); glVertex3f(50, 0, -50)
    glTexCoord2f(1, 1); glVertex3f(50, 100, -50)
    glTexCoord2f(0, 1); glVertex3f(50, 100, 50)
    glEnd()

    # >>>>> CARA SUPERIOR <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-50, 100, 50)
    glTexCoord2f(1, 0); glVertex3f(50, 100, 50)
    glTexCoord2f(1, 1); glVertex3f(50, 100, -50)
    glTexCoord2f(0, 1); glVertex3f(-50, 100, -50)
    glEnd()

    # >>>>> CARA INFERIOR <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-50, 0, -50)
    glTexCoord2f(1, 0); glVertex3f(50, 0, -50)
    glTexCoord2f(1, 1); glVertex3f(50, 0, 50)
    glTexCoord2f(0, 1); glVertex3f(-50, 0, 50)
    glEnd()

    glDisable(GL_TEXTURE_2D)  # Deshabilitar texturas después de pintar

 """

def pinta_escenario(fileimage):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, carga_textura(fileimage))
    glColor3f(1, 1, 1)

    # >>>>> CARA FRONTAL <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-20, -20, 20)
    glTexCoord2f(1, 0); glVertex3f(20, -20, 20)
    glTexCoord2f(1, 1); glVertex3f(20, 20, 20)
    glTexCoord2f(0, 1); glVertex3f(-20, 20, 20)
    glEnd()

    # >>>>> CARA TRASERA <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(20, -20, -20)
    glTexCoord2f(1, 0); glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 1); glVertex3f(-20, 20, -20)
    glTexCoord2f(0, 1); glVertex3f(20, 20, -20)
    glEnd()

    # >>>>> CARA IZQUIERDA <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 0); glVertex3f(-20, -20, 20)
    glTexCoord2f(1, 1); glVertex3f(-20, 20, 20)
    glTexCoord2f(0, 1); glVertex3f(-20, 20, -20)
    glEnd()

    # >>>>> CARA DERECHA <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(20, -20, 20)
    glTexCoord2f(1, 0); glVertex3f(20, -20, -20)
    glTexCoord2f(1, 1); glVertex3f(20, 20, -20)
    glTexCoord2f(0, 1); glVertex3f(20, 20, 20)
    glEnd()

    # >>>>> CARA SUPERIOR <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-20, 20, 20)
    glTexCoord2f(1, 0); glVertex3f(20, 20, 20)
    glTexCoord2f(1, 1); glVertex3f(20, 20, -20)
    glTexCoord2f(0, 1); glVertex3f(-20, 20, -20)
    glEnd()

    # >>>>> CARA INFERIOR <<<<<
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 0); glVertex3f(20, -20, -20)
    glTexCoord2f(1, 1); glVertex3f(20, -20, 20)
    glTexCoord2f(0, 1); glVertex3f(-20, -20, 20)
    glEnd()

    glDisable(GL_TEXTURE_2D)
