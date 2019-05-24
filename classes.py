from tkinter import *
#####################################################################
# Classes

class Segment(object):
    """ Single snake segment """
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="white")

class Enemy_segment(object):
    """ Single enemy segment """
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="dark green")


class Snake(object):
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

    def move(self):
        """ Moves the snake with the specified vector"""
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
                 x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)

    def add_segment(self):
        """ Adds segment to the snake """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.life += 1
        self.segments.insert(0, Segment(x, y))

    def delete_seg(self):
        return self._delete()

    def _delete(self):
        l = s.segments[1:]
        self.segments = l
        self.life -= 1
        c.delete(s.segments[0])

    def change_direction(self, event):
        """ Changes direction of snake """
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]


class Enemy(object):
    """ Random enemy class """
    def __init__(self, segments):
        self.segments = segments
        # possible moves
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # initial movement direction
        self.vector = self.mapping["Down"]

    def delete(self):
        c.delete(self.segments)
        self.segments = None

    def move(self):
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

    def add_enemy_segment(self):
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