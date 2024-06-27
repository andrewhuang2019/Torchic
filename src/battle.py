import pygame
from pygame.locals import *
from button import Button
from screen import Screen

blue = (0, 0, 255)
green = (0, 255, 0)

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.battle_screen = Screen("Battle")

        self.button1 = Button(350, 450, 200, 50, "FIGHT", blue, green)
        self.button2 = Button(575, 450, 200, 50, "PKMN", blue, green)
        self.button3 = Button(350, 525, 200, 50, "ITEM", blue, green)
        self.button4 = Button(575, 525, 200, 50, "RUN", blue, green)

        self.back_button = Button(12, 12, 50, 50, "B", blue, green)

        self.scale_factor = 10

        self.pokemon1_image_path = "assets/sprites/back/" + pokemon1.get_name() + ".png"
        self.pokemon1_image = pygame.image.load(self.pokemon1_image_path)

        self.pokemon1_width = self.pokemon1_image.get_width()
        self.pokemon1_height = self.pokemon1_image.get_height()

        self.scaled_width = int(self.pokemon1_width * self.scale_factor)
        self.scaled_height = int(self.pokemon1_height * self.scale_factor)

        self.pokemon1_image = pygame.transform.scale(self.pokemon1_image, (self.scaled_width, self.scaled_height))



    def use_move(self, move):
        pass

    def display_screen(self):
        self.battle_screen.check_update((255,255,255))
        self.battle_screen.screen_update()
        self.button1.draw(self.battle_screen.screen)
        self.button2.draw(self.battle_screen.screen)
        self.button3.draw(self.battle_screen.screen)
        self.button4.draw(self.battle_screen.screen)
        self.back_button.draw(self.battle_screen.screen)

        self.battle_screen.screen.blit(self.pokemon1_image, (30, 150))

        pygame.display.flip()

    def button1_is_clicked(self, event):
        return self.button1.is_clicked(event)
    
    def button2_is_clicked(self, event):
        return self.button2.is_clicked(event)
    
    def button3_is_clicked(self, event):
        return self.button3.is_clicked(event)
    
    def button4_is_clicked(self, event):
        return self.button4.is_clicked(event)
    
    def back_button_is_clicked(self, event):
        return self.back_button.is_clicked(event)

    def make_current_screen(self):
        self.battle_screen.make_current_screen()


