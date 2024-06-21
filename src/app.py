import pygame
from pygame.locals import *
from button import Button

blue = (0, 0, 255)
green = (0, 255, 0)

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 600
        self.button1 = None
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Torchic")
        self.button1 = Button(350, 450, 200, 50, "Click Me", blue, green)
        self.button2 = Button(575, 450, 200, 50, "Click Me", blue, green)
        self.button3 = Button(350, 525, 200, 50, "Click Me", blue, green)
        self.button4 = Button(575, 525, 200, 50, "Click Me", blue, green)

        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if self.button1.is_clicked(event):
            print("Button Clicked!")
    
    def on_loop(self):
        self.button1.draw(self._display_surf)
        self.button2.draw(self._display_surf)
        self.button3.draw(self._display_surf)
        self.button4.draw(self._display_surf)
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