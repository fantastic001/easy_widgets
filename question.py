
import urwid

palette = [
    ('button', '', ''),
    ('focused', 'white', 'light blue'),
    ('bg', '', ''),
]
main = urwid.Padding(urwid.Text(""),  left=2, right=2)

def get_answer(btn, edit):
    msg = edit.edit_text
    main.original_widget = urwid.Text(msg, align="center")

def question(message):
    e = urwid.Edit(message + "\n", align="center")
    l = [
        urwid.AttrMap(e, "", focus_map="focused"),
        urwid.Padding(urwid.AttrMap(urwid.Button("OK", get_answer, e), "", focus_map="focused"), align="center", left=10, right=10)
    ]
    return urwid.Pile(l)

main.original_widget = question("blah")

loop = urwid.MainLoop(urwid.Filler(main), palette)

loop.run()
