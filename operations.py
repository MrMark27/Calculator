from tkinter import *
import GUI
from math import sqrt

class PushButtonSum(Button):
    def __init__(self, window):
        super().__init__(text='=', width=3, bg='Light Blue', fg='Black', command= lambda: self.click(window))
        button_size = 10
        self.grid(ipady=button_size, ipadx=button_size)



    def click(self, click_ed):
        eq = str(click_ed.get())
        eq = eq.replace('√', 'sqrt')
        eq = eq.replace('÷', '/')
        eq= eq.replace('×', '*')

        eq = str(round(eval(eq), 4))
        click_ed.set(eq)


