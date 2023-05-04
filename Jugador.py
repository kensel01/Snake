from pygame.locals import *
import pygame

TAM_CUADRO = 20
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ANCHO = 800
ALTO = 600
class Jugador:
    def __init__(self):
        self.segmentos = [(5*TAM_CUADRO, 5*TAM_CUADRO)]
        self.direccion = "derecha"
        self.puntuacion = 0
    
    def mover(self):
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
        
        # Eliminamos el último segmento si la serpiente es más larga que su puntuación
        if len(self.segmentos) > self.puntuacion:
            self.segmentos.pop()
    
    def dibujar(self, pantalla):
        for segmento in self.segmentos:
            pygame.draw.rect(pantalla, VERDE, (segmento[0], segmento[1], TAM_CUADRO, TAM_CUADRO))
    
    def colision(self):
        cabeza = self.segmentos[0]
        
        # Si la serpiente choca con una pared
        if cabeza[0] < 0 or cabeza[0] >= ANCHO or cabeza[1] < 0 or cabeza[1] >= ALTO:
            return True
        
        # Si la serpiente choca consigo misma
        if cabeza in self.segmentos[1:]:
            return True
        
        return False