import pygame, sys, random
from pygame.math import Vector2
import colores
import botones

class SNAKE:
	def __init__(self) -> None:
		self.cuerpo = [Vector2(6,10), Vector2(5,10), Vector2(4,10)]
		self.direccion = Vector2(1,0)
		#Mi snake se inicia direccionandose hacia la derecha.
		self.nuevo_bloque = False
		self.sonido_comida = pygame.mixer.Sound("Sonidos/Comida.mp3")
		self.sonido_choque = pygame.mixer.Sound("Sonidos/Choque.mp3")
		self.musica_principal = pygame.mixer.Sound("Sonidos/In The Canime.mp3")
		
	def crear_snake(self):
		for bloque in self.cuerpo:
			x_pos = int(bloque.x * celda_tamanio)
			y_pos = int(bloque.y * celda_tamanio)
			bloque_rect = pygame.Rect(x_pos, y_pos, celda_tamanio, celda_tamanio)
			pygame.draw.rect(pantalla, (colores.AZUL), bloque_rect)
			#Coloco un rectangulo en la celda donde se encuentra la snake.

	def movimiento_snake(self):
		if self.nuevo_bloque == True:
			cuerpo_copia = self.cuerpo[:]
			cuerpo_copia.insert(0, cuerpo_copia[0] + self.direccion)
			self.cuerpo = cuerpo_copia[:]
			self.nuevo_bloque = False
		else:
			#Copio la lista del cuerpo del snake MENOS el ultimo elemento.
			#Este ultimo elemento desaparece.
			cuerpo_copia = self.cuerpo[:-1]
			cuerpo_copia.insert(0, cuerpo_copia[0] + self.direccion)
			#Agrego un nuevo elemento adelante, que es el primer elemento de la lista anterior.
			#Y por ultimo le paso la direccion.
			self.cuerpo = cuerpo_copia[:]
	
	def agregar_bloque(self):
		self.nuevo_bloque = True
	
	def sonar_comida(self):
		self.sonido_comida.play()
	
	def sonar_choque(self):
		self.sonido_choque.play()
	
	def sonar_musica(self):
		self.musica_principal.play()

class FRUTA:
	def __init__(self) -> None:
		self.randomize()

	def crear_fruta(self):
		x_pos = int(self.pos.x * celda_tamanio)
		y_pos = int(self.pos.y * celda_tamanio)
		fruta_rect = pygame.Rect(x_pos, y_pos , celda_tamanio, celda_tamanio)
		pantalla.blit(manzana, fruta_rect)
		
		#pygame.draw.rect(pantalla, (colores.GRIS), fruta_rect)
		#Coloco un rectangulo la celda donde se encuentra la fruta.
	
	def randomize(self):
		#Creo una posicion aleatoria para 'x' e 'y'. ('-1' es para que siempre este dentro de la pantalla).
		self.x = random.randint(0, celda_numero - 1)
		self.y = random.randint(0, celda_numero - 1)
                
		self.pos = Vector2(self.x , self.y)
        #Creo un vector bidimensional, logra que sea mas sencillo acceder a las posiciones 'x' e 'y'.
		#Obtengo la posicion de la fruta en la pantalla.

class OBSTACULO:
	def __init__(self) -> None:
		self.randomize()
	
	def randomize(self):
		self.x = random.randint(0, celda_numero - 1)
		self.y = random.randint(0, celda_numero - 1)
                
		self.pos = Vector2(self.x , self.y)

	def crear_obstaculo(self, tipo):
		x_pos = int(self.pos.x * celda_tamanio)
		y_pos = int(self.pos.y * celda_tamanio)
		obstaculo_rect = pygame.Rect(x_pos, y_pos , celda_tamanio, celda_tamanio)
		pantalla.blit(tipo, obstaculo_rect)

class MAIN:
	def __init__(self) -> None:
		#Creo un OBJETO 'snake' y otro OBJETO 'fruta' de la clase que le corresponde...
		self.snake = SNAKE()
		self.fruta = FRUTA()
		self.obstaculo = OBSTACULO()

	def update(self):
		self.snake.movimiento_snake()
		self.colision()
		self.check_falla()
		#self.snake.sonar_musica()
	
	def crear_elementos(self):
		self.fruta.crear_fruta()
		self.snake.crear_snake()
		self.obstaculo.crear_obstaculo(arbol)
		self.crear_score()
	
	def colision(self):
		if self.snake.cuerpo[0] == self.fruta.pos:
			#print("Comio")
			self.fruta.randomize()
			self.snake.agregar_bloque()
			self.snake.sonar_comida()
		
		for bloque in self.snake.cuerpo[1:]:
			if bloque == self.fruta.pos:
				self.fruta.randomize()
		#Si un elemento de la serpiente esta en la misma posicion de la fruta, hago que se genere nuevamente la fruta en otra posicion.
	
	def check_falla(self):
		if not 0 <= self.snake.cuerpo[0].x < celda_numero or not 0 <= self.snake.cuerpo[0].y < celda_numero:
			self.game_over()
		
		for bloque in self.snake.cuerpo[1:]:
			if bloque == self.snake.cuerpo[0]:
				self.game_over()
		
		if self.snake.cuerpo[0] == self.obstaculo.pos:
			self.snake.sonar_choque()

		if self.snake.cuerpo[1] == self.obstaculo.pos:
			self.game_over()
		
	
	def game_over(self):
		pygame.quit()
		sys.exit()

	def crear_score(self):
		texto_score = str(len(self.snake.cuerpo) - 3)
		#El largo del snake determina la cantidad de puntos. Por defecto, al comenzar con 3 elementos, se lo resto.
		texto_del_score = fuente.render("Score: ", True, (colores.NEGRO))
		superficie_score = fuente.render(texto_score, True, (colores.NEGRO))
		#El 'antialias' (segundo parametro) siempre es True. Sirve para que los bordes no se vean pixeleados.
		score_x_pos = int(celda_tamanio * celda_numero - 60)
		score_y_pos = int(celda_tamanio * celda_numero - 650)
		score_rect = superficie_score.get_rect(center = (score_x_pos, score_y_pos))
		texto_del_score_rect = texto_del_score.get_rect(midright = (score_rect.left, score_rect.centery))
		fondo_rect = pygame.Rect(texto_del_score_rect.left, texto_del_score_rect.top, texto_del_score_rect.width + score_rect.width + 5, texto_del_score_rect.height)

		pygame.draw.rect(pantalla, (colores.DORADO), fondo_rect)
		pantalla.blit(superficie_score, score_rect)
		pantalla.blit(texto_del_score, texto_del_score_rect)
		pygame.draw.rect(pantalla, (colores.AMARILLO), fondo_rect, 2)
		#Borde del rectangulo del Score.

		return texto_score


pygame.mixer.pre_init(44100,-16,2,512)
#Se utiliza para que no haya un delay en el momento de emitir un sonido.

pygame.init()
celda_tamanio = 35
celda_numero = 20

pantalla = pygame.display.set_mode((celda_tamanio * celda_numero, celda_tamanio * celda_numero))
pygame.display.set_caption("Snake Game")

#Imagenes
imagen_fondo_pos = (240,200)

manzana = pygame.image.load("Imagenes/manzana.png").convert_alpha()
#El metodo 'converte_alpha' convierte la imagen en un formato con el que pygame pueda trabajar mas facilmente.
manzana = pygame.transform.scale(manzana, (30, 30))
#Transformo la escala de mi imagen

arbol = pygame.image.load("Imagenes/arbol.png").convert_alpha()
arbol = pygame.transform.scale(arbol, (35,35))

boom = pygame.image.load("Imagenes/boom.png").convert_alpha()
boom = pygame.transform.scale(boom, (35,35))

perro = pygame.image.load("Imagenes/perro.png").convert_alpha()
perro = pygame.transform.scale(perro, (40, 40))

imagen_snake = pygame.image.load("Imagenes/fondo.png").convert_alpha()
imagen_snake = pygame.transform.scale(imagen_snake, (250, 300))

imagen_cobra = pygame.image.load("Imagenes/fondo_2.png").convert_alpha()
imagen_cobra = pygame.transform.scale(imagen_cobra, (300, 300))

imagen_voldemort = pygame.image.load("Imagenes/fondo_3.png").convert_alpha()
imagen_voldemort = pygame.transform.scale(imagen_voldemort, (500, 300))

start_imagen = pygame.image.load("Imagenes/start.png").convert_alpha()
exit_imagen = pygame.image.load("Imagenes/exit.png").convert_alpha()

#Creo instancia del boton
start_boton = botones.Boton(200, 300, start_imagen)
exit_boton = botones.Boton(400, 300, exit_imagen)


#Texto
fuente = pygame.font.SysFont("Helvetica" , 30)

'''
PARA MOVERME A LA IZQ o ARRIBA tengo que disminuir 'x' e 'y' respectivamente.
PARA MOVERME A LA DERECHA o ABAJO tengo que aumentar 'x' e 'y' respectivamente.
'''

#SCREEN_UPDATE = pygame.USEREVENT
#pygame.time.set_timer(SCREEN_UPDATE, 150)
#Creo una 'actualizacion de la pantalla' con un evento personalizado (USEREVENT).
#Luego con el time, le indico c/ cuanto quiero activarlo (150 milisegundos).
tiempo = pygame.time.Clock()

juego_principal = MAIN()

running = True
while running:
	#Musica principal
	#musica = pygame.mixer.music.load("Sonidos/In The Canime.mp3")
	#pygame.mixer.music.play(-1)
	#(-1) es para que se repita la musica en loop.

	#esta_jugando = True
	esta_en_intro = True

	#PANTALLA INTRO
	while esta_en_intro:
		tiempo.tick(5)
		#CIERRE DE PANTALLA
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False 
		pantalla.fill(colores.NEGRO)

		titulo = fuente.render("SNAKE GAME", True, colores.CELESTE)
		instrucciones = fuente.render("Presione ENTER para JUGAR", True, colores.AZUL)
		pantalla.blit(titulo, (250, 200))
		pantalla.blit(instrucciones, (150, 300))

		tecla = pygame.key.get_pressed()

		if tecla[pygame.K_a]:
			esta_en_intro = False
			esta_jugando = True
		
		pygame.display.update()

	while esta_jugando:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				esta_jugando = False
				running = False

			#if event.type == SCREEN_UPDATE:
			#	juego_principal.update()
			
			#tecla = pygame.key.get_pressed()
			pantalla.fill((colores.BLANCO))
			pantalla.blit(imagen_snake, imagen_fondo_pos)

			puntaje = juego_principal.crear_score()
			puntaje = int(puntaje)

			if puntaje < 3:
				tiempo.tick(5)
				juego_principal.update()
			elif puntaje < 10:
				tiempo.tick(8)
				juego_principal.update()
			else:
				tiempo.tick(14)
				juego_principal.update()

			juego_principal.crear_elementos()

			if event.type == pygame.KEYDOWN:
				#if tecla[pygame.K_UP]:
				if event.key == pygame.K_UP:
					if juego_principal.snake.direccion.y != 1:
						juego_principal.snake.direccion = Vector2(0, -1)
				if event.key == pygame.K_RIGHT:
					if juego_principal.snake.direccion.x != -1:
						juego_principal.snake.direccion = Vector2(1, 0)
				if event.key == pygame.K_LEFT:
					if juego_principal.snake.direccion.x != 1:
						juego_principal.snake.direccion = Vector2(-1, 0)
				if event.key == pygame.K_DOWN:
					if juego_principal.snake.direccion.y != -1:
						juego_principal.snake.direccion = Vector2(0, 1)
			
	pygame.display.update()
	#Actualizo la pantalla.

	

pygame.quit()

'''CREAR MENU DE INICIO
	if start_boton.crear_botones(pantalla):
    	#print("START")
		pass
	if exit_boton.crear_botones(pantalla):
		running = False
'''