from numpy import positive
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from ursina import *


class Menu:
    def __init__(self):
        super().__init__()
        self.Menu = DropdownMenu(
            "Menu",
            buttons=(
                DropdownMenuButton("New Game"),
                DropdownMenuButton("Restart"),
                DropdownMenu(
                    "Options",
                    buttons=(
                        DropdownMenuButton("Fullscreen"),
                        DropdownMenuButton("Not Fullscreen"),
                    ),
                ),
                DropdownMenuButton("Exit"),
            ),
        )
        self.Menu.enabled = False
        self.scale = (0.7, 0.09, 0.5)
        self.start = DropdownMenuButton("Singlplayer", position=(-0.35, 0.3, 0))
        self.multi = DropdownMenuButton("Multiplayer", position=(-0.35, 0, 0))
        self.start.text_entity.x = 0.28
        self.multi.text_entity.x = 0.28
        self.start.scale, self.multi.scale = self.scale, self.scale

    def update(self):
        self.start.enabled, self.multi.enabled = self.Menu.enabled

    def input(self, key):
        if key == "left mouse down" and mouse.hovered_entity:
            text = mouse.hovered_entity.text
            if text == "Singlplayer":
                print("Singl")
            print(mouse.hovered_entity.text)
            self.Menu.close()
