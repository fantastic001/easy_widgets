import urwid

palette = [
    ('banner', 'white', 'light red'),
    ('streak', 'white', 'light blue'),
    ('bg', '', ''),
]


main = urwid.Padding(urwid.Text("Loading"))

def quit(btn):
    raise urwid.ExitMainLoop()


def submit(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'Ok')
    urwid.connect_signal(done, 'click', quit)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='banner')]))

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', submit, c)
        body.append(urwid.AttrMap(button, None, focus_map='streak'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

choices = ["2.x", "3.x"]

main = urwid.Padding(menu(u'Pythons', choices), left=2, right=2)


loop = urwid.MainLoop(main, palette)

loop.run()
