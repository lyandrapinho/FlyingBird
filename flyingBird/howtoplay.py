import pygame
from flyingBird.background import Background
from flyingBird.const import C_RED, C_BLACK


class HowToPlay:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.background = Background(width, height, mode="menu")

        self.font_title = pygame.font.SysFont("Arial", 28, bold=True)
        self.font_subtitle = pygame.font.SysFont("Arial", 16, bold=True)
        self.font_text = pygame.font.SysFont("Arial", 15)
        self.font_back = pygame.font.SysFont("Arial", 14)

        self.instructions = [
            ("CONTROLS",           "subtitle"),
            ("",                   "space"),
            ("SPACE",              "title"),
            ("Makes the bird fly up",  "text"),
            ("Release to fall down",   "text"),
            ("",                   "space"),
            ("SURVIVE",            "subtitle"),
            ("",                   "space"),
            ("Avoid the pipes",    "text"),
            ("Don't touch the edges",  "text"),
            ("The further you go, the higher your score!",    "text"),
        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_BACKSPACE, pygame.K_ESCAPE):
                return "menu"
        return None

    def draw(self):
        self.background.draw(self.screen)

        # Title
        title = self.font_title.render("How to Play", True, C_RED)
        self.screen.blit(title, title.get_rect(center=(self.width // 2, 25)))

        # Top separator
        pygame.draw.line(self.screen, C_RED,
                         (self.width // 2 - 100, 45),
                         (self.width // 2 + 100, 45), 2)

        # Instruction lines
        y = 62
        for text, kind in self.instructions:
            if kind == "space":
                y += 8
                continue
            elif kind == "subtitle":
                surf = self.font_subtitle.render(text, True, C_RED)
                y += 4
            elif kind == "title":
                surf = self.font_title.render(text, True, C_RED)
            else:
                surf = self.font_text.render(text, True, C_BLACK)

            self.screen.blit(surf, surf.get_rect(center=(self.width // 2, y)))
            y += surf.get_height() + 4

        # Bottom separator
        pygame.draw.line(self.screen, C_RED,
                         (self.width // 2 - 100, self.height - 35),
                         (self.width // 2 + 100, self.height - 35), 2)

        # Return hint
        back = self.font_back.render("Press BACKSPACE or ESC to return", True, C_RED)
        self.screen.blit(back, back.get_rect(center=(self.width // 2, self.height - 20)))
