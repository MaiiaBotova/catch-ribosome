from tkinter import *
import random

# Globals
WIDTH = 1000
HEIGHT = 600
SEG_SIZE = 20

#####################################################################
# Classes
#####################################################################

class Block(Canvas):
    def __init__(self, size, c, x = 0, y = 0 ):
        super().__init__()
        self.x = size * random.randint(1, (WIDTH - size) / size)
        self.y = size * random.randint(1, (HEIGHT - size) / size)
        self.size = size
        self.canvas = c
        self.life = 1
        self.instance = self.canvas.create_rectangle(self.x, self.y,
                                           self.x + self.size, self.y + self.size,
                                           fill="red", outline='black')

    def create_block(self):
        """ Creates an apple to be eaten """
        self.x = self.size * random.randint(1, (WIDTH - self.size) / self.size)
        self.y = self.size * random.randint(1, (HEIGHT - self.size) / self.size)
        self.canvas.create_rectangle(self.x, self.y,
                                     self.x + self.size, self.y + self.size,
                                     fill="red", outline='black')


    def delete_block(self):
        self.canvas.delete(self.instance)



class Segment:
    """ Single snake segment """
    def __init__(self, x, y, c):
        self.c = c
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="white")
        self.life = 1


class Enemy_segment:
    """ Single enemy segment """
    def __init__(self, x, y, c):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="dark green")
        self.life = 1
###############################################################################
class Snake:
    """ Simple Snake class """

    def __init__(self, segments, life = 5):
        self.segments = segments
        self.life = life
        # possible moves
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # initial movement direction
        self.vector = self.mapping["Right"]

    def delete(self):
        c.delete(self.segments)
        self.segments = None

    def move(self, c):
        """ Moves the snake with the specified vector"""
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

    def add_segment(self, c):
        """ Adds segment to the snake """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.life += 1
        self.segments.insert(0, Segment(x, y, c))

    def delete_seg(self, c):
        return self._delete(c)

    def _delete(self, c):
        l = self.segments[1:]
        self.segments = l
        self.life -= 1
        c.delete(self.segments[0])

    def change_direction(self, event):
        """ Changes direction of snake """
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

######################################################################
class Enemy:
    """ Random enemy class """
    def __init__(self, segments):
        self.segments = segments
        self.life = 3
        # possible moves
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # initial movement direction
        self.vector = self.mapping["Down"]

    def delete(self, c):
        c.delete(self.segments)
        self.segments = None

    def move(self, c):
        """ Moves the enemy with a random vector"""
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)
        if x2 > WIDTH:
            self.vector = self.mapping["Left"]
        elif x1 < 0 :
            self.vector = self.mapping["Right"]
        elif y1 < 0 :
            self.vector = self.mapping["Down"]
        elif y2 > HEIGHT:
            self.vector = self.mapping["Up"]
        else:
            l = ["Down", "Right", "Up", "Left"]
            self.vector = self.mapping[l[random.randint(0, 3)]]
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
                 x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)

    def add_enemy_segment(self, c):
        """ Adds segment to the enemy """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Enemy_segment(x, y))

    def change_direction(self, event):
        """ Changes direction of enemy"""
        if event.keysym in self.mapping:
            L = ["Down", "Right", "Up", "Left"]
            self.vector = L[random.randint(0, 3)]

##############################################################################