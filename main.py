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

personaje_visible = True
emocion1 = False
emocion2 = False
emocion3 = False
emocion4 = False
emocion5 = False
accion1=False
accion2=False
accion3=False
accion4=False

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
            #if event.key == pygame.K_p:
                #sd.sonidoOn('Sonidos/musica.wav') 
            #if event.key == pygame.K_o:
                #sd.sonidoOff()
            if event.key == pygame.K_w:
                glTranslatef(0, 0, -0.5)
            if event.key == pygame.K_s:
                glTranslatef(0, 0, 0.5)
            if event.key == pygame.K_a:
                glTranslatef(-0.5, 0, 0)
            if event.key == pygame.K_d:
                glTranslatef(0.5, 0, 0)
            if event.key == pygame.K_r:
                camara_z = -9
                rotacion_x = 0
                rotacion_y = 0
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            if event.key == pygame.K_UP:
                camara_z += 0.5
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            if event.key == pygame.K_DOWN:
                camara_z -= 0.5
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)

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

    if personaje_visible:
        per.pinta_Normal()
    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()


    

