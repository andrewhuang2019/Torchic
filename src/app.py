import pygame
from pygame.locals import *

from button import Button
from battle import Battle
from screen import Screen

blue = (0, 0, 255)
green = (0, 255, 0)

class App:
    def __init__(self):
        pygame.init()
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 600

        self.battle = Battle()
        self.menu_screen = Screen("Menu")
        self.battle.make_current_screen()
        #self.button1 = None
        self.in_battle = True
 
    def on_init(self):
        self.menu_screen.make_current_screen()
        #self.battle_screen = Battle()
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        
        '''if self.battle_screen.button1_is_clicked(event):
            print("Button clicked!")'''
    
    def on_loop(self):
        #self.battle_screen.display_screen()

        #self.battle_screen.screen_update()
        pass

    def on_render(self):
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