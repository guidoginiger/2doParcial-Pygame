import pygame, sys
import colores

class Boton:
    def __init__(self, x, y, imagen) -> None:
        self.imagen = pygame.transform.scale(imagen, (90,80))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.click = False

    def crear_botones(self, surface):
        surface.blit(self.imagen, (self.rect.x, self.rect.y))

        accion = False

        #Obtener la posicion del mouse.
        mouse_pos = pygame.mouse.get_pos()
        #Chequear la posicion del mouse con respecto al rectangulo de las imagenes.
        if self.rect.collidepoint(mouse_pos):
            #print("Cursor")
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                #Configurado para que haga 'CLICK' con el boton izquierdo del mouse.
                #print("CLICK")
                self.click = True
                accion = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
            
        return accion

