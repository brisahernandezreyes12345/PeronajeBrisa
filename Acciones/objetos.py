import pygame 
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image


def rectangulo(width=2, height=1, depth=3):

    w, h, d = width / 2, height / 2, depth / 2  # Mitades para centrarlo

    vertices = [
        [-w, -h, -d], [w, -h, -d], [w,  h, -d], [-w,  h, -d],  # Cara trasera
        [-w, -h,  d], [w, -h,  d], [w,  h,  d], [-w,  h,  d]   # Cara frontal
    ]

    faces = [
        (0, 1, 2, 3),  # Trasera
        (4, 5, 6, 7),  # Frontal
        (0, 1, 5, 4),  # Inferior
        (2, 3, 7, 6),  # Superior
        (0, 3, 7, 4),  # Izquierda
        (1, 2, 6, 5)   # Derecha
    ]

    normals = [
        (0, 0, -1),  # Trasera
        (0, 0, 1),   # Frontal
        (0, -1, 0),  # Inferior
        (0, 1, 0),   # Superior
        (-1, 0, 0),  # Izquierda
        (1, 0, 0)    # Derecha
    ]

    glBegin(GL_QUADS)
    for i in range(6):
        glNormal3fv(normals[i])  # Normal de la cara
        for j in faces[i]:
            glVertex3fv(vertices[j])  # Dibuja los vértices
    glEnd()



def cono(base, height, num_segments, inverted=True):### si tenia el traslate pero se lo quitamos
   

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Dibujar la superficie lateral del cono
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, height, 0)  # Vértice superior del cono
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x = base * math.cos(angle)
        y = 0
        z = base * math.sin(angle)
        glVertex3f(x, y, z)
    glEnd()

    # Dibujar la base del cono
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)  # Centro de la base
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x = base * math.cos(angle)
        y = 0
        z = base * math.sin(angle)
        glVertex3f(x, y, z)
    glEnd()

    

def cilindro(radio,angIncial,angFinal,segmentos):
        glBegin(GL_QUAD_STRIP)
        for i in range(segmentos):
            angulo = angIncial + i * (angFinal - angIncial) / segmentos
            x = radio * math.cos(angulo)
            y = radio * math.sin(angulo)
            glNormal3f(x, y, 0)
            glVertex3f(x, y, 0)
            glVertex3f(x, y, 1)
        glEnd() 

def mitadCirculo(radius=1, segments=20):###cambiar
   
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Centro del semicírculo

    for i in range(segments + 1):
        angle = math.pi * (i / segments)  # De 0 a π (180 grados)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)

    glEnd()



def esfera(radius=1, slices=20, stacks=20):

    for i in range(stacks):
        lat0 = math.pi * (-0.5 + i / stacks)  # Ángulo de latitud
        z0 = math.sin(lat0) * radius
        zr0 = math.cos(lat0) * radius

        lat1 = math.pi * (-0.5 + (i + 1) / stacks)
        z1 = math.sin(lat1) * radius
        zr1 = math.cos(lat1) * radius

        glBegin(GL_TRIANGLE_STRIP)
        for j in range(slices + 1):
            lng = 2 * math.pi * (j / slices)  # Ángulo de longitud
            x = math.cos(lng)
            y = math.sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)

            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

   
def linea(x1, y1, z1, x2, y2, z2, thickness=3.0):


    glLineWidth(thickness)  # Define el grosor de la línea
    glBegin(GL_LINES)
    glVertex3f(x1, y1, z1)  # Punto inicial
    glVertex3f(x2, y2, z2)  # Punto final
    glEnd()
    glLineWidth(5.0)  # Restablece el grosor a 1.0 (opcional)
    
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

def cubo(size=1):
   
    vertices = [
        [-size, -size, -size], [size, -size, -size], [size,  size, -size], [-size,  size, -size],  # Cara trasera
        [-size, -size,  size], [size, -size,  size], [size,  size,  size], [-size,  size,  size]   # Cara delantera
    ]

    faces = [
        (0, 1, 2, 3),  # Trasera
        (4, 5, 6, 7),  # Frontal
        (0, 1, 5, 4),  # Inferior
        (2, 3, 7, 6),  # Superior
        (0, 3, 7, 4),  # Izquierda
        (1, 2, 6, 5)   # Derecha
    ]

    normals = [
        (0, 0, -1),  # Trasera
        (0, 0, 1),   # Frontal
        (0, -1, 0),  # Inferior
        (0, 1, 0),   # Superior
        (-1, 0, 0),  # Izquierda
        (1, 0, 0)    # Derecha
    ]

    glBegin(GL_QUADS)
    for i in range(6):
        glNormal3fv(normals[i])  # Define la normal de la cara
        for j in faces[i]:
            glVertex3fv(vertices[j])  # Dibuja los vértices
    glEnd()

    
