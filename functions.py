from tkinter import *
import random
from tkinter import messagebox as mb
from math import sqrt
# Globals
WIDTH = 1000
HEIGHT = 600
SEG_SIZE = 20

##############################################################
# Helper functions


# def create_block(c):
#     """ Creates an apple to be eaten """
#     global BLOCK
#     posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
#     posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
#     BLOCK = c.create_oval(posx, posy,
#                           posx + SEG_SIZE, posy + SEG_SIZE,
#                           fill="red", outline='black')
#     return BLOCK

def distance(s, e, c):
    MIN = 2*SEG_SIZE
    for i in range(s.life):
        for j in range(e.life):
            s_head_coords = c.coords(s.segments[i].instance)
            x11, y11, x12, y12 = s_head_coords
            e_head_coords = c.coords(e.segments[j].instance)
            x21, y21, x22, y22 = e_head_coords
            K = min(sqrt((abs(x11 - x21))**2 + (abs(y11 - y21))**2), sqrt((abs(x12 - x22))**2 + (abs(y12 - y22))**2))
            if MIN > K:
                MIN = K
    return MIN


# def main():
#     """ Handles game process """
#     global IN_GAME, BLOCK
#     if IN_GAME:
#         s.move()
#         e.move()
#         s_head_coords = c.coords(s.segments[-1].instance)
#         x11, y11, x12, y12 = s_head_coords
#         # Check for collision with gamefield edges
#         if x12 > WIDTH or x11 < 0 or y11 < 0 or y12 > HEIGHT:
#             IN_GAME = False
#         # Check for collision with enemy
#         elif distance(s, e) < SEG_SIZE:
#             # тут сразу и жизнь режется
#             s.delete_seg()
#             e.add_enemy_segment()
#         # elif s.life == 0:
#         #     IN_GAME = False
#         # Eating apples
#         elif  [x11, y11, x12, y12] == c.coords(BLOCK):
#             s.add_segment()
#             c.delete(BLOCK)
#             create_block()
#             Score += 1
#         # Self-eating
#         else:
#             for index in range(len(s.segments) - 1):
#                 if s_head_coords == c.coords(s.segments[index].instance):
#                     IN_GAME = False
#                     pass
#         root.after(100, main)
#         # Not IN_GAME -> stop game and print message
#     else:
#         c.create_text(WIDTH / 2, HEIGHT / 2,
#                   text="GAME OVER!",
#                   font="Arial 20",
#                   fill="red")

def new_game(c, s, e, main, apple):
    answer = mb.askyesno(title="Question", message="Start new game?")
    if answer == True:
        c.delete(apple)
        c.delete(s.segments)
        c.delete(e.segments)
        root = Tk()
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
                          cl.Enemy_segment(740, 400, c)]
        s = cl.Snake(segments)
        e = cl.Enemy(enemy_segments)

        # Reaction on keypress
        c.bind("<KeyPress>", s.change_direction)
        fu.create_block(c)
        IN_GAME = True
        main(IN_GAME, 0, c)
        root.mainloop()



def load_game(root):
    filewin = Toplevel(root)
    button = Button(filewin, text="Load game")
    button.pack()

def save(root):
    filewin = Toplevel(root)
    button = Button(filewin, text="Save progress")
    button.pack()

def score(Score):
    print('Score '.format(Score.points))
