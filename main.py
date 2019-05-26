import random
from math import *
from collections import OrderedDict

from tkinter import *
from tkinter import messagebox as mb

import classes  as cl
import functions as fu
import frame as fr

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
class SecondLevel:
    def __init__(self, Score, root):
        self.Score = Score
        self._root = root
        self._sequence = self._generate_sequence()
        self._canvas = self._draw_canvas()
        self._buttons = self._add_buttons()

        self._rectangle = [250, 100, 400, 120]
        self._create_triplet_rectangle("#05f")


    @staticmethod
    def _generate_sequence():
        L = list(AminoAcidsDictionary[k] for k in AminoAcidsDictionary.keys())
        sequence = [random.choice(L) for _ in range(10)]
        sequence = 'AUG ' + ' '.join(sequence)
        return sequence

    def _update_triplet_rectangle(self):
        self._create_triplet_rectangle("peach puff")
        self._rectangle[0] += 30
        self._rectangle[2] += 30
        self._create_triplet_rectangle("#05f")

    def _create_triplet_rectangle(self, outline):
        self._canvas.create_rectangle(*self._rectangle,
                           outline=outline, fill=None)

    def _draw_canvas(self):
        c = Canvas(self._root, width=WIDTH, height=HEIGHT, bg="peach puff")
        c.grid(row=0, column=5, rowspan=5, columnspan=5, sticky=N + E + S + W)
        c.create_text(100, 50, anchor=N, font="Purisa",
                      text="Score {}".format(Score))
        x1 = 250
        y1 = 100
        x2 = 400
        y2 = 120
        c.create_rectangle(x1, y1, x2, y2,
                           outline="#05f", fill=None)
        c.create_text(500, 100, anchor=N, font="Purisa",
                      text="{}".format(self._sequence))
        return c
    #
    # def _add_amino_acids_commands(self):
    tmpl = """def {0}(self):
        pair = ['{1}', '{0}']
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
        triplet = self._sequence[:3]
        triplet_user_selected, acid = pair
        if AminoAcidsDictionary[acid] == triplet:
            Score += 1
        else:
            self._canvas.create_text(100, 50, anchor=N, font="Purisa",
                          text="Wrong! Try another one")
            Score -= 1
        self._update_triplet_rectangle()
        self._sequence = self._sequence[3:]

    # def gly(self):
    #     print("gly method!")
    #     self.var = ['GGG', 'Gly']
    #     self.add_amino_acid()
    #
    # def pro(self):
    #     self.var = ['CCC', 'Pro']
    #
    # def asp(self):
    #     self.var = ['GAU', 'Asp']
    #
    # def glu(self):
    #     self.var = ['GAG', 'Glu']
    #
    # def ala(self):
    #     self.var = ['GCC', 'Ala']
    #
    # def asn(self):
    #     self.var = ['AAU', 'Asn']
    #
    # def gln(self):
    #     self.var = ['CAA', 'Gln']
    #
    # def ser(self):
    #     self.var = ['UCC', 'Ser']
    #
    # def thr(self):
    #     self.var = ['ACA', 'Thr']
    #
    # def lys(self):
    #     self.var = ['AAA', 'Lys']
    #
    # def arg(self):
    #     self.var = ['AGG', 'Arg']
    #
    # def his(self):
    #     self.var = ['CAC', 'His']
    #
    # def val(self):
    #     self.var = ['GUC', 'Val']
    #
    # def ile(self):
    #     self.var = ['AUU', 'Ile']
    #
    # def met(self):
    #     self.var = ['AUG', 'Met']
    #
    # def cys(self):
    #     self.var = ['UGC', 'Cys']
    #
    # def leu(self):
    #     self.var = ['CUU', 'Leu']
    #
    # def phe(self):
    #     self.var = ['UUU', 'Phe']
    #
    # def tyr(self):
    #     self.var = ['UAU', 'Tyr']
    #
    # def trp(self):
    #     self.var = ['UGG', 'Trp']


def second_lvl(Score, root):
    c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
    c.grid(row=0, column=5, rowspan=5, columnspan=5, sticky=N+E+S+W)
    c.create_text(100, 50, anchor=N, font="Purisa",
                  text="Score {}".format(Score))

    x1 = 250
    y1 = 100
    x2 = 400
    y2 = 120
    L = list(AminoAcidsDictionary[k] for k in AminoAcidsDictionary.keys())
    sequence = [random.choice(L) for _ in range(10)]
    sequence = 'AUG ' + ' '.join(sequence)
    seq = sequence
    res = SecondLevel(seq)
    c.create_rectangle(x1, y1, x2, y2,
                            outline="#05f", fill=None)
    c.create_text(500, 100, anchor=N, font="Purisa",
                  text="{}".format(seq))

    Gly = Button(root, text="Gly", command=res.gly)
    Gly.grid(row=0, column=0, sticky=S)
    Pro = Button(root, text="Pro", command=res.pro)
    Pro.grid(row=0, column=1, sticky=S)
    Asp = Button(root, text="Asp", command=res.asp)
    Asp.grid(row=0, column=2, sticky=S)
    Glu = Button(root, text="Glu", command=res.glu)
    Glu.grid(row=0, column=3, sticky=S)
    Ala = Button(root, text="Ala", command=res.ala)
    Ala.grid(row=0, column=4, sticky=S)
    Asn = Button(root, text="Asn", command=res.asn)
    Asn.grid(row=1, column=0, sticky=S)
    Gln = Button(root, text="Gln", command=res.gln)
    Gln.grid(row=1, column=1, sticky=S)
    Ser = Button(root, text="Ser", command=res.ser)
    Ser.grid(row=1, column=2, sticky=S)
    Thr = Button(root, text="Thr", command=res.thr)
    Thr.grid(row=1, column=3, sticky=S)
    Lys = Button(root, text="Lys", command=res.lys)
    Lys.grid(row=1, column=4, sticky=S)
    Arg = Button(root, text="Arg", command=res.arg)
    Arg.grid(row=2, column=0, sticky=S)
    His = Button(root, text="His", command=res.his)
    His.grid(row=2, column=1, sticky=S)
    Val = Button(root, text="Val", command=res.val)
    Val.grid(row=2, column=2, sticky=S)
    Ile = Button(root, text="Ile", command=res.ile)
    Ile.grid(row=2, column=3, sticky=S)
    Met = Button(root, text="Met", command=res.met)
    Met.grid(row=2, column=4, sticky=S)
    Cys = Button(root, text="Cys", command=res.cys)
    Cys.grid(row=3, column=0, sticky=S)
    Leu = Button(root, text="Leu", command=res.leu)
    Leu.grid(row=3, column=1, sticky=S)
    Phe = Button(root, text="Phe", command=res.phe)
    Phe.grid(row=3, column=2, sticky=S)
    Tyr = Button(root, text="Tyr", command=res.tyr)
    Tyr.grid(row=3, column=3, sticky=S)
    Trp = Button(root, text="Trp", command=res.trp)
    Trp.grid(row=3, column=4, sticky=S)
    # Check sequence
    seq = ''.join(seq.split())
    while len(seq) > 0:
        triplet = seq[:3]
        while True:
            if res.var:
                trio, acid = res.var
                if AminoAcidsDictionary[triplet] == acid:
                    Score += 1
                else:
                    c.create_text(100, 50, anchor=N, font="Purisa",
                                  text="Wrong! Try another one")
                    Score -= 1
                c.create_rectangle(100, 50, 120, 100, outline=None, fill="peach puff")
                c.create_text(100, 50, anchor=N, font="Purisa",
                                  text="Score {}".format(Score))
                c.create_rectangle(x1, y1, x2, y2,
                                   outline="peach puff", fill=None)
                c.create_rectangle(x1+30, y1, x2+30, y2,
                                   outline="#05f", fill=None)
                x1 += 30
                x2 += 30
                seg = seg[3:]




def next():
    c.destroy()
    sl = SecondLevel(Score, root)

    # second_lvl(Score, root)
##############################################################


def main(IN_GAME, first_stage, Score, c, apple):
    """ Handles game process """
    if IN_GAME:
        if first_stage:
            s.move(c)
            e.move(c)
            e2.move(c)
            e3.move(c)
            for segm in s.segments:
                print(c.coords(segm.instance))
            s_head_coords = c.coords(s.segments[-1].instance)
            x11, y11, x12, y12 = s_head_coords
            # Check for collision with gamefield edges
            if x12 > WIDTH:
                first_stage = False
                # Next.next()
                pass
                # second_lvl(Score, root)
            elif x11 < 0 or y11 < 0 or y12 > HEIGHT:
                IN_GAME = False
                c.create_text(WIDTH / 2, HEIGHT / 2,
                              text="GAME OVER!",
                              font="Arial 20",
                              fill="red")
                pass
            # Check for collision with enemy
            elif fu.distance(s, e, c) < SEG_SIZE:
                # тут сразу и жизнь режется
                s.delete_seg(c)
                e.add_enemy_segment(c)
            elif fu.distance(s, e2, c) < SEG_SIZE:
                s.delete_seg(c)
                e2.add_enemy_segment(c)
            elif fu.distance(s, e3, c) < SEG_SIZE:
                s.delete_seg(c)
                e3.add_enemy_segment(c)
            # elif s.life == 0:
            #     IN_GAME = False
            # Eating apples
            elif abs(x11 - apple.x) <= SEG_SIZE and abs(y11 - apple.y) <= SEG_SIZE:
                s.add_segment(c)
                apple.delete_block()
                apple = cl.Block(SEG_SIZE, c)
                Score += 1
                # context = c.getContext('2d')
                # context.getContext("2d").clearRect(100, 50, 10, 10)
                c.create_rectangle(125, 50, 150, 100, outline=None,  fill="peach puff")
                c.create_text(100, 50, anchor=N, font="Purisa",
                              text="Score {}".format(Score))
            # Self-eating
            else:
                for index in range(len(s.segments) - 1):
                    if s_head_coords == c.coords(s.segments[index].instance):
                        IN_GAME = False
                        c.create_text(WIDTH / 2, HEIGHT / 2,
                                      text="GAME OVER!",
                                      font="Arial 20",
                                      fill="red"), Score
                        pass
            root.after(100, main, IN_GAME, first_stage, Score, c, apple)
        # Not IN_GAME -> stop game and print message
        else:
            c.create_text(WIDTH / 2, HEIGHT / 2,
                          text="GOOD JOB!",
                          font="Arial 20",
                          fill="red")
            Next = Button(c, text="Next", command=next)
            Next.grid(pady=100, padx=100)
            return Score
    else:
        c.create_text(WIDTH / 2, HEIGHT / 2,
              text="GAME OVER!",
              font="Arial 20",
              fill="red")



##############################################################################
# Setting up window
##############################################################################
root = Tk()
root.title("Catch the Ribosome!")
# Creating frame
frame = Frame(root, bg='pink', bd=5)
# Making menu string
mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="New game", command=fu.new_game)
mainmenu.add_command(label="Load game", command=fu.load_game)
mainmenu.add_command(label="Save", command=fu.save)
mainmenu.add_command(label="Exit", command=root.quit)
# Button(root, text="Score {}", command=fu.score).grid(ipadx=100, ipady=20)

####################################################################

# Drawing canvas
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
# c.place(relx=-5, rely=-1, anchor=CENTER)
c.grid(row=0, column = 0,  sticky=(N, E, S, W))
# catch keypressing
c.focus_set()
# creating segments and snake
segments = [cl.Segment(0, 300, c),
                cl.Segment(20, 300, c),
                cl.Segment(40, 300, c),
                cl.Segment(60, 300, c),
                cl.Segment(80, 300, c)]

enemy_segments = [cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
                  cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
                  cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)]
s = cl.Snake(segments)
e = cl.Enemy(enemy_segments)
e2 = cl.Enemy([cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
                  cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
                  cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)])
e3 = cl.Enemy([cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
                  cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c),
                  cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500), c)])
# Reaction on keypress
c.bind("<KeyPress>", s.change_direction)
# Creating an apple
apple = cl.Block(SEG_SIZE, c)
# apple.instance
IN_GAME = True
c.create_text(100, 50, anchor=N, font="Purisa",
    text="Score {}".format(Score))
main(IN_GAME, True, Score, c, apple)
root.mainloop()

##########################################################################################
# Classes MainFrame and Game
##########################################################################################

class MainFrame(Frame):
    def __init__(self, root):
        super().__init__()
        self._root = root
        self.grid(row=0, column=0, sticky=(N, E, S, W))
        self._game = None
        # self._game.add_frame(self)
        self._add_menu()
        self._canvas = self._add_canvas()

    def add_game(self, game):
        self._game = game

    def _add_menu(self):
        mainmenu = Menu(self._root)
        self._root.config(menu=mainmenu)
        # Пропишем рамку
        frame = Frame(self._root, bg='pink', bd=5)
        self._root.config(menu=mainmenu)
        mainmenu.add_command(label="New game", command=fu.new_game)
        mainmenu.add_command(label="Load game", command=fu.load_game)
        mainmenu.add_command(label="Save", command=fu.save)
        mainmenu.add_command(label="Exit", command=self._root.quit)

    def _add_canvas(self):
        self._root.title("Catch the Ribosome!")
        self.frame = Frame(self._root, bg='pink', bd=5)
        self._canvas = Canvas(self._root, width=WIDTH, height=HEIGHT, bg="peach puff")
        self._canvas.grid(row=0, column=0, sticky=(N, E, S, W))


    def new_game(self):
        answer = mb.askyesno(title="Question", message="Start new game?")
        if answer == True:
            self._canvas.clear()
            self.game.start()

    def load_game(root):
        filewin = Toplevel(root)
        button = Button(filewin, text="Load game")
        button.pack()

    def save(root):
        filewin = Toplevel(root)
        button = Button(filewin, text="Save progress")
        button.pack()



######################################################################################

class Game:
    def __init__(self, frame, num_enemies):
        self.frame = frame
        self.snake = self.create_snake()
        self.enemies = [self.create_enemy() for _ in range(num_enemies)]
        self.score = 0
        self.block = cl.Block(SEG_SIZE, self.frame._canvas)

    def create_enemy(self):
        enemy_segments = [cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500) ),
                            cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500) ),
                            cl.Enemy_segment(random.randint(100, 1000), random.randint(100, 500) )]
        enemy = cl.Enemy(enemy_segments, self.frame._canvas)
        return enemy


    def create_snake(self):
        segments = [cl.Segment(0, 300),
                         cl.Segment(20, 300),
                         cl.Segment(40, 300),
                         cl.Segment(60, 300),
                         cl.Segment(80, 300)]
        self.snake = cl.Snake(segments, self.frame._canvas)

    def start(self):
        resume = self._is_game_over()
        if not resume:
            main()
            root.mainloop()

    def add_frame(self):

        self.canvas.destroy()
        # context = c.getContext('2d')
        # context.getContext("2d").clearRect(100, 50, 10, 10)
        c.create_text(100, 50, anchor=N, font="Purisa",
                      text="Score {}".format(Score))

    def second_lvl(self):
        self.frame._canvas.destroy()
        self.frame._canvas = self.frame._add_canvas()
        AminoAcidsDictionary = {'Gly': 'GGG',
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
        X = 200
        Y = 250
        for acid in AminoAcidsDictionary.keys():
            acid = Button(self.frame._root, text="{}".format(acid), command=fu.score).grid(ipadx=X, ipady=Y)
            acid.grid()
            X += 20





    def main(self):
        self.block.instance()
        self.snake.move(c)
        for e in self.enemies:
            e.move(c)
        snake_head = c.coords(self.snake.segments[-1].instance)
        x1, y1, x2, y2 = snake_head
        if self._is_game_over():
            self._game_over()
        # Check for collision with enemy
        else:
             for enemy in self.enemies:
                if fu.distance(s, enemy, c) < SEG_SIZE:
                    self.snake.delete_seg()
                    enemy.add_enemy_segment()
        # Eating apples
        if abs(x1 - self.block.x) <= SEG_SIZE and abs(y1 - self.block.y) <= SEG_SIZE:
            self.snake.add_segment(c)
            self.block.delete_block()
            block = cl.Block(SEG_SIZE, c)
            self.score += 1
        root.after(100, main)

    def _is_game_over(self):
        result = False
        x1, y1, x2, y2 = self.snake.segments[-1].instance
        if  x1 < 0 or y1 < 0 or y2 > HEIGHT:
            result = True
            self._game_over()
        elif x2 > WIDTH:
            self.second_lvl()
        # Check for collision with enemy
        elif self.snake.life == 0:
            result = True
            self._game_over()
        # Self-eating
        else:
            for index in range(len(s.segments) - 1):
                if self.snake.coords[0] == c.coords(s.segments[index].instance):
                    result = True
                    self._game_over()
        return result




    def _game_over(self):
        c.create_text(WIDTH / 2, HEIGHT / 2,
                         text="GAME OVER!\n Your score: {}".format(self.score),
                         font="Arial 20",
                         fill="red")

########################################################################################
# How it should be
########################################################################################
# root = Tk()
# num_enemies = 2
# frame = MainFrame(root)
# game = Game(frame, num_enemies)
# frame.add_game(game)
