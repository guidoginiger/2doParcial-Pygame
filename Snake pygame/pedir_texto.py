import pygame, sys
import colores

pygame.init()

def ingresar_nombre(pantalla):

    nombre = ''
    ingreso_nombre = True
    while ingreso_nombre:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ingreso_nombre = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                    #Permite borrar la ultima letra
                elif event.key == pygame.K_RETURN and len(nombre) > 0:
                    ingreso_nombre = False
                    return nombre
                
                elif event.key == pygame.K_SPACE:
                    nombre += '_'
                else:
                    nombre = event.unicode