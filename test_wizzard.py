
from src import * 

Application.init()

menu = Menu("Just exit now")
menu.addOption("OK", lambda b,p: Application.exit())


name = ""
times = 0 

def setName(x):
    global name 
    name = x
def setTimes(x):
    global times 
    times = x

w = Wizzard(menu)\
    .withChoices("Select number", "times", [(1, "one"), (2, "two")])\
    .withInput("Enter your name", "name")\
    .withParam("name", setName)\
    .withParam("times", setTimes)


w.show()

Application.run()
print(name * times)


