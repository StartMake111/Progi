from subprocess import run
from ursina import *

app = Ursina()

a = Entity(model="sphere", rotation=(45, 45, 0), color=color.green)

app.run()
