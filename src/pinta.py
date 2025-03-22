import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import math

import Acciones.luces as lc
import Acciones.colores as color
import Acciones.objetos as obj
from PIL import Image

############### BOCAS ###############
def bocaTriste():

    glPushMatrix()
    
    glTranslatef(0.9, 0.5, -0.72) 
    color.colorNegro()

    glPopMatrix()
    obj.mitadCirculo(0.3, 30) 
    

def bocaSorp(radius=0.5, segments=100):
    glPushMatrix()
    
    glTranslatef(0.9, 0.7, -0.72)
    
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Centro del círculo
    
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)

    glEnd()

    glPopMatrix()


def bocaFeliz():####################### no esta utilizando traslatef OJOOOOOOOOUSA ROTATEF
    glPushMatrix()   
    glRotatef(180, 0, 0, 0)
    
    glPopMatrix()

    obj.mitadCirculo(0.3, 30) 
    
 


#################### CEJAS ##########################

def cejaSorp(radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7):################## NUNCA USA TRASLATE NI ROTATEF, agregue PUSHMATRIZNNNN
    
    glPushMatrix()

    glLineWidth(thickness)  # Establece el grosor de la línea
    glBegin(GL_LINE_STRIP)  # Dibuja solo las líneas del arco   

    for i in range(segments + 1):
        angle = math.radians(start_angle + (end_angle - start_angle) * i / segments)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)

    glEnd()
    glPopMatrix()


def cejaEnojado():

    #FALTA EL TRASLATEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

    obj.linea(-0.3, 0, -5, 0.3, 0, -5,  thickness=8.0)  # Línea gruesa
    

################## CUERPO ###################

def parteSuperior():

    
    color.colorNaranja()
    glPushMatrix()

    glTranslatef(1,4,3)
    obj.cono(3,4,4)
    
    glPopMatrix()


def parteInferior():
    glPushMatrix()

    glEnable(GL_COLOR_MATERIAL)  # Habilita el uso de colores en materiales
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    color.colorNaranja()  # Aplica el color naranja correctamente

    glTranslatef(-1, -12, -3)  # Mueve la figura antes de rotar
    glRotatef(180, 0, 1, 0)  # Rota correctamente en el eje Y

    obj.cono(3, 4, 4)  # Dibuja la figura

    glDisable(GL_COLOR_MATERIAL)  # Desactiva el uso de materiales después de dibujar
    glPopMatrix()



def piernaIzq():

    glPushMatrix()

    glTranslatef(0.2,3,1.4)
    
    obj.rectangulo(0.7,4,0.5)
    
    glPopMatrix()



def load_texture(FileName): 
    #Abre la imagen del archivo que se dio.
    im = Image.open(FileName)
    #Obtiene el ancho y el alto de la imagen
    ix, iy = im.size 
    # Convertimos la imagen a bytes en formato RGB
    image = im.tobytes("raw", "RGBX", 0, -1)
        
    #Identificador de la textura    
    texture_id = glGenTextures(1)
    #Vincula la textura con el identificador a una textura 2D
    glBindTexture(GL_TEXTURE_2D, texture_id)
    #Establece la alineación de los bytes de la textura
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    # Cambiamos el formato de la textura a GL_RGBA para que coincida con los bytes de la imagen
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
   
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return texture_id

