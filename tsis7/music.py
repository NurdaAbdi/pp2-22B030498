import pygame

pygame.init()

song_list = ["saveyourtears.mp3" , "onerightnow.mp3" ]

song_names = ["saveyourtears" , "onerightnow" ]
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('2 musics')

font = pygame.font.SysFont('sf', 24)
clock = pygame.time.Clock()
running = True

index = 0
pygame.mixer.music.load(song_list[index])
pygame.mixer.music.play()
song_name = song_names[index]
text1 = font.render("1-save your tears", True , ('red'))
text2 = font.render("2-one right now", True , ('blue'))
text3 = font.render("Currently playing:  " + song_name, True, ('green'))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        index -= 1
        pygame.mixer.music.load(song_list[index])
        song_name = song_names[index]
        pygame.mixer.music.play()
    if pressed[pygame.K_LCTRL]: pygame.mixer.music.play()
    if pressed[pygame.K_SPACE]: pygame.mixer.music.stop()
    if pressed[pygame.K_UP]: pygame.mixer.music.pause()
    if pressed[pygame.K_DOWN]: pygame.mixer.music.unpause()
    if pressed[pygame.K_RIGHT]: 
        index += 1
        pygame.mixer.music.load(song_list[index])
        song_name = song_names[index]
        text3 = font.render("Currently playing:  " + song_name, True, ('purple'))
        pygame.mixer.music.play()
    if index == len(song_list) - 1:
        index = -1


    screen.fill((255, 255, 255))
    screen.blit(text1, (22,100))
    screen.blit(text2, (22,150))
    screen.blit(text3, (22, 440))
    pygame.display.flip()
    clock.tick(5.75)