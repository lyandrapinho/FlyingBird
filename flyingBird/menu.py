import pygame
from flyingBird.background import Background
from flyingBird.const import C_RED, C_GRAY

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.background = Background(width, height, mode="menu")
        self.font_title  = pygame.font.SysFont("Arial", 40, bold=True)
        self.font_option = pygame.font.SysFont("Arial", 24)
        self.options = ["Start", "How to Play", "Exit"]
        self.selected = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected].lower()
        return None

    def draw(self):
        self.background.draw(self.screen)
        # Title
        title = self.font_title.render("Flying Bird", True, C_RED)
        self.screen.blit(title, title.get_rect(center=(self.width // 2, 80)))
        # Menu options
        for i, text in enumerate(self.options):
            color = C_RED if i == self.selected else C_GRAY
            label = self.font_option.render(text, True, color)
            self.screen.blit(label, label.get_rect(center=(self.width // 2, 160 + i * 50)))
