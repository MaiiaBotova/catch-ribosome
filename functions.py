from tkinter import *
import random
from tkinter import messagebox as mb
from math import sqrt
# Globals
WIDTH = 1000
HEIGHT = 500
SEG_SIZE = 20

##############################################################
# Helper functions


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

# def new_game():
#     answer = mb.askyesno(title="Question", message="Start new game?")
#     if answer == True:
#         c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
#         # c.place(relx=-5, rely=-1, anchor=CENTER)
#         c.grid(row=0, column=0, sticky=(N, E, S, W))
#         # catch keypressing
#         c.focus_set()
#         # creating segments and snake
#         segments = [cl.Segment(0, 300, c),
#                     cl.Segment(20, 300, c),
#                     cl.Segment(40, 300, c),
#                     cl.Segment(60, 300, c),
#                     cl.Segment(80, 300, c)]
#
#         enemy_segments = [cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                           cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                           cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)]
#         s = cl.Snake(segments)
#         e = cl.Enemy(enemy_segments)
#         e2 = cl.Enemy([cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                        cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                        cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)])
#         e3 = cl.Enemy([cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                        cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                        cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)])
#         # Reaction on keypress
#         c.bind("<KeyPress>", s.change_direction)
#         # Creating an apple
#         apple = cl.Block(SEG_SIZE, c)
#         # apple.instance
#         IN_GAME = True
#         c.create_text(100, 50, anchor=N, font="Purisa",
#                       text="Score {}".format(Score))
#         main(IN_GAME, True, c, apple)
#         root.mainloop()






def _get_save_file_name(self):
       initialdir = os.path.expanduser(SAVE_DIR)
       if not os.path.exists(initialdir):
           os.makedirs(initialdir)
       save_file_name = filedialog.asksaveasfilename(
           initialdir=initialdir,
           title='Save game',
           filetypes=(("json files", "*.json"), ("all files", "*.*"))
       )
       if save_file_name in [(), '']:
           return None
       return save_file_name

def save(self):
   old_lock = self.lock
   self.lock = True
   save_file_name = self._get_save_file_name()
   if save_file_name is not None:
       saved_game = {
           "turn": self.turn,
           "moves": self.moves,
           "bot_class_name": self.bot.__class__.__name__,
           "grid": self.grid,
           "lock": old_lock,
           "finished": self.finished,
           "human": self.human,
           "victory_line": self.victory_line,
       }
       with open(save_file_name, 'w') as f:
           json.dump(saved_game, f)
   self.lock = old_lock

def _get_load_file_name(self):
   initialdir = os.path.expanduser(SAVE_DIR)
   if not os.path.exists(initialdir):
       initialdir = os.path.expanduser('~')
   save_file_name = filedialog.askopenfilename(
       initialdir=initialdir,
       filetypes=(("json files", "*.json"), ("all files", "*.*"))
   )
   if save_file_name in [(), '']:
       return None
   return save_file_name