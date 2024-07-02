import pygame

class Screen:
    def __init__(self, title, width=800, height=600, fill=(0,0,255)):
        self.title = title

        self.height = height

        self.width = width

        self.fill = fill

        self.current_state = False

    #sets the screen as the current screen
    def make_current_screen(self):
        pygame.display.set_caption(self.title)
        self.current_state = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    #ends the current screen
    def end_current_screen(self):
        self.current_state = False

    #updates screen color property and checks current state
    def check_update(self, fill):
        self.fill = fill
        return self.current_state
    
    #updates screen color
    def screen_update(self):
        if self.current_state:
            self.screen.fill(self.fill)

    #returns the screen title (?)
    def get_title(self):
        return self.screen