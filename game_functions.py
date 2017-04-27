import pygame
import sys
from bullet import Bullet




def check_events(the_shooter, screen, bullets):
	# the escape hatch from while loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# the user clicked the red X. Get out of loop and kill game.
				sys.exit()
			elif event.type == pygame.KEYDOWN:
		# 	if event.key == keys['up' or 'down' or 'left' or 'right']:
		# 		return keys_down == True

				if event.key == 273:
					the_shooter.should_move("up", True) 
				
				elif event.key == 274:
					the_shooter.should_move("down", True)
				
				elif event.key == 276:
					the_shooter.should_move("left", True)
				
				elif event.key == 275:
					the_shooter.should_move("right", True)

				elif event.key == 32:
					for direction in range(1,5):
						new_bullet = Bullet(screen, the_shooter, direction)
						bullets.add(new_bullet)
				
			elif event.type == pygame.KEYUP:
				print ("The user let go of a key")
				if event.key == 273:	
					the_shooter.should_move("up", False)
				
				if event.key == 274:
					the_shooter.should_move("down", False) 
				
				if event.key == 276:
					the_shooter.should_move("left", False) 
				
				if event.key == 275:
					the_shooter.should_move("right", False)