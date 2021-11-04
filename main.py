from ursina import *

rotation_value = 3
x_movement = 0.05
border = 8


def update():
    global rotation_value
    global x_movement

    entity.rotation_z += rotation_value
    entity.x += x_movement

    if round(entity.x) == border:
        rotation_value = -3
        x_movement = -0.05

    elif round(entity.x) == -border:
        rotation_value = 3
        x_movement = 0.05


app = Ursina()

entity = Entity(model='cube', color=color.white, scale=(1, 1, 1))
entity.x = entity.y = entity.z = 0

app.run()
