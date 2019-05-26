import random
from tkinter import *
from tkinter import messagebox as mb
from math import *
import classes  as cl
import functions as fu
import frame as fr

# Globals
WIDTH = 1000
HEIGHT = 500
SEG_SIZE = 20
Score = 0
##############################################################

def next():
    c.destroy()
    second_lvl(Score, root)

def second_lvl(Score, root):
    c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
    c.grid(row=0, column=0, sticky=(N, E, S, W))
    # catch keypressing
    c.focus_set()
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
    X = 0
    Y = 0
    for acid in AminoAcidsDictionary.keys():
        Button(root, text="{}".format(acid), command=fu.score).grid(row=X, column=Y, sticky=N+W+E+S, padx=50)
        if Y == 5:
            X+=1
        Y +=1


##############################################################


def main(IN_GAME, Score, c, apple):
    """ Handles game process """
    if IN_GAME:
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
            c.create_text(WIDTH / 2, HEIGHT / 2,
                             text="GOOD JOB!",
                             font="Arial 20",
                             fill="red")
            Next = Button(c, text="Next", command=next)
            Next.grid(pady=100, padx=100)
            Next.callback()
        if x11 < 0 or y11 < 0 or y12 > HEIGHT:
            IN_GAME = False
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
            c.create_text(100, 50, anchor=N, font="Purisa",
                          text="Score {}".format(Score))
        # Self-eating
        else:
            for index in range(len(s.segments) - 1):
                if s_head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
                    pass
        root.after(100, main, IN_GAME, Score, c, apple)
        # Not IN_GAME -> stop game and print message
    else:
        c.create_text(WIDTH / 2, HEIGHT / 2,
              text="GAME OVER!",
              font="Arial 20",
              fill="red"), Score


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
Button(root, text="Score {}", command=fu.score).grid(ipadx=100, ipady=20)

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
    text="Score 0")
main(IN_GAME, 0, c, apple)
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
