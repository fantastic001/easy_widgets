
import urwid

widget = urwid.WidgetPlaceholder(None)

main = urwid.Padding(widget, left=5, right=5)


palette = [
    ('button', '', ''),
    ('focus', 'white', 'light blue'),
    ('bg', '', ''),
]

loop = urwid.MainLoop(main, palette)

widgets = []

class Application(object):
    
    def run():
        loop.run()

    def addColor(name, fg, bg):
        palette.append((name, fg, bg))

    def setWidget(w):
        widgets.append(widget.original_widget)
        widget.original_widget = w

    def exit():
       raise urwid.ExitMainLoop() 
