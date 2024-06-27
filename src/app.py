import pygame
from pygame.locals import *

from button import Button
from battle import Battle
from screen import Screen
from menu import Menu
from pokemon_manager import PokemonManager
from pokemon import Pokemon

blue = (0, 0, 255)
green = (0, 255, 0)

class App:
    def __init__(self):
        pygame.init()
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 600

        self.battle = Battle()
        self.menu = Menu()
        self.menu.make_current_screen()
        self.pokedex = PokemonManager()

        self.pokemon1 = self.pokedex.get_random_pokemon()
        self.pokemon1 = Pokemon(self.pokemon1['Name'])

        #self.button1 = None
 
    def on_init(self):
        self.in_menu = True
        self.in_battle = False
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if self.menu.fight_button_is_clicked(event):
            self.battle.make_current_screen()
            self.in_battle = True
            self.in_menu = False
        if self.battle.back_button_is_clicked(event):
            self.menu.make_current_screen()
            self.in_battle = False
            self.in_menu = True

    def on_loop(self):
        pass

    def on_render(self):
        if self.in_menu == True:
            self.menu.display_screen()
        if self.in_battle == True:
            self.battle.display_screen()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()