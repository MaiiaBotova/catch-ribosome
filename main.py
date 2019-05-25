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
        if x12 > WIDTH or x11 < 0 or y11 < 0 or y12 > HEIGHT:
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
        return c.create_text(WIDTH / 2, HEIGHT / 2,
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
# Button(root, text="Score {}".format(Score), command=fu.score).grid(ipadx=100, ipady=20)

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
apple.instance
IN_GAME = True
c.create_text(100, 50, anchor=N, font="Purisa",
    text="Score 0")
main(IN_GAME, 0, c, apple)
root.mainloop()
########################################################################################
# How it should be
########################################################################################

frame = MainFrame(root)
game = Game(frame, num_enemies)
frame.add_game(game)

##########################################################################################
# Classes MainFrame and Game
##########################################################################################

class MainFrame(Frame):
    def __init__(self, root, game):
        super().__init__()
        self._root = root
        self.grid(row=0, column=0, sticky=(N, E, S, W))
        self._game = None
        self._game.add_frame(self)
        self._add_menu()
        self._canvas = self._add_canvas()

    def add_game(self, game):
        self._game = game

    def _add_menu(self):
        mainmenu = tk.Menu(self.root)
        self._root.config(menu=mainmenu)
        # Пропишем рамку
        frame = tk.Frame(self.root, bg='pink', bd=5)
        self._root.config(menu=mainmenu)
        mainmenu.add_command(label="New game", command=fu.new_game)
        mainmenu.add_command(label="Load game", command=fu.load_game)
        mainmenu.add_command(label="Save", command=fu.save)
        mainmenu.add_command(label="Exit", command=self._root.quit)

    def _add_canvas(Canvas):
        super.__init__()








    def new_game(self):
        answer = mb.askyesno(title="Question", message="Start new game?")
        if answer == True:
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



######################################################################################

class Game:
    def __init__(self, num_enemies):
        self.snake = cl.Snake()
        self.enemies = [cl.Enemy() for _ in range(num_enemies)]
        self.score = 0
        self.block = block

    def start(self):
        self._move()
        resume = self._is_game_over()
        if resume:
            main()
            root.mainloop()

    def _is_game_over(self, snake, enemy):
        x1, y1, x2, y2 = snake.coords
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            self._game_over()
        # Check for collision with enemy
        elif fu.distance(s, e, c) < SEG_SIZE:
            # тут сразу и жизнь режется
            snake.delete_seg()
            enemy.add_enemy_segment()
        elif snake.life == 0:
            self._game_over()
        # Self-eating
        else:
            for index in range(len(s.segments) - 1):
                if snake.coords[0] == c.coords(s.segments[index].instance):
                    self._game_over()

    def _game_over(self):
        c.create_text(WIDTH / 2, HEIGHT / 2,
                         text="GAME OVER!\n Your score: {}".format(self.score),
                         font="Arial 20",
                         fill="red")


