
from src import * 

m = Menu("Some menu")

m.addOption("option 1", lambda btn: Application.exit())
m.addOption("option 2", lambda btn: Application.exit())
m.addOption("option 3", lambda btn: Application.exit())
m.addOption("option 4", lambda btn: Application.exit())
m.show()


Application.run()
