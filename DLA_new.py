import random
import pygame
import sys
import pandas

x = 400
y = 400
r = 5
field = [[0 for i in range(x)] for j in range(y)]


class Coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0


class Particle:
    def __init__(self):
        self.step = Coordinate()
        self.circle = Coordinate()
        self.centre = Coordinate()
        self.centre.x = x // 2
        self.centre.y = y // 2
        self.aggregate_near_particle = None
        self.change = 0

    def random_cords(self):
        a = True
        self.circle.x = random.randint(r, x - r - 1)
        self.circle.y = random.randint(r, y - r - 1)
        while a == True:
            for i in range(y):
                for j in range(x):
                    if (i - self.circle.y + 1) ** 2 + (j - self.circle.x + 1) ** 2 <= (r - 1) ** 2 and field[i][j] == 2:
                        self.circle.x = random.randint(r, x - r - 1)
                        self.circle.y = random.randint(r, y - r - 1)
                    else:
                        a = False

    def random_step(self):
        self.step.x = random.randrange(-5, 6, 5)
        self.step.y = random.randrange(-5, 6, 5)

    def draw_centre(self):
        for i in range(y):
            for j in range(x):
                if (i - self.centre.y + 1) ** 2 + (j - self.centre.x + 1) ** 2 <= (r - 1) ** 2:
                    field[i][j] = 2

    def draw_particle(self, type):
        for i in range(y):
            for j in range(x):
                if (i - self.circle.y + 1) ** 2 + (j - self.circle.x + 1) ** 2 <= (r - 1) ** 2:
                    field[i][j] = type

    def checking(self):
        self.aggregate_near_particle = False

        for i in range(y):
            for j in range(x):
                if (field[i][j] == 2) and (self.circle.x - r < i) and (self.circle.x + r > i) and (self.circle.y - r < j) and (self.circle.y + r > j):
                    self.draw_particle(2)
                    self.aggregate_near_particle = True

        if self.aggregate_near_particle == True:
            self.random_cords()
            self.draw_particle(1)
            self.change +=1
        else:
            self.random_step()
            while (self.circle.x + self.step.x <= r) and (self.circle.y + self.step.y <= r) and (self.circle.x + self.step.x > x) and (self.circle.y + self.step.y > y):
                self.random_step()
            self.draw_particle(0)
            self.circle.x += self.step.x
            self.circle.y += self.step.y
            self.draw_particle(1)

class Controller:
    def __init__(self):
        self.ca = Particle()
        self.count_of_cells = 0

    def initialization (self):
        self.ca.draw_centre()
        self.ca.random_cords()
        self.ca.draw_particle(1)

    def moving (self):
        self.count_of_cells = 0
        if (self.ca.circle.x > r) and (self.ca.circle.y > r) and (self.ca.circle.x < x) and (self.ca.circle.y < y):
            self.ca.checking()
            for i in range(y):
                for j in range(x):
                    if field[i][j] == 2:
                        self.count_of_cells += 1
        else:
            self.ca.draw_particle(0)
            self.ca.random_cords()
            self.ca.draw_particle(1)


class Visualisation:
    def __init__(self):
        self.control = Controller()

    def processing(self, share):
        pygame.init()
        #FPS = 60
        WHITE = (255, 255, 255)
        LIGHT = (173, 216, 230)
        DARK = (95, 158, 160)
        scale = 2
        form = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        form.fill(WHITE)
        pygame.display.update()
        pygame.display.set_caption('DLA')
        self.control.initialization()
        #clock = pygame.time.Clock()
        while self.control.count_of_cells < x * y * share / 100:
            #clock.tick(FPS)
            self.control.moving()
            for i in range(y):
                for j in range(x):
                    if field[i][j] == 0:
                        pygame.draw.rect(form, WHITE, [i * scale, j * scale, scale, scale])
                    if field[i][j] == 1:
                        pygame.draw.rect(form, LIGHT, [i * scale, j * scale, scale, scale])
                    if field[i][j] == 2:
                        pygame.draw.rect(form, DARK, [i * scale, j * scale, scale, scale])
                pygame.display.update()
        #clock.tick(FPS)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()

def main():
    share = int(input('Введите процент клеток: '))
    dis = Visualisation()
    dis.processing(share)

main()
