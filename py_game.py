import pygame
import random
import time
from msvcrt import getch


pygame.init()

s_breadth = 600
s_height = 600

black = (0,0,0)
white = (255,255,255) #basic color configurations
red = (255,0,0)
purp = (61, 21, 87)
pink = (223, 103, 140)
green = (0, 128, 0)



def msg(words, num=90, s_breadth=300, s_height=300):
    warning = pygame.font.Font('freesansbold.ttf',num)
    surface = warning.render(words, True, black)
    rectangle = surface.get_rect()
    rectangle.center = ((s_breadth),(s_height))
    game_screen.blit(surface, rectangle)
    pygame.display.update()
    pygame.time.wait(3000)


game_screen = pygame.display.set_mode((s_breadth,s_height))
pygame.display.set_caption('raftaar')
fps = pygame.time.Clock()
tesla_is_awesome = pygame.image.load('car.jpg')
car_width = tesla_is_awesome.get_rect().size
car_width = car_width[0]
t = pygame.font.Font('freesansbold.ttf', 12)



obstacle_x =obstacle_y = obstacle_width = obstacle_height = obstacle_move = 4

def initial():
	global obstacle_x ,obstacle_y , obstacle_width , obstacle_height , obstacle_move
	obstacle_x = random.randrange(0, s_breadth)
	obstacle_y = -40
	obstacle_width = 150
	obstacle_height = 150
	ostacle_speed = 9

times = 0

maxi = 0
    
def main():
	global maxi
	score = 0
	x = 481
	y = 481
	var_move = 0
	
	initial()

	global obstacle_x ,obstacle_y , obstacle_width , obstacle_height , obstacle_move, times


	bombard = False
	m = 0


	times = times + 1


	if times == 4:
		game_screen.fill(purp)
		msg('you exceeded your number of tries', 34)
		msg('your score is'+str(maxi), 34, 300, 400)
		pygame.quit()

	while not bombard:

		g = 0

		# keye = ord(getch())

		# print(x, var_move)


		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #now this condition is kept because pygame.KEYUP
				#means when key button is released, now one might argue that why don't you just remove this condition?, even
				#well if we release a key nothing will happen
				#well i started off by not putting this condition and guess what? evrytime i pressed an arrow key, after release
				#car started to move left by certain speed , i dunno why that happened but it happened , hence it became a necessity to keep the condition for key release
					var_move = 0



			if event.type == pygame.KEYDOWN:



				if event.key == pygame.K_LEFT:    #if basic arrow keys are pressed....
					var_move = -3

				elif event.key == pygame.K_RIGHT:
					var_move = 3





		x += var_move
		game_screen.fill(purp)

		score_text = t.render("Score: {}".format(score), True, pink)
		game_screen.blit(score_text, (20, 20))


		pygame.draw.rect(game_screen, pink, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])#the obstacle generation
		obstacle_y += obstacle_move
		game_screen.blit(tesla_is_awesome,(x,y))
    
		if x > s_breadth - car_width or x < 0:
			msg('shit happens')
			main()
		

		if y <= obstacle_y+obstacle_height:

			if x > obstacle_x and x < obstacle_x + obstacle_width or x+car_width > obstacle_x and x + car_width < obstacle_x+obstacle_width:
				msg('shit happens')
				main()

		if obstacle_y > s_height:
			score = score + 1
			obstacle_y = -200
			obstacle_x = random.randrange(obstacle_width/2,s_breadth-obstacle_width/2)

		maxi = max(maxi, score)


		pygame.display.update()
		fps.tick(60) 



main()
pygame.quit()
quit()
