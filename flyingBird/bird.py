import pygame
import os
from flyingBird.const import BIRD_WIDTH, BIRD_HEIGHT, BIRD_GRAVITY, BIRD_JUMP_STRENGTH, BIRD_ANIMATION_SPEED

ASSET_PATH = os.path.join(os.path.dirname(__file__), '..', 'asset')

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = BIRD_GRAVITY
        self.jump_strength = BIRD_JUMP_STRENGTH
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.frames = self._load_frames()
        self.current_frame = 0
        self.animation_speed = BIRD_ANIMATION_SPEED
        self.animation_counter = 0

    def _load_frames(self):
        frames = []
        for i in range(6):
            path = os.path.join(ASSET_PATH, f"Player{i}.png")
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, (self.width, self.height))
            frames.append(image)
        return frames

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.velocity = self.jump_strength

    def update(self):
        # Apply gravity each frame
        self.velocity += self.gravity
        self.y += self.velocity
        # Advance animation frame
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self, screen):
        angle = -self.velocity * 3
        angle = max(-40, min(angle, 90))
        rotated = pygame.transform.rotate(self.frames[self.current_frame], angle)
        rect = rotated.get_rect(center=(self.x + self.width // 2, int(self.y) + self.height // 2))
        screen.blit(rotated, rect)

    def get_rect(self):
        return pygame.Rect(self.x, int(self.y), self.width, self.height)
