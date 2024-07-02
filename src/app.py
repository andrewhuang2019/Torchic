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

        self.pokedex = PokemonManager()

        self.pokemon1 = self.pokedex.get_random_pokemon()
        self.pokemon1 = Pokemon(self.pokemon1['Name'], self.pokemon1['HP'], self.pokemon1['Attack'], self.pokemon1['Defense'], 
                                self.pokemon1['Sp. Atk'], self.pokemon1['Sp. Def'], self.pokemon1['Speed'], 25, 
                                4, self.pokemon1['Type 1'], self.pokemon1['Type 2'])
        
        self.pokemon2 = self.pokedex.get_random_pokemon()
        self.pokemon2 = Pokemon(self.pokemon2['Name'], self.pokemon2['HP'], self.pokemon2['Attack'], self.pokemon2['Defense'], 
                                self.pokemon2['Sp. Atk'], self.pokemon2['Sp. Def'], self.pokemon2['Speed'], 25, 
                                4, self.pokemon2['Type 1'], self.pokemon2['Type 2'])

        self.battle = Battle(self.pokemon1, self.pokemon2)
        self.menu = Menu()
        self.menu.make_current_screen()
 
    def on_init(self):
        self.in_menu = True
        self.in_battle = False
        self._running = True
 
    def on_event(self, event):

        if event.type == pygame.QUIT:
            self._running = False

        if self.menu.fight_button_is_clicked(event):

            self.pokemon1 = self.pokedex.get_random_pokemon()
            self.pokemon1 = Pokemon(self.pokemon1['Name'], self.pokemon1['HP'], self.pokemon1['Attack'], self.pokemon1['Defense'], 
                                    self.pokemon1['Sp. Atk'], self.pokemon1['Sp. Def'], self.pokemon1['Speed'], 25, 
                                    4, self.pokemon1['Type 1'], self.pokemon1['Type 2'])
        
            self.pokemon2 = self.pokedex.get_random_pokemon()
            self.pokemon2 = Pokemon(self.pokemon2['Name'], self.pokemon2['HP'], self.pokemon2['Attack'], self.pokemon2['Defense'], 
                                    self.pokemon2['Sp. Atk'], self.pokemon2['Sp. Def'], self.pokemon2['Speed'], 25, 
                                    4, self.pokemon2['Type 1'], self.pokemon2['Type 2'])
            
            self.battle = Battle(self.pokemon1, self.pokemon2)
            self.battle.make_current_screen()
            self.in_battle = True
            self.in_menu = False

        if self.battle.button1_is_clicked(event):
            if self.battle.button1_text() == "FIGHT":
                self.battle.button1_set_text("ATTACK")
            elif self.battle.button1_text() == "ATTACK":
                self.battle.button1_set_text("FIGHT")

        if self.battle.button2_is_clicked(event):
            if self.battle.button2_text() == "PKMN":
                self.battle.button2_set_text("POKE")
            elif self.battle.button2_text() == "POKE":
                self.battle.button2_set_text("PKMN")

        if self.battle.button3_is_clicked(event):
            if self.battle.button3_text() == "ITEM":
                self.battle.button3_set_text("POTION")
            elif self.battle.button3_text() == "POTION":
                self.battle.button3_set_text("ITEM")

        if self.battle.button4_is_clicked(event):
            if self.battle.button4_text() == "RUN":
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