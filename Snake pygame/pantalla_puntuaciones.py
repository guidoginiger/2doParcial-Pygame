import pygame, sys
import puntuaciones
import colores

pygame.init()

fuente_puntaje = pygame.font.Font("Consolas", 25)
fuente_titulo_puntaje = pygame.font.Font("Consolas", 45)
fuente_salir = pygame.font.Font("Consolas", 25)

def puntaje(pantalla):
    run_scores = True
    pantalla.fill(colores.NEGRO)

    #Mostrar lista de puntajes
    puntajes = puntuaciones.lista_puntajes()

    while run_scores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_scores = False
                pygame.quit() 
                sys.exit()
        
        titulo = fuente_titulo_puntaje.render('POSICIONES', True, (colores.DORADO))
        pantalla.blit(titulo, (150, 200))

        rectangulo_scores = pygame.Rect(350, 120, 350, 460)
        pygame.draw.rect(pantalla, (colores.AZUL), rectangulo_scores)

        for indice, elemento in enumerate(puntajes):
            posicion_jugador = f'{str(indice +1).zfill(2)} - {elemento[1]}'
            puntuacion_jugador =  f'{elemento[2]}'
            texto_a_mostrar = posicion_jugador +  puntuacion_jugador
            texto = fuente_puntaje.render(texto_a_mostrar, True, (colores.CELESTE))
            pantalla.blit(texto, ((500 - (texto.get_width()//2)), 30*indice + 150))
        
        titulo_salir = fuente_titulo_puntaje.render('PRESIONA ESC PARA SALIR', True, (colores.DORADO))
        pantalla.blit(titulo_salir, (100, 550))

        pygame.display.update()
        
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_ESCAPE]:
            run_scores = False
            pygame.quit()
            sys.exit

