import os
import pygame
from flyingBird.menu import Menu
from flyingBird.game import Game
from flyingBird.howtoplay import HowToPlay
from flyingBird.const import WIN_WIDTH, WIN_HEIGHT, MUSIC_VOLUME

pygame.init()
pygame.mixer.init()

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ASSET_PATH = os.path.join(BASE_PATH, 'asset')

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flying Bird")
clock = pygame.time.Clock()

def play_music(filename):
    path = os.path.join(ASSET_PATH, filename)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(MUSIC_VOLUME)
    pygame.mixer.music.play(-1)

# Game states: "menu", "playing", "howtoplay"
state = "menu"
menu = Menu(screen, WIN_WIDTH, WIN_HEIGHT)
howtoplay = HowToPlay(screen, WIN_WIDTH, WIN_HEIGHT)
game = None
high_score = 0

play_music("Menu.mp3")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            action = menu.handle_event(event)
            if action == "start":
                game = Game(screen, WIN_WIDTH, WIN_HEIGHT)
                state = "playing"
                play_music("Game.mp3")
            elif action == "how to play":
                state = "howtoplay"
            elif action == "exit":
                running = False

        elif state == "playing":
            game.handle_event(event)

        elif state == "howtoplay":
            action = howtoplay.handle_event(event)
            if action == "menu":
                state = "menu"

    # Draw based on current state
    if state == "menu":
        menu.draw()

    elif state == "playing":
        game.update()
        game.draw()
        if game.is_over():
            high_score = max(high_score, game.score)
            state = "menu"
            play_music("Menu.mp3")

    elif state == "howtoplay":
        howtoplay.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.quit()
