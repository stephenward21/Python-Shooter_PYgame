# The reason you have access to this model is because you ran $ pip install pygame
# Pygame is not part of core (like math or random)
import pygame
from shooter import Player
from game_functions import check_events
from enemies import Enemy
from pygame.sprite import Group, groupcollide



# the core functionality/loop
def run_game():
	# Init all the pygame stuff
	pygame.init()
	# set up a tuple for a screen size (horizontal, vertical)
	screen_size = (1000,800)
	# tuple for background color (R, G, B)
	background_color = (82,111,53)
	# create a pygame to us
	screen = pygame.display.set_mode(screen_size)
	# set a caption on the terminal window
	pygame.display.set_caption("3rd Person Shooter")


	the_shooter = Player(screen, './images/Hero.png', 100, 100)
	the_shooter_group = Group()
	the_shooter_group.add(the_shooter)
	bad_guy = Enemy(screen)
	enemies = Group()
	enemies.add(bad_guy)
	bullets = Group()

	tick = 0


	# Main game loop run forever...(or until break)
	# could also use Boolean instead of 1...
	while 1:
		tick += 1
		if tick % 40 == 0:
			enemies.add(Enemy(screen))

		screen.fill(background_color)
		check_events(the_shooter, screen, bullets)

		# Draw the shooter
		for shooter in the_player_group:
			the_shooter.draw_me()


		for bad_gu in enemies:
			bad_guy.update_me(the_shooter)
			bad_guy.draw_me()

		hero_died = groupcollide(the_shooter_group, enemies, True, False)
		bullet_hit = groupcollide(bullets,enemies,True,True)
		print bullet_hit

		# clear the screen for the next time throught the loop					
		pygame.display.flip()

# Start the Game!
run_game()