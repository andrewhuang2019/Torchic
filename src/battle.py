import pygame
from pygame.locals import *
from button import Button
from screen import Screen

blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.battle_screen = Screen("Battle")

        self.button1 = Button(340, 450, 200, 50, "FIGHT", blue, green)
        self.button2 = Button(565, 450, 200, 50, "PKMN", blue, green)
        self.button3 = Button(340, 525, 200, 50, "ITEM", blue, green)
        self.button4 = Button(565, 525, 200, 50, "RUN", blue, green)

        self.fight_box_border = pygame.Rect(10, 430, 780, 165)        
        self.fight_box = pygame.Rect(20, 440, 760, 145)

        self.back_button = Button(12, 12, 50, 50, "B", blue, green)

        #Pokemon images
        self.scale_factor1 = 8
        self.scale_factor2 = 5

        self.pokemon1_image_path = "assets/sprites/back/" + pokemon1.get_name() + ".png"
        self.pokemon1_image = pygame.image.load(self.pokemon1_image_path)

        self.pokemon2_image_path = "assets/sprites/front/" + pokemon2.get_name() + ".png"
        self.pokemon2_image = pygame.image.load(self.pokemon2_image_path)

        self.pokemon1_width = self.pokemon1_image.get_width()
        self.pokemon1_height = self.pokemon1_image.get_height()

        self.scaled_width1 = int(self.pokemon1_width * self.scale_factor1)
        self.scaled_height1 = int(self.pokemon1_height * self.scale_factor1)

        self.scaled_width2 = int(self.pokemon1_width * self.scale_factor2)
        self.scaled_height2 = int(self.pokemon1_height * self.scale_factor2)

        self.pokemon1_image = pygame.transform.scale(self.pokemon1_image, (self.scaled_width1, self.scaled_height1))
        self.pokemon2_image = pygame.transform.scale(self.pokemon2_image, (self.scaled_width2, self.scaled_height2))

        #Pokemon health
        self.pokemon1_health = pygame.Rect(514, 314, 190, 8)
        self.pokemon1_health_background = pygame.Rect(510, 310, 198, 16)
        
        self.pokemon2_health = pygame.Rect(134, 64, 190, 8)
        self.pokemon2_health_background = pygame.Rect(130, 60, 198, 16)


    def use_move(self, move):
        pass

    def display_screen(self):
        self.battle_screen.check_update((255,255,255))
        self.battle_screen.screen_update()

        self.battle_screen.screen.blit(self.pokemon1_image, (50, 200))
        self.battle_screen.screen.blit(self.pokemon2_image, (525, 75))

        pygame.draw.rect(self.battle_screen.screen, black, self.fight_box_border)
        pygame.draw.rect(self.battle_screen.screen, white, self.fight_box)

        pygame.draw.rect(self.battle_screen.screen, black, self.pokemon1_health_background)
        pygame.draw.rect(self.battle_screen.screen, white, self.pokemon1_health)

        pygame.draw.rect(self.battle_screen.screen, black, self.pokemon2_health_background)
        pygame.draw.rect(self.battle_screen.screen, white, self.pokemon2_health)

        self.button1.draw(self.battle_screen.screen)
        self.button2.draw(self.battle_screen.screen)
        self.button3.draw(self.battle_screen.screen)
        self.button4.draw(self.battle_screen.screen)
        self.back_button.draw(self.battle_screen.screen)

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


