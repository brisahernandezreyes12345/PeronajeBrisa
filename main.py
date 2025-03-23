"""
import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import math
import Acciones.sonidos as sd
import Acciones.escenarios as es
import Acciones.luces as lu
import src.pinta as pt
import Acciones.textos as tx
import Acciones.colores as color
import src.personaje as per

velocidad_camara = 0.1
velocidad_rotacion = 0.2
raton = 0.1
mouse_sensivity = 0.1

pygame.init()
pygame.mixer.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0,-1.0, -9)
glOrtho(-10,10,-10,10,-10,10)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glClearColor(1.0, 1.0, 1.0, 1.0)

pygame.event.set_grab(True)
pygame.mouse.set_visible(True)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_p:
                sd.sonidoOn('Ejemplo3D/Sonidos/musica.wav')
            if event.key == pygame.K_o:
                sd.sonidoOff()

    #Moviento de camara con teclado
    keys = pygame.key.get_pressed()

    if keys [pygame.K_s]:
        glTranslatef(0,0,10)
    if keys [pygame.K_w]:
        glTranslatef(0,0,-10)
    if keys [pygame.K_a]:
        glTranslatef(10,0,0)
    if keys [pygame.K_d]:
        glTranslatef(-10,0,0)
    if keys [pygame.K_x]:
        glTranslatef(0,10,0)
    if keys [pygame.K_z]:
        glTranslatef(0,-10,0)
    
    #Moviento de camara con mouse
    x, y = pygame.mouse.get_rel()
    x *= mouse_sensivity
    y *= mouse_sensivity
       
    if x != 0:
           glRotatef(x, 0, 1, 0)
    if y != 0:
           glRotatef(y, 1, 0, 0)
       
    pygame.mouse.set_pos(display[0] // 2, display[1] // 2)

   
    glPushMatrix()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)



    #es.pinta_escenario('Ejemplo3D/Imagenes/escenario1.jpg')
    glColor3f(1.0, 1.0, 1.0)
    es.pinta_escenario('Imagenes/escenario1.jpg') #Se busca desde la carpeta donde esta el main, lo estabas buscando afuera de la carpeta
    
    pt.parteSuperior()
    pt.parteInferior()

    pt.piernaIzq()
    glPopMatrix() 
    pygame.display.flip()
    pygame.time.wait(10)
"""
import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from Acciones import escenarios as es
from Acciones import sonidos as sd
from src import personaje as per

camara_z = -9
rotacion_y = 0.0
rotacion_x = 0.0
pygame.init()
pygame.mixer.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(0.5, 0.8, 1.0, 1)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, -1.0, camara_z)
glEnable(GL_DEPTH_TEST)
fondoAc='Imagenes/escenario1.jpg' #Controla el fondo actual


#Centra y hace invisible el cursor
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                fondoAc='Imagenes/escenario1.jpg'#Se busca desde la carpeta donde esta el main, lo estabas buscando afuera de la carpeta
                sd.sonidoOn('Sonidos/sonido1.mp3')
            if event.key == pygame.K_2:
                fondoAc='Imagenes/escenario2.jpg'
                sd.sonidoOn('Sonidos/sonido2.mp3')
            if event.key == pygame.K_3:
                fondoAc='Imagenes/escenario3.jpg'
                sd.sonidoOn('Sonidos/sonido3.mp3')
            if event.key == pygame.K_4:
                fondoAc='Imagenes/escenario4.jpg'
                sd.sonidoOn('Sonidos/sonido4.mp3')
            if event.key == pygame.K_5:
                fondoAc='Imagenes/escenario5.png'
                sd.sonidoOn('Sonidos/sonido5.mp3')

    #Se pueden movimientos mas fluidos con el mouse
    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    rotacion_y += mouse_dx * 0.1
    rotacion_x += mouse_dy * 0.1
    rotacion_x = max(-90, min(90, rotacion_x))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(rotacion_x, 1, 0, 0)
    glRotatef(rotacion_y, 0, 1, 0)


    glColor3f(1.0, 1.0, 1.0)
    es.pinta_escenario(fondoAc) 

    per.pinta_Normal()
    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()


    

