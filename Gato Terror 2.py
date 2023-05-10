import pygame

running = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Casa')
px = 0
sol=0

#Song
audio_1up = pygame.mixer.Sound('C:/HTML/Pygame_Gato_Terror/musica.mp3')
audio_2up = pygame.mixer.Sound('C:/HTML/Pygame_Gato_Terror/musica1.mp3')
audio_3up = pygame.mixer.Sound('C:/HTML/Pygame_Gato_Terror/musica2.mp3')

     
    
def load():
    global  minha_imagem1, minha_imagem, minha_imagem2, minha_imagem3, minha_imagem4, minha_imagem5,t,click

    minha_imagem1 = pygame.image.load('C:/HTML/Pygame_Gato_Terror/cat.png')
    minha_imagem1 = pygame.transform.scale(minha_imagem1, (40, 40))
    minha_imagem = pygame.image.load('C:/HTML/Pygame_Gato_Terror/cat.png')
    minha_imagem = pygame.transform.scale(minha_imagem, (100, 100))
    minha_imagem = pygame.transform.rotate(minha_imagem, -20)
    click = minha_imagem.get_rect(center=(360, 120))
   #Texto 

    font = pygame.font.Font('C:/HTML/Pygame_Gato_Terror/SedgwickAveDisplay-Regular.ttf', 18)
    t = font.render("Clique no Gato para salva-lo! ", False, (0, 255, 0))
    minha_imagem5 = pygame.image.load('C:/HTML/Pygame_Gato_Terror/bruxa.png')
    minha_imagem5 = pygame.transform.scale(minha_imagem5, (120, 50))
    minha_imagem4 = pygame.image.load('C:/HTML/Pygame_Gato_Terror/terror.jpg')
    minha_imagem4 = pygame.transform.scale(minha_imagem4, (820, 650))
    minha_imagem2 = pygame.image.load('C:/HTML/Pygame_Gato_Terror/fantasma.jpg')
    minha_imagem2 = pygame.transform.scale(minha_imagem2, (880, 650))

load() 


def draw():

    global click3,click4,px,sol

 #Casa
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
    click4=pygame.draw.circle(screen, (255,255,255), (720, sol), 80)
    pygame.mixer.Sound.play(audio_1up)
    if sol>50 and sol<100:
        pygame.mixer.Sound.stop(audio_1up)
        pygame.draw.rect(screen, (5, 194, 252), (0, 0, 800, 600))
        pygame.draw.circle(screen, (252,237,0), (720, sol), 80)
        pygame.mixer.Sound.play(audio_2up)
    elif sol>100 and sol<150:
        pygame.mixer.Sound.stop(audio_2up)
        pygame.draw.rect(screen, (69, 104, 249), (0, 0, 800, 600))
        pygame.draw.circle(screen, (252,237,0), (720, sol), 80)
        pygame.mixer.Sound.play(audio_3up)
    elif sol>150:   
        pygame.mixer.Sound.stop(audio_3up)
        pygame.draw.rect(screen, (233, 185, 71), (0, 0, 800, 600)) 
        pygame.draw.circle(screen, (252,237,0), (720, sol), 80)   
    
    pygame.draw.rect(screen, (11, 82, 22), (0, 300, 800, 300))
    pygame.draw.rect(screen, (85, 75, 45), (50, 200, 400, 200))
    pygame.draw.rect(screen, (95, 50, 20), (600, 250, 50, 250))
    pygame.draw.rect(screen, (135, 25, 23), (340, 240, 80, 160))
    pygame.draw.circle(screen, (0, 0, 0), (350, 320), 6)

    #Janela
    click3 = pygame.draw.rect(screen, (145, 236, 237), (60, 220, 200, 50))
    pygame.draw.rect(screen, (145, 236, 237), (60, 300, 200, 50))
    pygame.draw.rect(screen, (0, 0, 0), (60, 220, 200, 5))
    pygame.draw.rect(screen, (0, 0, 0), (60, 270, 200, 5))
    pygame.draw.rect(screen, (0, 0, 0), (60, 220, 5, 50))
    pygame.draw.rect(screen, (0, 0, 0), (260, 220, 5, 55))
    pygame.draw.rect(screen, (0, 0, 0), (160, 220, 5, 55))

    pygame.draw.rect(screen, (0, 0, 0), (60, 300, 200, 5))
    pygame.draw.rect(screen, (0, 0, 0), (60, 350, 200, 5))
    pygame.draw.rect(screen, (0, 0, 0), (60, 300, 5, 50))
    pygame.draw.rect(screen, (0, 0, 0), (260, 300, 5, 55))
    pygame.draw.rect(screen, (0, 0, 0), (160, 300, 5, 55))

    #Telhado
    pygame.draw.polygon(screen, (71, 4, 4), [(50, 200), (450, 200),
                                             (230, 150)])

    #Arvore
    pygame.draw.rect(screen, (95, 50, 20), (600, 350, 50, 200))
    pygame.draw.circle(screen, (0, 66, 54), (620, 300), 80)

    #Escada
    pygame.draw.rect(screen, (0, 0, 0), (430, 220, 10, 200))
    pygame.draw.rect(screen, (0, 0, 0), (470, 220, 10, 200))
    pygame.draw.rect(screen, (0, 0, 0), (430, 300, 40, 10))
    pygame.draw.rect(screen, (0, 0, 0), (430, 340, 40, 10))
    pygame.draw.rect(screen, (0, 0, 0), (430, 380, 40, 10))
    pygame.draw.rect(screen, (0, 0, 0), (430, 260, 40, 10))

    #Nuvem
    pygame.draw.circle(screen, (255, 255, 255), (440 + px, 60), 30)
    pygame.draw.circle(screen, (255, 255, 255), (480 + px, 60), 30)
    pygame.draw.circle(screen, (255, 255, 255), (520 + px, 60), 30)



while running:
    draw()
    screen.blit(t, t.get_rect(top=30, left=50))
    screen.blit(minha_imagem1, (10, 20))
    screen.blit(minha_imagem, (320, 80))
    dt=1
    px-=0.3*dt
    if px <-420: 	
        px = screen.get_width()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:		
        sol = sol - (0.1 * dt)
        if sol<0:
            sol=10

       
    if keys[pygame.K_DOWN]:		
        sol = sol + (0.1 * dt) 
        if sol>220:
            sol=0



    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:


            mouse_pos = pygame.mouse.get_pos()
            sol= min(mouse_pos[1],100)

            if click.collidepoint(pygame.mouse.get_pos()):
                for d in range(200):
                    screen.blit(minha_imagem2, (0, 0))
                    pygame.time.wait(8)
                    pygame.display.update()

            if click3.collidepoint(pygame.mouse.get_pos()):
                for d in range(200):
                    screen.blit(minha_imagem4, (0, 0))
                    pygame.time.wait(4)
                    pygame.display.update()
            if click4.collidepoint(pygame.mouse.get_pos()):
                for d in range(200):
                    screen.blit(minha_imagem5, (650, 80))
                    pygame.time.wait(4)
                    pygame.display.update()
    pygame.display.update()
pygame.quit()


