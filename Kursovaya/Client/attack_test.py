from ursina import *
import time


class Attack(Entity):
    def __init__(self, start):
        super().__init__()
        self.cube = Entity(
            model="cube", parent=camera.ui, scale=(0.2, 1, 0.2), visible=False
        )
        self.tt = 0
        self.start = start
        self.on_left = False
        self.a = FrameAnimation3d(
            "Mesh/anim/anim_for_game_",
            rotation=(-90, 0, 0),
            fps=60,
            position=(0, -0.34, -20),
            scale=0.04,
            parent=camera.ui,
            billboard=True,
            always_on_top=True,
        )
        self.a.resume()
    def at_the_moment(self):
        if (
            (self.a.sequence.t > 0.40 and self.a.sequence.t < 0.65)
            or (self.a.sequence.t > 0.90 and self.a.sequence.t < 1.15)
            or (self.a.sequence.t > 1.40 and self.a.sequence.t < 1.65)
            or (self.a.sequence.t > 1.90 and self.a.sequence.t < 2.15)
        ):
            return True

    def input(self, key):
        global on_left
        played = False
        if (
            key == "left mouse down"
            and self.on_left
            and self.at_the_moment()
            and self.start
        ):
            self.cube.animate_rotation((30, 0, 30))
            self.cube.animate_position((0.5, -0.5, 0))
            self.on_left = False
            return 0
        if (
            key == "left mouse down"
            and not self.on_left
            and self.at_the_moment()
            and self.start
        ):
            self.cube.visible = True
            self.cube.animate_rotation((30, 0, -30))
            self.cube.animate_position((-0.5, -0.5, 0))
            self.on_left = not self.on_left
            return 0
