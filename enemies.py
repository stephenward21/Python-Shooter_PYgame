import pygame
from pygame.sprite import Sprite
from math import hypot

class Enemy(Sprite):
	def __init__(self, screen, tick = 0):
		super(Enemy,self).__init__()
		print tick
		if tick < 35:
			self.image = pygame.image.load('./images/2.png')
		elif tick < 85:
			self.image = pygame.image.load('./images/3.png')
		else:
			self.image = pygame.image.load('./images/monster.png')
		self.image = pygame.image.load('./images/2.png')
		self.speed = 3
		self.x = 1000
		self.y = 400
		self.screen = screen
		self.rect = self.image.get_rect()

	def update_me(self, the_shooter):
		dx = self.x - the_shooter.x
		dy = self.y - the_shooter.y 
		dist = math.hypot(dx, dy)
		dx = dx / dist
		dy = dy / dist
		self.x -= dx * self.speed
		self.y -= dy * self.speed
		# self.rect.left = self.x
		# self.rect.top = self.y


	def draw_me(self):
		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.image,[self.x, self.y]) 
		# self.screen.blit(self.image, [self.x, self.y])