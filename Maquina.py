import pygame
from pygame.locals import *
import random 

TAM_CUADRO = 20
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ANCHO = 800
ALTO = 600


class Maquina:
    def __init__(self):
        self.segmentos = [(15*TAM_CUADRO, 15*TAM_CUADRO)]
        self.direccion = "derecha"
    
    def mover(self, serpiente):
        cabeza_x, cabeza_y = self.segmentos[0]
        
        # Si la máquina está en la misma fila que la serpiente
        if cabeza_y == serpiente.segmentos[0][1]:
            if cabeza_x < serpiente.segmentos[0][0]:
                self.direccion = "derecha"
            else:
                self.direccion = "izquierda"
        # Si la máquina está en la misma columna que la serpiente
        elif cabeza_x == serpiente.segmentos[0][0]:
            if cabeza_y < serpiente.segmentos[0][1]:
                self.direccion = "abajo"
            else:
                self.direccion = "arriba"
        
        self.mover_automaticamente()
    
    def mover_automaticamente(self):
        # Movimiento aleatorio
        posibles_direcciones = ["derecha", "izquierda", "arriba", "abajo"]
        posibles_direcciones.remove(self.direccion)
        # Descartamos las direcciones que llevarían a una colisión
        for direccion in posibles_direcciones:
            if direccion == "derecha" and (self.segmentos[0][0]+TAM_CUADRO, self.segmentos[0][1]) in self.segmentos:
                posibles_direcciones.remove(direccion)
            elif direccion == "izquierda" and (self.segmentos[0][0]-TAM_CUADRO, self.segmentos[0][1]) in self.segmentos:
                posibles_direcciones.remove(direccion)
            elif direccion == "arriba" and (self.segmentos[0][0], self.segmentos[0][1]-TAM_CUADRO) in self.segmentos:
                posibles_direcciones.remove(direccion)
            elif direccion == "abajo" and (self.segmentos[0][0], self.segmentos[0][1]+TAM_CUADRO) in self.segmentos:
                posibles_direcciones.remove(direccion)
        
        # Si todas las direcciones llevan a una colisión, la máquina se mueve en la dirección actual
        if not posibles_direcciones:
            return
        
        # Se elige aleatoriamente una de las direcciones posibles y se mueve en esa dirección
        nueva_direccion = random.choice(posibles_direcciones)
        self.direccion = nueva_direccion
        
        cabeza_x, cabeza_y = self.segmentos[0]
        
        if self.direccion == "derecha":
            cabeza_x += TAM_CUADRO
        elif self.direccion == "izquierda":
            cabeza_x -= TAM_CUADRO
        elif self.direccion == "arriba":
            cabeza_y -= TAM_CUADRO
        elif self.direccion == "abajo":
            cabeza_y += TAM_CUADRO
        
        # Agregamos el nuevo segmento al principio de la lista
        self.segmentos.insert(0, (cabeza_x, cabeza_y))
        
        # Eliminamos el último segmento
        self.segmentos.pop()
    
    def dibujar(self, pantalla):
        for segmento in self.segmentos:
            pygame.draw.rect(pantalla, ROJO, (segmento[0], segmento[1], TAM_CUADRO, TAM_CUADRO))
