import pygame
from pygame.sprite import Sprite


class Player(object):
	def __init__(self, screen, image, start_x, start_y):
		self.image = pygame.image.load(image)
		# Resize the image
		self.image = pygame.transform.scale(self.image,(207,250))
		self.x = start_x
		self.y = start_y
		self.speed = 10
		self.screen = screen
		self.should_move_up = False
		self.should_move_down = False
		self.should_move_left = False
		self.should_move_right = False
		self.rect = self.image.get_rect()
		self.rect.left = self.x
		self.rect.top = self.y

	def draw_me(self):
		if(self.should_move_up):
			self.y -= self.speed
		elif(self.should_move_down):
			self.y += self.speed
		elif(self.should_move_left):
			self.x -= self.speed
		elif(self.should_move_right):
			self.x += self.speed

		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.image, [self.x, self.y])

		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.image, [self.x, self.y])

	def should_move(self, direction, true_or_false):
		if direction == "up":
			self.should_move_up = true_or_false
		if direction == "down":
			self.should_move_down = true_or_false
		if direction == "left":
			self.should_move_left = true_or_false
		if direction == "right":
			self.should_move_right = true_or_false