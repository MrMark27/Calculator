from tkinter import ttk


class PushButton(ttk.Button):
    def __init__(self, name, equacion):
        super().__init__(text=name, width=3, command=lambda: self.click(equacion, name), cursor="hand2")

        button_size = 11

        self.grid(ipady=button_size, ipadx=button_size)

    def click(self, click_ed, name):
        if name == 'C':
            click_ed.set('')
            name = ""
        elif name == '-/+':
            name = click_ed.get()
            if name[0:2] == '-(' and name[-1] == ')':
                name = name[2:(len(name)-1)]
            else:
                name = f'-({name})'
            click_ed.set(name)
            name = ''
        elif name == '√x':
            name = click_ed.get()
            if name[0:2] == '√(' and name[-1] == ')':
                name = name[2:(len(name)-1)]
            else:
                name = f'√({name})'
            click_ed.set(name)
            name = ''
        name = click_ed.get() + str(name)
        click_ed.set(name)
