
from src import * 

Application.addColor("test", "dark green", "")
Application.init()


def printMe(b, s):
    print(s)


m = Menu("Some menu")

textin = TextInput("Enter something", lambda ans: Application.exit())

msg = MessageBox("Your choice", "You have selected the first option")

menubox = MenuBox("Select something")
menubox.addOption("Print dialog", lambda x: MessageBox("Dialog", "This is dialog").exec())
menubox.addOption("exit", lambda x: 0)

table = Table("test table", ["A", "B"], [["1", "2"], ["3", "4"]], lambda i,j: MessageBox("Your selection", "%d %d" % (i,j)).exec())

m.addOption("option 1", lambda btn: msg.exec())
m.addOption("option 2", lambda btn: menubox.exec())
m.addOption("option 3", lambda btn: Application.exit())
m.addOption("option 4", lambda btn: textin.show(), "test")
m.addOption("Show table", lambda btn, x: table.show())

strings = [
    "a",
    "b"
]

for string in strings:
    m.addOption("Print %s" % string, printMe, params=[string])

m.show()


Application.run()
