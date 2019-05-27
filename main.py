import os
import random
from math import *
from collections import OrderedDict
import json

from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog

import classes  as cl
import functions as fu


# Globals
WIDTH = 1000
HEIGHT = 500
SEG_SIZE = 20
Score = 0

AminoAcidsDictionary = OrderedDict(
    {'Gly': 'GGG',
                            'Pro': 'CCC',
                            'Asp': 'GAU',
                            'Glu': 'GAG',
                            'Ala': 'GCC',
                            'Asn': 'AAU',
                            'Gln': 'CAA',
                            'Ser': 'UCC',
                            'Thr': 'ACA',
                            'Lys': 'AAA',
                            'Arg': 'AGG',
                            'His': 'CAC',
                            'Val': 'GUC',
                            'Ile': 'AUU',
                            'Met': 'AUG',
                            'Cys': 'UGC',
                            'Leu': 'CUU',
                            'Phe': 'UUU',
                            'Tyr': 'UAU',
                            'Trp': 'UGG'}
)
##############################################################



# def second_lvl(Score, root):
#     c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
#     c.grid(row=0, column=5, rowspan=5, columnspan=5, sticky=N+E+S+W)
#     c.create_text(100, 50, anchor=N, font="Purisa",
#                   text="Score {}".format(Score))
#     x1 = 240
#     y1 = 100
#     x2 = 300
#     y2 = 120
#     L = list(AminoAcidsDictionary[k] for k in AminoAcidsDictionary.keys())
#     sequence = [random.choice(L) for _ in range(10)]
#     sequence = 'AUG ' + ' '.join(sequence)
#     seq = sequence
#     res = SecondLevel(seq)
#     c.create_rectangle(x1, y1, x2, y2,
#                             outline="#05f", fill=None)
#     c.create_text(500, 100, anchor=N, font="Purisa",
#                   text="{}".format(seq))
#
#     Gly = Button(root, text="Gly", command=res.gly)
#     Gly.grid(row=0, column=0, sticky=S)
#     Pro = Button(root, text="Pro", command=res.pro)
#     Pro.grid(row=0, column=1, sticky=S)
#     Asp = Button(root, text="Asp", command=res.asp)
#     Asp.grid(row=0, column=2, sticky=S)
#     Glu = Button(root, text="Glu", command=res.glu)
#     Glu.grid(row=0, column=3, sticky=S)
#     Ala = Button(root, text="Ala", command=res.ala)
#     Ala.grid(row=0, column=4, sticky=S)
#     Asn = Button(root, text="Asn", command=res.asn)
#     Asn.grid(row=1, column=0, sticky=S)
#     Gln = Button(root, text="Gln", command=res.gln)
#     Gln.grid(row=1, column=1, sticky=S)
#     Ser = Button(root, text="Ser", command=res.ser)
#     Ser.grid(row=1, column=2, sticky=S)
#     Thr = Button(root, text="Thr", command=res.thr)
#     Thr.grid(row=1, column=3, sticky=S)
#     Lys = Button(root, text="Lys", command=res.lys)
#     Lys.grid(row=1, column=4, sticky=S)
#     Arg = Button(root, text="Arg", command=res.arg)
#     Arg.grid(row=2, column=0, sticky=S)
#     His = Button(root, text="His", command=res.his)
#     His.grid(row=2, column=1, sticky=S)
#     Val = Button(root, text="Val", command=res.val)
#     Val.grid(row=2, column=2, sticky=S)
#     Ile = Button(root, text="Ile", command=res.ile)
#     Ile.grid(row=2, column=3, sticky=S)
#     Met = Button(root, text="Met", command=res.met)
#     Met.grid(row=2, column=4, sticky=S)
#     Cys = Button(root, text="Cys", command=res.cys)
#     Cys.grid(row=3, column=0, sticky=S)
#     Leu = Button(root, text="Leu", command=res.leu)
#     Leu.grid(row=3, column=1, sticky=S)
#     Phe = Button(root, text="Phe", command=res.phe)
#     Phe.grid(row=3, column=2, sticky=S)
#     Tyr = Button(root, text="Tyr", command=res.tyr)
#     Tyr.grid(row=3, column=3, sticky=S)
#     Trp = Button(root, text="Trp", command=res.trp)
#     Trp.grid(row=3, column=4, sticky=S)
#     # Check sequence
#     seq = ''.join(seq.split())
#     while len(seq) > 0:
#         triplet = seq[:3]
#         while True:
#             if res.var:
#                 trio, acid = res.var
#                 if AminoAcidsDictionary[triplet] == acid:
#                     Score += 1
#                 else:
#                     c.create_text(100, 50, anchor=N, font="Purisa",
#                                   text="Wrong! Try another one")
#                     Score -= 1
#                 c.create_rectangle(100, 50, 120, 100, outline=None, fill="peach puff")
#                 c.create_text(100, 50, anchor=N, font="Purisa",
#                                   text="Score {}".format(Score))
#                 c.create_rectangle(x1, y1, x2, y2,
#                                    outline="peach puff", fill=None)
#                 c.create_rectangle(x1+30, y1, x2+30, y2,
#                                    outline="#05f", fill=None)
#                 x1 += 30
#                 x2 += 30
#                 seg = seg[3:]


#
#
# def next():
#     c.destroy()
#     sl = SecondLevel(Score, root)
#     mainloop()
#
#     # second_lvl(Score, root)
# ##############################################################
#
#
# def main(IN_GAME, first_stage, c, apple):
#     """ Handles game process """
#     global Score
#     if IN_GAME:
#         if first_stage:
#             s.move(c)
#             e.move(c)
#             e2.move(c)
#             e3.move(c)
#             for segm in s.segments:
#                 print(c.coords(segm.instance))
#             s_head_coords = c.coords(s.segments[-1].instance)
#             x11, y11, x12, y12 = s_head_coords
#             # Check for collision with gamefield edges
#             if x12 > WIDTH:
#                 first_stage = False
#                 # Next.next()
#                 pass
#                 # second_lvl(Score, root)
#             elif x11 < 0 or y11 < 0 or y12 > HEIGHT:
#                 IN_GAME = False
#                 c.create_text(WIDTH / 2, HEIGHT / 2,
#                               text="GAME OVER!",
#                               font="Arial 20",
#                               fill="red")
#                 pass
#             # Check for collision with enemy
#             elif fu.distance(s, e, c) < SEG_SIZE:
#                 # тут сразу и жизнь режется
#                 s.delete_seg(c)
#                 e.add_enemy_segment(c)
#             elif fu.distance(s, e2, c) < SEG_SIZE:
#                 s.delete_seg(c)
#                 e2.add_enemy_segment(c)
#             elif fu.distance(s, e3, c) < SEG_SIZE:
#                 s.delete_seg(c)
#                 e3.add_enemy_segment(c)
#             # Eating apples
#             elif abs(x11 - apple.x) <= SEG_SIZE and abs(y11 - apple.y) <= SEG_SIZE:
#                 s.add_segment(c)
#                 apple.delete_block()
#                 apple = cl.Block(SEG_SIZE, c)
#                 Score += 1
#                 # context = c.getContext('2d')
#                 # context.getContext("2d").clearRect(100, 50, 10, 10)
#                 c.create_rectangle(125, 50, 150, 100, outline='peach puff',  fill="peach puff")
#                 c.create_text(100, 50, anchor=N, font="Purisa",
#                               text="Score {}".format(Score))
#             # Self-eating
#             else:
#                 for index in range(len(s.segments) - 1):
#                     if s_head_coords == c.coords(s.segments[index].instance):
#                         IN_GAME = False
#                         c.create_text(WIDTH / 2, HEIGHT / 2,
#                                       text="GAME OVER!",
#                                       font="Arial 20",
#                                       fill="red"), Score
#                         pass
#             root.after(100, main, IN_GAME, first_stage, c, apple)
#         # Not IN_GAME -> stop game and print message
#         else:
#             c.create_text(WIDTH / 2, HEIGHT / 2,
#                           text="GOOD JOB!",
#                           font="Arial 20",
#                           fill="red")
#             if Score == 0:
#                 IN_GAME = False
#                 c.create_text(WIDTH / 2, 3*HEIGHT / 4,
#                               text="GAME OVER! Need more points",
#                               font="Arial 20",
#                               fill="red")
#                 pass
#             else:
#                 Next = Button(c, text="Next", command=next)
#                 Next.grid(pady=100, padx=100)
#     else:
#         c.create_text(WIDTH / 2, HEIGHT / 2,
#               text="GAME OVER!",
#               font="Arial 20",
#               fill="red")
#
#
#
# ##############################################################################
# # Setting up window
# ##############################################################################
# root = Tk()
# root.title("Catch the Ribosome!")
# # Creating frame
# frame = Frame(root, bg='pink', bd=5)
# # Making menu string
# mainmenu = Menu(root)
# root.config(menu=mainmenu)
# mainmenu.add_command(label="New game", command=fu.new_game)
# mainmenu.add_command(label="Load game", command=fu.load_game)
# mainmenu.add_command(label="Save", command=fu.save)
# mainmenu.add_command(label="Exit", command=root.quit)
# # Button(root, text="Score {}", command=fu.score).grid(ipadx=100, ipady=20)
#
# ####################################################################
#
# # Drawing canvas
# c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
# # c.place(relx=-5, rely=-1, anchor=CENTER)
# c.grid(row=0, column = 0,  sticky=(N, E, S, W))
# # catch keypressing
# c.focus_set()
# # creating segments and snake
# segments = [cl.Segment(0, 300, c),
#                 cl.Segment(20, 300, c),
#                 cl.Segment(40, 300, c),
#                 cl.Segment(60, 300, c),
#                 cl.Segment(80, 300, c)]
#
# enemy_segments = [cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                   cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                   cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)]
# s = cl.Snake(segments)
# e = cl.Enemy(enemy_segments)
# e2 = cl.Enemy([cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                   cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                   cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)])
# e3 = cl.Enemy([cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                   cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
#                   cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)])
# # Reaction on keypress
# c.bind("<KeyPress>", s.change_direction)
# # Creating an apple
# apple = cl.Block(SEG_SIZE, c)
# # apple.instance
# IN_GAME = True
# c.create_text(100, 50, anchor=N, font="Purisa",
#     text="Score {}".format(Score))
# main(IN_GAME, True, c, apple)
# root.mainloop()

##########################################################################################
# Classes MainFrame and Game
##########################################################################################

class MainFrame(Frame):
    def __init__(self, root, game = None):
        super().__init__()
        self._root = root
        self.grid(row=0, column=0, sticky=(N, E, S, W))
        self._game = game
        self._canvas = None
        self._add_menu()
        self._add_canvas()
        self.lock = False

    def add_game(self, game):
        self._game = game

    def _add_menu(self):
        mainmenu = Menu(self._root)
        self._root.config(menu=mainmenu)
        # Пропишем рамку
        frame = Frame(self._root, bg='pink', bd=5)
        self._root.config(menu=mainmenu)
        mainmenu.add_command(label="New game", command=self.new_game)
        mainmenu.add_command(label="Load game", command=self.load_game)
        mainmenu.add_command(label="Save", command=self.save)
        mainmenu.add_command(label="Exit", command=self._root.quit)

    def _add_canvas(self):
        self._root.title("Catch the Ribosome!")
        self.frame = Frame(self._root, bg='pink', bd=5)
        self._canvas = Canvas(self._root, width=WIDTH, height=HEIGHT, bg="peach puff")
        self._canvas.grid(row=0, column=0, sticky=(N, E, S, W))

    def new_game(self):
        answer = mb.askyesno(title="Question", message="Start new game?")
        if answer == True:
            self._canvas.delete()
            self.grid(row=0, column=0, sticky=(N, E, S, W))
            # self._add_menu()
            self._add_canvas()
            self.add_game(Game(frame, num_enemies))
            self._game.start()

    def load_game(self):
        save_file_name = self._get_load_file_name()
        with open(save_file_name, 'r', encoding='utf-8') as load_file:
            load_file.read()



    def _get_load_file_name(self):
        initialdir = os.path.expanduser(os.getcwd())
        if not os.path.exists(initialdir):
            initialdir = os.path.expanduser('~')
        save_file_name = filedialog.askopenfilename(
            initialdir=initialdir,
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
                "snake": self._game.snake,
                "score": self._game.score,
                "num enemies": self._game.num_enemies,
                "grid": self.grid,
                "lock": old_lock,
                "apple": self._game.block,
                "level": self._game.level,
                "num acids": self._game.num_acids,
                "sequence": self._game.sequence,
            }
            with open(save_file_name, 'w') as f:
                json.dump(saved_game, f)
        self.lock = old_lock

    def _get_save_file_name(self):
        initialdir = os.path.expanduser(os.getcwd())
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

######################################################################################

class Game:
    def __init__(self, frame, num_enemies, level = 1):
        self.frame = frame
        self.snake = self.create_snake()
        self.enemies = [self.create_enemy() for _ in range(num_enemies)]
        self.num_enemies = num_enemies
        self.score = 0
        self.block = cl.Block(SEG_SIZE, self.frame._canvas)
        self.level = level
        self.create_snake()



    def create_enemy(self):
        x = random.randint(100, 1000)
        y = random.randint(100, 1000)
        enemy_segments = [cl.Enemy_segment(x, y, self.frame._canvas),
                            cl.Enemy_segment(x +SEG_SIZE, y, self.frame._canvas ),
                            cl.Enemy_segment(x + 2*SEG_SIZE, y, self.frame._canvas )]
        enemy = cl.Enemy(enemy_segments, self.frame._canvas)
        return enemy


    def create_snake(self):
        segments = [cl.Segment(0, 300, self.frame._canvas),
                         cl.Segment(20, 300, self.frame._canvas),
                         cl.Segment(40, 300, self.frame._canvas),
                         cl.Segment(60, 300, self.frame._canvas),
                         cl.Segment(80, 300, self.frame._canvas)]
        self.snake = cl.Snake(segments, self.frame._canvas)

    def start(self):
        # catch keypressing
        self.frame._canvas.focus_set()
        # Reaction on keypress
        self.frame._canvas.bind("<KeyPress>", self.snake.change_direction)
        self.block.create_block()
        resume = self._is_game_over()
        if resume == False:
            if self.level == 1:
                self.main()

            elif self.level == 2:
                self.second_lvl()
        else:
            self._game_over()



    def main(self):
        self.snake.move()
        for enemy in self.enemies:
            enemy.move(self.frame._canvas)
        print('Hello!')
        snake_head = self.snake.segments[-1]._instance
        x1, y1, x2, y2 = snake_head
        turner_off = self._is_game_over()
        if  turner_off == True:
            self._game_over()
        # Check for collision with enemy
        else:
             for enemy in self.enemies:
                if fu.distance(self.snake, enemy, self.frame._canvas) < SEG_SIZE:
                    self.snake.delete_seg()
                    enemy.add_enemy_segment()
        # Eating apples
        if abs(x1 - self.block.x) <= SEG_SIZE and abs(y1 - self.block.y) <= SEG_SIZE:
            self.snake.add_segment(self.frame._canvas)
            self.block.delete_block()
            block = cl.Block(SEG_SIZE, self.frame._canvas)
            block.create_block()
            self.score += 1
        self.frame._root.after(100, self.main)

    def _is_game_over(self):
        x1, y1, x2, y2 = self.snake.segments[-1]._instance
        if  x1 < 0 or y1 < 0 or y2 > HEIGHT:
            return True
        elif x2 > WIDTH:
            self.level = 2
            return False
        # Check for collision with enemy
        elif self.snake.life == 0:
            return True
        # Self-eating
        else:
            for index in range(len(self.snake.segments) - 1):
                if self.snake.segments[0].instance == self.snake.segments[index].instance:
                    return True
        return False

    def _game_over(self):
        self.frame._canvas.create_text(WIDTH / 2, HEIGHT / 2,
                         text="GAME OVER!\n Your score: {}".format(self.score),
                         font=("Purisa", 20),
                         fill="red")

    def second_lvl(self):
        SecondLevel(self.score, self.frame._root)


########################################################################################

class SecondLevel(Game):
    def __init__(self):
        super().__init__()
        self._root = root
        self._sequence = self._generate_sequence()
        self._canvas = self._draw_canvas()
        self._buttons = self._add_buttons()

        self._rectangle = [230, 100, 280, 120]
        self._create_triplet_rectangle("#05f")

    @staticmethod
    def _generate_sequence():
        L = list(AminoAcidsDictionary[k] for k in AminoAcidsDictionary.keys())
        sequence = [random.choice(L) for _ in range(10)]
        sequence = 'AUG ' + ' '.join(sequence)
        return sequence

    def _update_triplet_rectangle(self):
        self._create_triplet_rectangle("peach puff")
        self._rectangle[0] += 48
        self._rectangle[2] += 48
        self._create_triplet_rectangle("#05f")

    def _create_triplet_rectangle(self, outline):
        self._canvas.create_rectangle(*self._rectangle,
                           outline=outline, fill=None)

    def _draw_canvas(self):
        c = Canvas(self._root, width=WIDTH, height=HEIGHT, bg="peach puff")
        c.grid(row=0, column=5, rowspan=5, columnspan=5, sticky=N + E + S + W)
        c.create_text(100, 50, anchor=N, font="Purisa",
                      text="Score {}".format(Score))
        x1 = 230
        y1 = 100
        x2 = 280
        y2 = 120
        c.create_rectangle(x1, y1, x2, y2,
                           outline="#05f", fill=None)
        c.create_text(500, 100, anchor=N, font="Purisa",
                      text="{}".format(self._sequence))
        return c
    #
    # def _add_amino_acids_commands(self):
    tmpl = """def {0}(self):
        pair = ['{0}', '{1}']
        self._add_amino_acid(pair)"""
    for amino_acid, triplet in AminoAcidsDictionary.items():
        func_def = tmpl.format(amino_acid, triplet)
        exec(func_def)

    @staticmethod
    def _add_button(row, col, name, command):
        b = Button(root, text=name, command=command)
        b.grid(row=row, column=col, sticky=S)
        return b

    def _add_buttons(self):
        buttons = []
        for i, amino_acid in enumerate(AminoAcidsDictionary):
            row = i // 5
            col = i % 5
            command = getattr(self, amino_acid)
            buttons.append(
                self._add_button(row, col, amino_acid, command)
            )
        return buttons

    def _add_amino_acid(self, pair):
        global Score
        if self._sequence == '':
            return self._canvas.create_text(500, 250, anchor=N, font=("Purisa", 40),
                          text="Congratulations! You win!\nYour score is {}".format(Score))
        if Score == 0:
            # gameover = PhotoImage(file="died.gif")
            # self._canvas.create_image(20, 200, image=gameover, anchor=N)
            self._canvas.create_text(500, 250, anchor=N, font=("Purisa", 40),
                          text="Game over! Botay bolshe!")
            pass
        else:
            triplet = self._sequence[:3]
            acid, triplet_user_selected = pair
            if triplet_user_selected == triplet:
                Score += 1
                r = lambda: random.randint(0, 255)
                color=str('#%02X%02X%02X' % (r(), r(), r()))
                x1, y1, x2, y2 = self._rectangle
                self._canvas.create_oval(x1-3, y1 + 30 - 3, x2 + 3, y2 + 30 + 3, fill=color, outline='black')
                color = str('#%02X%02X%02X' % (r(), r(), r()))
                self._canvas.create_text((x1 + x2)/2, (y1 + y2)/2 + 30, fill=color, font=("Purisa", 20), text='{}'.format(acid))
                self._update_triplet_rectangle()
                self._sequence = self._sequence[4:]
            else:
                self._canvas.create_text(300, 50, anchor=N, font="Purisa",
                              text="Wrong! Try another one")
                Score -= 1
            self._canvas.create_rectangle(25, 50, 150, 100, outline='peach puff',  fill="peach puff")
            self._canvas.create_text(100, 50, anchor=N, font="Purisa",
                          text="Score {}".format(Score))

########################################################################################
# How it should be
########################################################################################
root = Tk()
num_enemies = 4
frame = MainFrame(root)
game = Game(frame, num_enemies)
frame.add_game(game)
game.start()
game.frame._root.mainloop()