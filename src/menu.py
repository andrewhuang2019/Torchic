import pygame
from pygame.locals import *
from button import Button
from screen import Screen

blue = (0, 0, 255)
green = (0, 255, 0)

class Menu:
    def __init__(self):
        self.menu_screen = Screen("Menu")

        self.fight_button = Button(300, 250, 200, 50, "Enter Battle", blue, green)

    def display_screen(self):
        self.fight_button.draw(self.menu_screen.screen)
        pygame.display.flip()

    def fight_button_is_clicked(self, event):
        return self.fight_button.is_clicked(event)

    def make_current_screen(self):
        self.menu_screen.make_current_screen()
