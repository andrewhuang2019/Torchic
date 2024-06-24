import pygame
from pygame.locals import *
from button import Button
from battle import Battle

blue = (0, 0, 255)
green = (0, 255, 0)

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 600
        self.button1 = None
        self.in_battle = False
 
    def on_init(self):
        self.battle_screen = Battle()
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if self.battle_screen.button1_is_clicked(event):
            print("Button clicked!")
    
    def on_loop(self):
        self.battle_screen.display_screen()
        pygame.display.flip()

    def on_render(self):
        pass
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