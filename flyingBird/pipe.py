import pygame
import random
import os
from flyingBird.const import PIPE_WIDTH, PIPE_SPEED, PIPE_GAP

ASSET_PATH = os.path.join(os.path.dirname(__file__), '..', 'asset')

class Pipe:
    def __init__(self, x, screen_height):
        self.x = x
        self.screen_height = screen_height
        self.width = PIPE_WIDTH
        self.speed = PIPE_SPEED
        self.gap = PIPE_GAP

        # Random vertical position for the gap opening
        self.gap_y = random.randint(60, screen_height - 60 - self.gap)

        self.image_top = self._load_image("PipeTop.png")
        self.image_bottom = self._load_image("PipeBottom.png")

    def _load_image(self, filename):
        path = os.path.join(ASSET_PATH, filename)
        return pygame.image.load(path).convert_alpha()

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        top_rect = self.top_rect()
        bottom_rect = self.bottom_rect()

        # Scale images to fit their respective rects
        top_scaled = pygame.transform.scale(self.image_top, (top_rect.width, top_rect.height))
        bottom_scaled = pygame.transform.scale(self.image_bottom, (bottom_rect.width, bottom_rect.height))

        screen.blit(top_scaled, top_rect.topleft)
        screen.blit(bottom_scaled, bottom_rect.topleft)

    def top_rect(self):
        return pygame.Rect(self.x, 0, self.width, self.gap_y)

    def bottom_rect(self):
        bottom_y = self.gap_y + self.gap
        return pygame.Rect(self.x, bottom_y, self.width, self.screen_height - bottom_y)

    def is_off_screen(self):
        return self.x + self.width < 0

    def collides_with(self, bird_rect):
        return self.top_rect().colliderect(bird_rect) or \
               self.bottom_rect().colliderect(bird_rect)
