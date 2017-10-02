
from .Widget import * 

class Menu(Widget):
    
    def __init__(self, title):
        self.title = title
        self.options = []
    def addOption(self, description, func):
        self.options.append((description, func))

    def getWidget(self):
        body = [urwid.Text(self.title), urwid.Divider()]
        for o in self.options:
            c, f = o
            button = urwid.Button(c)
            urwid.connect_signal(button, 'click', f)
            body.append(urwid.AttrMap(button, "button", focus_map='focus'))
        return urwid.Padding(urwid.ListBox(urwid.SimpleFocusListWalker(body)), left=5, right=5)
        
