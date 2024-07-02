import pygame

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font("assets/pokemon_pixel_font.ttf", 36)
        self.text_surf = self.font.render(text, True, white)
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)
    
    #draws a button onto the screen
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    #checks to see if a button is clicked
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
    
    #updates the text on a button
    def update_text(self, new_text):
        self.text = new_text
        self.text_surf = self.font.render(new_text, True, white)
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)