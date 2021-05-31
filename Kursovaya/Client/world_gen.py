from random import randint
from re import U
from ursina import *
from ursina.mesh_importer import get_blender


class Room(Entity):
    def __init__(self, position, scale):
        super().__init__()
        self.model = "level.obj"
        self.color = color.random_color()
        self.sides = ""
        self.position = position
        self.scale = scale
        self.collider = "mesh"


class World(Entity):
    def __init__(self):
        super().__init__()
        self.famaly_room = Room((0, -1, 0), scale=1.3)
        self.rooms = [self.famaly_room]
        self.sideschoise = {
            "l": (-24, 0, 0),
            "r": (24, 0, 0),
            "u": (0, 0, 24),
            "d": (0, 0, -24),
            "nl": "r",
            "nr": "l",
            "nu": "d",
            "nd": "u",
        }

    def generate_world(self):
        romms_total = randint(5, 15)
        for i in range(romms_total):
            room = self.rooms[randint(0, len(self.rooms) - 1)]
            sides = "lrud".replace(room.sides, "")
            side = sides[randint(0, len(sides) - 1)]
            room.sides += side
            NewRoom = Room(
                position=room.position + (self.sideschoise[side] * room.scale),
                scale=room.scale,
            )
            NewRoom.sides += self.sideschoise["n" + side]
            self.rooms.append(NewRoom)
