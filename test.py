
from src import * 

Application.addColor("test", "dark green", "")
Application.init()


def printMe(b, s):
    print(s)


m = Menu("Some menu")

textin = TextInput("Enter something", lambda ans: Application.exit())

msg = MessageBox("Your choice", "You have selected the first option")

menubox2 = MenuBox("second menu box")
menubox2.addOption("exit", lambda btn, x: 0)


menubox = MenuBox("Select something")
menubox.addOption("Print dialog", lambda btn, x: MessageBox("Dialog", "This is dialog").exec())
menubox.addOption("Show menubox", lambda btn, x: menubox2.exec())
menubox.addOption("exit", lambda x: 0)


table = Table("test table", ["A", "B"], [["1", "2"], ["3", "4"]], lambda i,j: MessageBox("Your selection", "%d %d" % (i,j)).exec())

m.addOption("option 1", lambda btn,x: msg.exec())
m.addOption("Show menubox", lambda btn,x: menubox.exec())
m.addOption("option 3", lambda btn,x: Application.exit())
m.addOption("option 4", lambda btn,x: textin.show(), "test")
m.addOption("Show table", lambda btn, x: table.show())

strings = [
    "a",
    "b"
]

for string in strings:
    m.addOption("Print %s" % string, printMe, params=[string])

m.show()


Application.run()
