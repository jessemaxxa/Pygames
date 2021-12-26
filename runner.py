import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/Sky.png')
Ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Green')

snail_surface = pygame.image.load('graphics/snail1.png')
snail_x_pos = 800

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky_surface,(0,0))
	screen.blit(Ground_surface,(0,300))
	screen.blit(text_surface, ((300,50)))
	snail_x_pos -= 4
	if snail_x_pos < 0:
		snail_x_pos = 800
	screen.blit(snail_surface,(snail_x_pos,255))
	

	pygame.display.update()
	clock.tick(60)
		
	
	
	