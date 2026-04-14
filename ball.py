import pygame
from constants import BALL_RADIUS, LINE_WIDTH
from circleshape import CircleShape


class Ball(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    