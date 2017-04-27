import pygame
import sys

def check_events():
	# the escape hatch from while loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# the user clicked the red X. Get out of loop and kill game.
				sys.exit()