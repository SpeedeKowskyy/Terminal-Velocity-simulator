import pygame

class Plotter:
    def __init__(self, width, height, text):
        self.width = width
        self.height = height

        self.text = text

        self.surf = pygame.Surface((self.width,self.height))

        self.axis_thickness = 2
        self.notch_height = 3
        self.notch_thickness = 1
        self.line_thickness = 2

        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)

        self.font = pygame.font.Font('freesansbold.ttf', 16)

    def update(self, y_vals):
        self.surf.fill(self.white)

        text = self.font.render(self.text + str(round(y_vals[-1], 4)), True, self.black)
        textRect = text.get_rect()
        textRect.center = self.width//2, self.height//2
        self.surf.blit(text, textRect)

        pygame.draw.line(self.surf, self.black, (0, self.height), (0, 0), self.axis_thickness)
        pygame.draw.line(self.surf, self.black, (0, self.height), (self.width, self.height), self.axis_thickness)

        n = len(y_vals)
        off_x = self.width/n
        temp_x = 0

        y_vals = [abs(x) for x in y_vals]

        max_val = max(y_vals)
        last_pos = (0, y_vals[0])

        for i in y_vals:
            temp_x += off_x
            if max_val != 0:
                y = self.height-(i/max_val)*self.height
            else:
                y = 0
            pygame.draw.line(self.surf, self.black, (temp_x, self.height), (temp_x, self.height-self.notch_height), self.notch_thickness)
            pygame.draw.line(self.surf, self.black, (0, y), (self.notch_height, y), self.notch_thickness)

            pygame.draw.line(self.surf, self.red, last_pos, (temp_x, y), self.line_thickness)

            last_pos = (temp_x, y)
