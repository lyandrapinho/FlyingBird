import pygame
from flyingBird.bird import Bird
from flyingBird.pipe import Pipe
from flyingBird.background import Background
from flyingBird.const import PIPE_INTERVAL, C_WHITE

class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.background = Background(width, height, mode="game")
        self.bird = Bird(80, height // 2)
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.pipe_interval = PIPE_INTERVAL
        self.frame_count = 0
        self.font = pygame.font.SysFont("Arial", 24, bold=True)

    def handle_event(self, event):
        if not self.game_over:
            self.bird.handle_event(event)

    def update(self):
        if self.game_over:
            return
        self.frame_count += 1
        self.background.update()
        self.bird.update()

        # Spawn a new pipe at regular intervals
        if self.frame_count % self.pipe_interval == 0:
            self.pipes.append(Pipe(self.width, self.height))

        for pipe in self.pipes:
            pipe.update()

        # Remove pipes that have left the screen
        self.pipes = [p for p in self.pipes if not p.is_off_screen()]

        # Score: point awarded when bird passes a pipe
        for pipe in self.pipes:
            if int(pipe.x + pipe.width) == self.bird.x:
                self.score += 1

        # Collision with pipes
        bird_rect = self.bird.get_rect()
        for pipe in self.pipes:
            if pipe.collides_with(bird_rect):
                self.game_over = True

        # Collision with top or bottom edge
        if self.bird.y <= 0 or self.bird.y + self.bird.height >= self.height:
            self.game_over = True

    def draw(self):
        self.background.draw(self.screen)

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.bird.draw(self.screen)

        # Display current score at top center
        score_text = self.font.render(str(self.score), True, C_WHITE)
        self.screen.blit(score_text, score_text.get_rect(center=(self.width // 2, 30)))

    def is_over(self):
        return self.game_over
