from tkinter import *
import widgets
import operations


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        super().__init__()
        self.parent = parent
        t = StringVar()
        equaction = ""
        i = 1  # crating numeric keyboard from 1 to 9
        while i <= 9:
            for x in reversed(range(2, 5)):
                for y in range(0, 3):
                    widgets.PushButton(i, t).grid(row=x, column=y)
                    i += 1

        widgets.PushButton('-/+', t).grid(row=5, column=0)
        widgets.PushButton('0', t).grid(row=5, column=1)
        widgets.PushButton('.', t).grid(row=5, column=2)

        widgets.PushButton('÷', t).grid(row=1, column=4)
        widgets.PushButton('×', t).grid(row=2, column=4)
        widgets.PushButton('-', t).grid(row=3, column=4)
        widgets.PushButton('+', t).grid(row=4, column=4)
        operations.PushButtonSum(t).grid(row=5, column=4)

        widgets.PushButton('C', t).grid(row=1, column=0, columnspan=2, ipadx=36)
        widgets.PushButton('√x', t).grid(row=1, column=2)

        Entry(justify=RIGHT, font=(NONE, 20), width=13, textvariable=t).grid(row=0, columnspan=5)
