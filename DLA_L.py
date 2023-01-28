import random
INCREASE = 15
WIDTH = 100
LENGTH = 100
RADIUS = 5
SPEED = 5
field = [[0 for i in range(WIDTH)] for j in range(LENGTH)]

class Coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0

class Particle:
    def __init__(self):
        self.step = Coordinate()
        self.moving_particle = Coordinate()
        self.centre_particle = Coordinate()
        self.centre_particle.x = WIDTH // 2
        self.centre_particle.y = LENGTH // 2
        self.aggregate_near_particle = None
        self.change = 0

    def draw_centre(self):
        for i in range(LENGTH):
            for j in range(WIDTH):
                if (i - self.centre_particle.y + 1) ** 2 + (j - self.centre_particle.x + 1) ** 2 <= (RADIUS - 1) ** 2:
                    field[i][j] = 2

    def random_cords(self):
        # intersection = None
        self.moving_particle.x = random.randint(2 * RADIUS + 1, WIDTH - 2 * RADIUS)
        self.moving_particle.y = random.randint(2 * RADIUS + 1, LENGTH - 2 * RADIUS)
        # while intersection != False:
        # count_of_cells = 0
        for i in range(self.moving_particle.y - RADIUS, self.moving_particle.y + RADIUS):
            for j in range(self.moving_particle.x - RADIUS, self.moving_particle.x + RADIUS):
                if field[i][j] == 2:
                    # count_of_cells = 1
                    # intersection = True
                    self.moving_particle.x = random.randint(2 * RADIUS + 1, WIDTH - 2 * RADIUS - 2)
                    self.moving_particle.y = random.randint(2 * RADIUS + 1, LENGTH - 2 * RADIUS - 2)
        # if count_of_cells = 0
        # intersection = False

    def random_step(self):
        self.step.x = random.randrange(-SPEED, SPEED + 1, SPEED)
        self.step.y = random.randrange(-SPEED, SPEED + 1, SPEED)
        while (self.moving_particle.x + self.step.x <= 2 * RADIUS + 1) and (self.moving_particle.y + self.step.y <= 2 * RADIUS + 1) and (
                self.moving_particle.x + self.step.x > WIDTH - 2 * RADIUS) and (
                self.moving_particle.y + self.step.y > LENGTH - 2 * RADIUS):
            self.step.x = random.randrange(-SPEED, SPEED + 1, SPEED)
            self.step.y = random.randrange(-SPEED, SPEED + 1, SPEED)

    def draw_particle(self, type):
        for i in range(LENGTH):
            for j in range(WIDTH):
                if (i - self.moving_particle.y + 1) ** 2 + (j - self.moving_particle.x + 1) ** 2 <= (RADIUS - 1) ** 2:
                    if field[i][j] == 2:
                        continue
                    else:
                        field[i][j] = type

    def checking(self):
        self.aggregate_near_particle = False
        for i in range(self.moving_particle.y - RADIUS, self.moving_particle.y + RADIUS):
            for j in range(self.moving_particle.x - RADIUS, self.moving_particle.x + RADIUS):
                if field[i][j] == 2:
                    self.draw_particle(2)
                    self.aggregate_near_particle = True

        if self.aggregate_near_particle:
            self.random_cords()
            self.draw_particle(1)
        else:
            self.random_step()
            self.draw_particle(0)
            self.moving_particle.x += self.step.x
            self.moving_particle.y += self.step.y
            self.draw_particle(1)

class Controller:
    def __init__(self):
        self.ca = Particle()
        self.count_of_cells_now = 0
        self.count_of_cells = 0
        self.drawing = None

    def initialization(self):
        self.ca.draw_centre()
        self.ca.random_cords()
        self.ca.draw_particle(1)

    def moving(self):
        self.drawing = False
        self.count_of_cells_now = 0
        if (self.ca.moving_particle.x > 2 * RADIUS) and (self.ca.moving_particle.y > 2 * RADIUS) and (
                self.ca.moving_particle.x < WIDTH - 2 * RADIUS) and (self.ca.moving_particle.y < LENGTH - 2 * RADIUS):
            self.ca.checking()
            for i in range(LENGTH):
                for j in range(WIDTH):
                    if field[i][j] == 2:
                        self.count_of_cells_now += 1
            if self.count_of_cells_now > self.count_of_cells + INCREASE:
                self.drawing = True
                self.count_of_cells = self.count_of_cells_now
        else:
            self.ca.draw_particle(0)
            self.ca.random_cords()
            self.ca.draw_particle(1)