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