from tkinter import *
from tkinter import messagebox as mb
from math import *
import classes  as cl
import functions as fu

# Globals
WIDTH = 1000
HEIGHT = 500
SEG_SIZE = 20
# IN_GAME = True
Score = cl.Score(0)
##############################################################


def main(IN_GAME, Score, c):
    """ Handles game process """
    if IN_GAME:
        s.move(c)
        e.move(c)
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
        root.after(100, main, IN_GAME, Score, c)
        # Not IN_GAME -> stop game and print message
    else:
        return c.create_text(WIDTH / 2, HEIGHT / 2,
                  text="GAME OVER!",
                  font="Arial 20",
                  fill="red"), Score


##############################################################################




####################################################################




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
s = cl.Snake(segments)
e = cl.Enemy(enemy_segments)

# Reaction on keypress
c.bind("<KeyPress>", s.change_direction)

fu.create_block(c)
IN_GAME = True
main(IN_GAME, 0, c)
root.mainloop()


class MainFrame(Frame):
    def __init__(self, root, game):
        super().__init__()
        self._root = root
        self.grid(row=0, column=0, sticky=(S, E, N, W))
        self._game = game
        self._game.add_frame(self)
        self._add_menu()
        self._canvas = self._add_canvas()

    def _add_menu(self):
        mainmenu = Menu(root)
        self._root.config(menu=mainmenu)
        # Пропишем рамку
        frame = Frame(root, bg='pink', bd=5)
        self._root.config(menu=mainmenu)
        mainmenu.add_command(label="New game", command=fu.new_game)
        mainmenu.add_command(label="Load game", command=fu.load_game)
        mainmenu.add_command(label="Save", command=fu.save)
        mainmenu.add_command(label="Exit", command=self._root.quit)

    def new_game(self):
        answer = mb.askyesno(title="Question", message="Start new game?")
        if answer == True:
            self._game.restart()
            # self._canvas.delete(BLOCK)
            # self._game.snake.delete()
            # self._game.delete_enemies()
            # root = Tk()
            # c = Canvas(root, width=WIDTH, height=HEIGHT, bg="peach puff")
            # self._canvas.grid()
            #
            # # catch keypressing
            # self._canvas.focus_set()
            # # creating segments and snake
            # segments = [cl.Segment(10, 300, c),
            #             cl.Segment(30, 300, c),
            #             cl.Segment(50, 300, c),
            #             cl.Segment(70, 300, c),
            #             cl.Segment(90, 300, c)]
            #
            # enemy_segments = [cl.Enemy_segment(700, 400, c),
            #                   cl.Enemy_segment(720, 400, c),
            #                   cl.Enemy_segment(740, 400, c)]
            # s = cl.Snake(segments)
            # e = cl.Enemy(enemy_segments)
            #
            # # Reaction on keypress
            # self._canvas.bind("<KeyPress>", self._game.snake.change_direction)
            #
            # fu.create_block(c)
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


class Game:
    def __init__(self, num_enemies):
        self.snake = Snake()
        self.enemies = [Enemy() for _ in range(num_enemies)]