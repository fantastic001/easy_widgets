
from src import * 

Application.init()

m = Menu("Some menu")

textin = TextInput("Enter something", lambda ans: Application.exit())

msg = MessageBox("Your choice", "You have selected the first option")

m.addOption("option 1", lambda btn: msg.exec())
m.addOption("option 2", lambda btn: Application.exit())
m.addOption("option 3", lambda btn: Application.exit())
m.addOption("option 4", lambda btn: textin.show())
m.show()


Application.run()
