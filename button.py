import pygame
import time


class Button:
    def __init__(self, x, y, width, height, text=None, function=None, color=(70, 70, 70), highlightedColor=(170, 170, 170),  parameter=None):
        pygame.init()
        self.image = pygame.Surface((width, height))
        self.position = (x, y)
        self.width = width
        self.height = height
        self.rectangle = self.image.get_rect()
        self.rectangle.topleft = self.position
        self.text = text
        self.color = color
        self.highlightedColor = highlightedColor
        self.function = function
        self.parameter = parameter
        self.highlighted = False

    def update(self, mouse):
        click = pygame.mouse.get_pressed()
        if self.rectangle.collidepoint(mouse):
            self.highlighted = True
            if click[0] == 1:
                    self.function()
                    time.sleep(0.4)
        else:
            self.highlighted = False

    def draw(self, window):
        self.image.fill(
            self.highlightedColor if self.highlighted else self.color)
        window.blit(self.image, self.position)
        font = pygame.font.SysFont('arial', self.height//2)
        msg = font.render(self.text, True, (255, 255, 255))
        textRect = msg.get_rect()
        textRect.center = (self.position[0] + self.width // 2, self.position[1] + self.height // 2)
        window.blit(msg, textRect)