from numpy import positive
from ursina import *
from ursina import hit_info
from ursina.hit_info import HitInfo
from ursina.prefabs.trail_renderer import TrailRenderer


class Oneplayer(Entity):
    def __init__(self, inv, hb, **kwargs):
        super().__init__()
        self.speed = 5
        self.origin_y = 0
        self.camera_pivot = Entity(parent=self, y=2)
        self.cursor = Entity(
            parent=camera.ui, model="quad", color=color.pink, scale=0.008, rotation_z=45
        )
        self.level = 1
        self.exp = 0
        camera.parent = self.camera_pivot
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        mouse.locked = False
        self.weapon = None
        self.inv = inv
        self.hb = hb
        self.mouse_sensitivity = Vec2(40, 40)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _if_death(self):
        for i in scene.entities:
            print(i)
            i.enabled = False

    def update(self):
        if self.enabled:
            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]
            self.camera_pivot.rotation_x -= (
                mouse.velocity[1] * self.mouse_sensitivity[0]
            )
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)
            self.direction = Vec3(
                self.forward * (held_keys["w"] - held_keys["s"])
                + self.right * (held_keys["d"] - held_keys["a"])
            ).normalized()
            origin = self.world_position + (self.up * 0.5)
            hit_info = raycast(
                origin, self.direction, ignore=(self,), distance=0.5, debug=False
            )
            if not hit_info.hit:
                self.position += self.direction * self.speed * time.dt

    def to_json(self):
        return "{'position' : pos}".replace("pos", self.position)


class Enemy(Entity):
    def __init__(self, player, hb, exp, inv, position, **kwargs):
        super().__init__()
        self.model = "lowpolybody"
        self.color = color.yellow
        self.position = position
        self.player = player
        self.scale = 1.4
        self.bullets = 0
        self.hb = hb
        self.exp = exp
        self.time_from_attack = 1
        self.hp_value = 100
        self.collision = True
        self.collider = BoxCollider(self, (0, 1, 0), (1, 2, 1))
        self.inv = inv
        self.origi = self.world_position
        tool = Tooltip(text=str(self.hp_value), parent=camera.ui, enabled=False)
        self.hit_info = raycast(
            self.origi,
            Vec3(self.forward).normalized(),
            ignore=(self,),
            distance=1,
            debug=True,
        )

    def move_to_player(self, other):
        x, y, z = other.position - self.position
        xyz = x ** 2 + y ** 2 + z ** 2
        if xyz > 1 and not self.hit_info.hit:
            self.position += (other.position - self.position) * 0.004
            self.time_from_attack = 1
        elif xyz <= 1:
            self.time_from_attack += time.dt
            if self.time_from_attack > 1:
                self.time_from_attack = 0
                self.attack()
        self.look_at(self.player)

    def attack(self):
        self.hb.value -= 10

    def update(self):
        self.move_to_player(self.player)
        if self.hb.value == 0:
            self.player.exp += 20
            destroy(self)
        if self.hp_value <= 0:
            self.collision = False
            self.collider.remove()
            destroy(self)
            self.inv.add_item(self.player.level)
            self.player.exp += 20
            self.exp.value += 20

    def to_json(self):
        return (
            "{'position': pos,'health_value':hp}".replace("pos", self.position)
        ).replace("hp", self.hp_value)
