import pygame
import os
from flyingBird.const import LAYER_SPEEDS

ASSET_PATH = os.path.join(os.path.dirname(__file__), '..', 'asset')

class Background:
    def __init__(self, width, height, mode="menu"):
        # mode='menu' = static background
        # mode='game' = parallax scrolling
        self.width = width
        self.height = height
        self.mode = mode
        self.layers = []

        if mode == "menu":
            self._load_menu()
        else:
            self._load_game()

    def _load_image(self, filename):
        path = os.path.join(ASSET_PATH, filename)
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (self.width, self.height))

    def _load_menu(self):
        surface = self._load_image("MenuBg.png")
        self.layers.append([surface, 0, self.width, 0])

    def _load_game(self):
        # Two copies of each layer placed side by side for infinite scrolling
        for i, speed in enumerate(LAYER_SPEEDS):
            surface = self._load_image(f"LevelBg{i}.png")
            self.layers.append([surface, 0, self.width, speed])

    def update(self):
        if self.mode == "menu":
            return
        for layer in self.layers:
            layer[1] -= layer[3]
            layer[2] -= layer[3]

            # Reposition a copy that has scrolled off-screen
            if layer[1] + self.width <= 0:
                layer[1] = layer[2] + self.width
            if layer[2] + self.width <= 0:
                layer[2] = layer[1] + self.width

    def draw(self, screen):
        for layer in self.layers:
            screen.blit(layer[0], (layer[1], 0))
            screen.blit(layer[0], (layer[2], 0))
