import pygame
import sys
import pandas
import DLA_L
from DLA_L import *

WHITE = (255, 255, 255)
LIGHT = (173, 216, 230)
DARK = (95, 158, 160)
SCALE = 2


class Visualisation:
    def __init__(self):
        self.control = Controller()

    def processing(self, share):
        pygame.init()
        form = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        form.fill(WHITE)
        pygame.display.update()
        pygame.display.set_caption('DLA')
        self.control.initialization()
        while self.control.count_of_cells < WIDTH * LENGTH * share / 100:
            self.control.moving()

            if self.control.drawing:
                for i in range(LENGTH):
                    for j in range(WIDTH):
                        if field[i][j] == 0:
                            pygame.draw.rect(form, WHITE, [i * SCALE, j * SCALE, SCALE, SCALE])
                        if field[i][j] == 1:
                            pygame.draw.rect(form, LIGHT, [i * SCALE, j * SCALE, SCALE, SCALE])
                        if field[i][j] == 2:
                            pygame.draw.rect(form, DARK, [i * SCALE, j * SCALE, SCALE, SCALE])
                    pygame.display.update()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()


def main():
    share = int(input('Введите процент клеток: '))
    dis = Visualisation()
    dis.processing(share)
    #df = pandas.DataFrame(field)
    #writer = pandas.ExcelWriter('output.xlsx')  # write dataframe to excel
    #df.to_excel(writer)
    #writer.save()


main()