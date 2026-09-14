#!/usr/bin/env python3
import pygame
import signal

running = True
def handler(signum, frame):
    global running
    print("CTRL+C received...")
    running = False
    exit(0) 

signal.signal(signal.SIGINT, handler)

WIDTH = 400
HEIGHT = 560
window = (WIDTH, HEIGHT)
TITLE = 'Candy Crush'
screen = pygame.display.set_mode(window)

background = pygame.Surface(window)

def draw():
    screen.blit(background, (0,0))

def loop():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        

pygame.display.flip()
if __name__ == "__main__":
    loop()
    pygame.quit()
