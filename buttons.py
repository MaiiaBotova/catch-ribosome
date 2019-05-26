from tkinter import *
import random
from tkinter import messagebox as mb
from math import sqrt


def new_game(root):
    pass


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