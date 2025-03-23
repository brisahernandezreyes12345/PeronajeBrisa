
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
def pinta_cono(x, y, z, radio_base, altura, color, rotacion):
    """Dibuja un cono con posición, color y rotación opcional."""
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(rotacion[0], 1, 0, 0)
    glRotatef(rotacion[1], 0, 1, 0)
    glRotatef(rotacion[2], 0, 0, 1)

    glColor3f(*color)
    glRotatef(-90, 1, 0, 0)  # Alinea el cono en eje Y

    quad = gluNewQuadric()
    gluCylinder(quad, radio_base, 0.0, altura, 20, 20)

    # Base del cono
    glRotatef(180, 1, 0, 0)
    gluDisk(quad, 0.0, radio_base, 20, 1)

    glPopMatrix()

def pinta_cubo(x, y, z, size, color):
    """Dibuja un cubo manualmente, centrado en (x, y, z), con tamaño y color."""
    hs = size / 2.0  # mitad del tamaño para centrarlo
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(*color)

    # Caras del cubo
    glBegin(GL_QUADS)
    # Cara frontal
    glVertex3f(-hs, -hs,  hs)
    glVertex3f( hs, -hs,  hs)
    glVertex3f( hs,  hs,  hs)
    glVertex3f(-hs,  hs,  hs)

    # Cara trasera
    glVertex3f( hs, -hs, -hs)
    glVertex3f(-hs, -hs, -hs)
    glVertex3f(-hs,  hs, -hs)
    glVertex3f( hs,  hs, -hs)

    # Cara izquierda
    glVertex3f(-hs, -hs, -hs)
    glVertex3f(-hs, -hs,  hs)
    glVertex3f(-hs,  hs,  hs)
    glVertex3f(-hs,  hs, -hs)

    # Cara derecha
    glVertex3f( hs, -hs,  hs)
    glVertex3f( hs, -hs, -hs)
    glVertex3f( hs,  hs, -hs)
    glVertex3f( hs,  hs,  hs)

    # Cara superior
    glVertex3f(-hs,  hs,  hs)
    glVertex3f( hs,  hs,  hs)
    glVertex3f( hs,  hs, -hs)
    glVertex3f(-hs,  hs, -hs)

    # Cara inferior
    glVertex3f(-hs, -hs, -hs)
    glVertex3f( hs, -hs, -hs)
    glVertex3f( hs, -hs,  hs)
    glVertex3f(-hs, -hs,  hs)
    glEnd()

    glPopMatrix()

def pinta_piramide(x, y, z, base, altura, color):
    """Dibuja una pirámide de base cuadrada centrada en (x, y, z)."""
    hs = base / 2.0  # mitad del tamaño base
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(*color)

    # Caras triangulares
    glBegin(GL_TRIANGLES)
    # Frente
    glVertex3f(-hs, 0, hs)
    glVertex3f(hs, 0, hs)
    glVertex3f(0, altura, 0)

    # Derecha
    glVertex3f(hs, 0, hs)
    glVertex3f(hs, 0, -hs)
    glVertex3f(0, altura, 0)

    # Atrás
    glVertex3f(hs, 0, -hs)
    glVertex3f(-hs, 0, -hs)
    glVertex3f(0, altura, 0)

    # Izquierda
    glVertex3f(-hs, 0, -hs)
    glVertex3f(-hs, 0, hs)
    glVertex3f(0, altura, 0)
    glEnd()

    # Base cuadrada
    glBegin(GL_QUADS)
    glVertex3f(-hs, 0, hs)
    glVertex3f(hs, 0, hs)
    glVertex3f(hs, 0, -hs)
    glVertex3f(-hs, 0, -hs)
    glEnd()

    glPopMatrix()

def pinta_prisma(x, y, z, escala, rotacion, color):
    """
    Dibuja un prisma rectangular (cuboid) con posición, escala y rotación personalizada.
    escala: (sx, sy, sz) → tamaño en cada eje.
    rotacion: (rx, ry, rz) → grados a rotar en cada eje.
    """
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(rotacion[0], 1, 0, 0)
    glRotatef(rotacion[1], 0, 1, 0)
    glRotatef(rotacion[2], 0, 0, 1)
    glScalef(*escala)
    glColor3f(*color)

    # Dibuja cubo base (prisma escalado)
    glBegin(GL_QUADS)
    # Cara frontal
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f( 0.5, -0.5, 0.5)
    glVertex3f( 0.5,  0.5, 0.5)
    glVertex3f(-0.5,  0.5, 0.5)

    # Cara trasera
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)

    # Izquierda
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5, -0.5)

    # Derecha
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5,  0.5)

    # Superior
    glVertex3f(-0.5, 0.5,  0.5)
    glVertex3f( 0.5, 0.5,  0.5)
    glVertex3f( 0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    # Inferior
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glEnd()
    glPopMatrix()


def pinta_esfera(x, y, z, radio, color):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(*color)
    quad = gluNewQuadric()
    gluSphere(quad, radio, 20, 20)
    glPopMatrix()

def pinta_bocaFeliz(x, y, z, radio, angulo_inicio, angulo_fin, color):
    """Dibuja un arco como boca en el plano XY, de angulo_inicio a angulo_fin (grados)."""
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(*color)
    glBegin(GL_LINE_STRIP)
    for ang in range(angulo_inicio, angulo_fin+1, 5):
        rad = math.radians(ang)
        glVertex3f(radio * math.cos(rad), radio * math.sin(rad), 0)
    glEnd()
    glPopMatrix()
