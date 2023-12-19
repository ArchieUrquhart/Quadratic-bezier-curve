import pygame
import sys

pygame.init()

#colous
white = (255, 255, 255)
black = (0,0,0)

#initialize window 
WIDTH = 1000
HIEGHT = 1000
screen = pygame.display.set_mode((WIDTH, HIEGHT))
title = "quadbezier"
pygame.display.set_caption(title)

clock = pygame.time.Clock()

frameRate = 60

startPos = (0,HIEGHT//2)
endPos = (WIDTH,HIEGHT//2)

points = [startPos, endPos]

def lerp(a, b, t):
	x = a[0] + (b[0]-a[0])*t
	y = a[1] + (b[1]-a[1])*t
	pos = (x,y)
	return pos

def quadBezier(start, point, end, draw):

	for i in range(0,11):
		t = i*0.1

		a = lerp(start,point,t)
		b = lerp(point,end,t)
		dot = lerp(a,b,t)

		pygame.draw.circle(screen,white,dot,5)

		if draw:
			pygame.draw.line(screen, white, a, b)
		

#DRAW 
	screen.fill(black)


	quadBezier(startPos,pygame.mouse.get_pos(),endPos,True)


	clock.tick(frameRate)
	pygame.display.update()

