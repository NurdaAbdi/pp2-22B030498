import pygame

pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("ПРИКОЛ")
myfont = pygame.font.Font('Roboto-Black.ttf', 40)
text_surface = myfont.render('Anime one love', True, 'Yellow')
run = True
while(run):
    screen.blit(text_surface, (200,200))
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
pygame.quit()
