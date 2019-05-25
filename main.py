from tkinter import *
from tkinter import messagebox as mb
import random
from math import *
import time
import classes  as cl
import functions as fu

# Globals
WIDTH = 1000
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True
Score = cl.Score(0)
##############################################################
# Helper functions
#
# def create_block():
#     """ Creates an apple to be eaten """
#     global BLOCK
#     posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
#     posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
#     BLOCK = c.create_oval(posx, posy,
#                           posx + SEG_SIZE, posy + SEG_SIZE,
#                           fill="red", outline='black')
#
# def distance(s, e):
#     MIN = 2*SEG_SIZE
#     for i in range(s.life):
#         for j in range(len(e.segments)):
#             s_head_coords = c.coords(s.segments[i].instance)
#             x11, y11, x12, y12 = s_head_coords
#             e_head_coords = c.coords(e.segments[j].instance)
#             x21, y21, x22, y22 = e_head_coords
#             K = min(sqrt((abs(x11 - x21))**2 + (abs(y11 - y21))**2), sqrt((abs(x12 - x22))**2 + (abs(y12 - y22))**2))
#             if MIN > K:
#                 MIN = K
#     return MIN
#

def main(IN_GAME, Score):
    """ Handles game process """
    # global IN_GAME, BLOCK
    if IN_GAME:
        s.move(c)
        e.move(c)
        # print("func main()\nprint segments and segments coordinates")
        # print(s.segments)
        for segm in s.segments:
            print(c.coords(segm.instance))
        s_head_coords = c.coords(s.segments[-1].instance)
        x11, y11, x12, y12 = s_head_coords
        # Check for collision with gamefield edges
        if x12 > WIDTH or x11 < 0 or y11 < 0 or y12 > HEIGHT:
            IN_GAME = False
        # Check for collision with enemy
        elif fu.distance(s, e, c) < SEG_SIZE:
            # тут сразу и жизнь режется
            s.delete_seg()
            e.add_enemy_segment()
        # elif s.life == 0:
        #     IN_GAME = False
        # Eating apples
        elif s_head_coords == c.coords(fu.BLOCK):
            s.add_segment()
            c.delete(fu.BLOCK)
            fu.create_block()
            Score += 1
        # Self-eating
        else:
            for index in range(len(s.segments) - 1):
                if s_head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
                    pass
        root.after(100, main(IN_GAME, Score))
        # Not IN_GAME -> stop game and print message
    else:
        return c.create_text(WIDTH / 2, HEIGHT / 2,
                  text="GAME OVER!",
                  font="Arial 20",
                  fill="red"), Score


#####################################################################
# Classes
#
# class Segment(object):
#     """ Single snake segment """
#     def __init__(self, x, y):
#         self.instance = c.create_rectangle(x, y,
#                                            x + SEG_SIZE, y + SEG_SIZE,
#                                            fill="white")
#
# class Enemy_segment(object):
#     """ Single enemy segment """
#     def __init__(self, x, y):
#         self.instance = c.create_rectangle(x, y,
#                                            x + SEG_SIZE, y + SEG_SIZE,
#                                            fill="dark green")
#
#
# class Snake(object):
#     """ Simple Snake class """
#
#     def __init__(self, segments, life = 5):
#         self.segments = segments
#         self.life = life
#         # possible moves
#         self.mapping = {"Down": (0, 1), "Right": (1, 0),
#                         "Up": (0, -1), "Left": (-1, 0)}
#         # initial movement direction
#         self.vector = self.mapping["Right"]
#
#     def delete(self):
#         c.delete(self.segments)
#         self.segments = None
#
#     def move(self):
#         """ Moves the snake with the specified vector"""
#         for index in range(len(self.segments) - 1):
#             segment = self.segments[index].instance
#             x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
#             c.coords(segment, x1, y1, x2, y2)
#
#         x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
#         c.coords(self.segments[-1].instance,
#                  x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
#                  x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)
#
#     def add_segment(self):
#         """ Adds segment to the snake """
#         last_seg = c.coords(self.segments[0].instance)
#         x = last_seg[2] - SEG_SIZE
#         y = last_seg[3] - SEG_SIZE
#         self.life += 1
#         self.segments.insert(0, Segment(x, y))
#
#     def delete_seg(self):
#         return self._delete()
#
#     def _delete(self):
#         l = s.segments[1:]
#         self.segments = l
#         self.life -= 1
#         c.delete(s.segments[0])
#
#     def change_direction(self, event):
#         """ Changes direction of snake """
#         if event.keysym in self.mapping:
#             self.vector = self.mapping[event.keysym]
#
#
# class Enemy(object):
#     """ Random enemy class """
#     def __init__(self, segments):
#         self.segments = segments
#         # possible moves
#         self.mapping = {"Down": (0, 1), "Right": (1, 0),
#                         "Up": (0, -1), "Left": (-1, 0)}
#         # initial movement direction
#         self.vector = self.mapping["Down"]
#
#     def delete(self):
#         c.delete(self.segments)
#         self.segments = None
#
#     def move(self):
#         """ Moves the enemy with a random vector"""
#         for index in range(len(self.segments) - 1):
#             segment = self.segments[index].instance
#             x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
#             c.coords(segment, x1, y1, x2, y2)
#         if x2 > WIDTH:
#             self.vector = self.mapping["Left"]
#         elif x1 < 0 :
#             self.vector = self.mapping["Right"]
#         elif y1 < 0 :
#             self.vector = self.mapping["Down"]
#         elif y2 > HEIGHT:
#             self.vector = self.mapping["Up"]
#         else:
#             l = ["Down", "Right", "Up", "Left"]
#             self.vector = self.mapping[l[random.randint(0, 3)]]
#         x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
#         c.coords(self.segments[-1].instance,
#                  x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
#                  x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)
#
#     def add_enemy_segment(self):
#         """ Adds segment to the enemy """
#         last_seg = c.coords(self.segments[0].instance)
#         x = last_seg[2] - SEG_SIZE
#         y = last_seg[3] - SEG_SIZE
#         self.segments.insert(0, Enemy_segment(x, y))
#
#     def change_direction(self, event):
#         """ Changes direction of enemy"""
#         if event.keysym in self.mapping:
#             L = ["Down", "Right", "Up", "Left"]
#             self.vector = L[random.randint(0, 3)]

##############################################################################




####################################################################

# def new_game():
#     answer = mb.askyesno(title="Question", message="Start new game?")
#     if answer == True:
#         root = Tk()
#         root.title("Catch the Ribosome!")
#
#         mainmenu = Menu(root)
#         root.config(menu=mainmenu)
#         # Пропишем рамку
#         frame = Frame(root, bg='pink', bd=5)
#         root.config(menu=mainmenu)
#         mainmenu.add_command(label="New game", command=new_game)
#         mainmenu.add_command(label="Load game", command=fu.load_game)
#         mainmenu.add_command(label="Save", command=fu.save)
#         mainmenu.add_command(label="Exit", command=root.quit)
#         Button(root, text="Score {}".format(Score), command=fu.score).grid(ipadx=100, ipady=20)




# c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
# c.grid()
# # catch keypressing
# c.focus_set()

# Reaction on keypress



# creating segments and snake




# c.bind("<KeyPress>", s.change_direction)
# # c.bind("<KeyPress>", e.change_direction)
# Score = 0
# main(True, 0)
# root.mainloop()

# def load_game():
#     filewin = Toplevel(root)
#     button = Button(filewin, text="Load game")
#     button.pack()
#
# def save():
#     filewin = Toplevel(root)
#     button = Button(filewin, text="Save progress")
#     button.pack()
#
# def score():
#     print('Score '.format(Score))

################################################################################

# Setting up window
root = Tk()
root.title("Catch the Ribosome!")

mainmenu = Menu(root)
root.config(menu=mainmenu)
# Пропишем рамку
frame = Frame(root, bg='pink', bd=5)
root.config(menu=mainmenu)
mainmenu.add_command(label="New game", command=fu.new_game)
mainmenu.add_command(label="Load game", command=fu.load_game)
mainmenu.add_command(label="Save", command=fu.save)
mainmenu.add_command(label="Exit", command=root.quit)
Button(root, text="Score {}".format(cl.Score), command=fu.score).grid(ipadx=100, ipady=20)

####################################################################


c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
c.grid()


# catch keypressing
c.focus_set()
# creating segments and snake
segments = [cl.Segment(10, 300, c),
                cl.Segment(30, 300, c),
                cl.Segment(50, 300, c),
                cl.Segment(70, 300, c),
                cl.Segment(90, 300, c)]

enemy_segments = [cl.Enemy_segment(700, 400, c),
                  cl.Enemy_segment(720, 400, c),
                  cl.Enemy_segment(740, 400,c )]
s = cl.Snake(segments, c)
e = cl.Enemy(enemy_segments)
# Reaction on keypress
c.bind("<KeyPress>", s.change_direction)

fu.create_block(c)
main(IN_GAME, 0)
root.mainloop()