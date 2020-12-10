# encoding: utf-8
import os
import sys

import pygame


def terminate():
    pygame.quit()
    sys.exit()


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.running = True

        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    def render(self):
        """ rendering everything """
        pass

    def main_loop(self):
        """ main program cycle """
        while self.running:
            self.screen.fill((0, 0, 0))
            self.render()
            self.handle_events()

    def text(self, color='white', what='', pos=(0, 0), zal=1):
        intro_text = what
        font = pygame.font.Font(None, 34)
        if zal == 0:
            string_rendered = font.render(intro_text, True, pygame.Color('white'))
        else:
            string_rendered = font.render(intro_text, True, pygame.Color(color))
        intro_rect = string_rendered.get_rect()
        text_w = string_rendered.get_width()
        text_h = string_rendered.get_height()
        intro_rect.y = pos[1]
        intro_rect.x = pos[0]
        pygame.draw.rect(self.screen, pygame.Color(color),
                         (intro_rect.x - 10, intro_rect.y - 10, text_w + 20, text_h + 20), zal)
        self.screen.blit(string_rendered, intro_rect)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((1920, 1080))
    game = Main(screen)
