

from .Dialog import * 

class MenuBox(Dialog):
    
    def __init__(self, title):
        self.title = title
        self.options = []

    def addOption(self, description, func):
        def f(b):
            self.exit()
            func(b)
        self.options.append((description, f))
    
    def getDialog(self):
        body = []
        for o in self.options:
            c, f = o
            button = urwid.Button(c)
            urwid.connect_signal(button, 'click', f)
            body.append(urwid.AttrMap(button, "button", focus_map='focus'))
        l = urwid.BoxAdapter(urwid.ListBox(urwid.SimpleFocusListWalker(body)), 5)
        return urwid.Pile([
            urwid.Text(self.title),
            urwid.Divider("-"),
            l,
        ])
