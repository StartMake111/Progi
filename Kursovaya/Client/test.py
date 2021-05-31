from os import spawnle
from re import L, T
from subprocess import run
from sys import float_repr_style
from typing import Tuple
from numpy import heaviside, positive
from ursina import *
from random import randint
from ursina.application import load_settings
from ursina.prefabs.health_bar import HealthBar
from Inventory import Inventory
from Entities import Oneplayer, Enemy
from world_gen import World
from attack_test import Attack
from tooltips import Menu
from ursina.prefabs.file_browser_save import FileBrowserSave
from ursina.prefabs.exit_button import ExitButton
import json

ruuls = (
    "Singlplayer - начать игру в одиночном режиме\n"
    + "Multiplayer - начать игру в многопользовательском режиме\n"
    + "Для атаки врага нажмите в момент соединения друх треугольников внизу экрана\n"
    + 'Для экипировки нового оружия "выбросите" его из инвенторя\n'
    + "Для открытия инвентаря нажмите 'i'\n"
    + 'Для того чтобы во время игры упровлять мышкой нажмите "esc"\n'
)


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


game_started = False
app = Ursina()
sky = Sky()
world = World()
Menu = Menu()
attack = Attack(game_started)
inventory = Inventory()
healt_bar_player = HealthBar(
    bar_color=color.lime.tint(-0.25),
    roundness=0.5,
    value=100,
    enabled=False,
    position_z=-1,
)
exp_bar = HealthBar(
    bar_color=color.green,
    roundness=0.5,
    max_value=100,
    position=(0.2 * window.aspect_ratio, 0.45),
    enabled=False,
)
player = Oneplayer(inventory, healt_bar_player, enabled=False)
healt_bar_player.position = (-0.35 * window.aspect_ratio, 0.45)
player.collider = "cube"
inventory.player = player


def start_game_singlplayer():
    global attack, inventory, healt_bar_player, game_started
    world.generate_world()
    exp_bar.value = player.exp
    healt_bar_player.enabled = True
    player.enabled = True
    mouse.locked = True
    attack.start = True
    game_started = True
    Menu.Menu.enabled = True
    exp_bar.enabled = True
    Menu.start.enabled, Menu.multi.enabled = False, False
    load_game_stats()
    spawn()


def destroy_all_and_respawn():
    for i in range(1, len(world.rooms) - 1):
        destroy(world.rooms[i])
    destroy(world)
    world.rooms = [world.famaly_room]
    enemys.clear()
    healt_bar_player.enabled = False
    player.enabled = False
    attack.start = False
    game_started = False
    Menu.Menu.enabled = False
    Menu.start.enabled, Menu.multi.enabled = True, True
    destroy(lose)
    healt_bar_player.value = 100
    player.position = (0, 0, 0)
    player.rotation = (0, 0, 0)


def input(key):
    if key == "l":
        for i in scene.entities:
            print(i.name)
    if key == "escape":
        mouse.locked = not mouse.locked
    if game_started == True:
        player.speed = 5 + held_keys["shift"] * 7
    if key == "left mouse down" and attack.at_the_moment():
        if (
            str(mouse.hovered_entity) == "render/scene/enemy"
            and distance(player, mouse.hovered_entity) < 2.5
        ):
            mouse.hovered_entity.hp_value -= (10 + int(player.weapon[0])) + (
                10 + int(player.weapon[0])
            ) * int(player.weapon[1]) / 10
    if (
        key == "left mouse down"
        and mouse.hovered_entity
        and str(mouse.hovered_entity) != "render/scene/enemy"
        and str(mouse.hovered_entity) != "render/scene/room"
        and str(mouse.hovered_entity) != "render/scene/oneplayer"
    ):
        print(mouse.hovered_entity)
        text = mouse.hovered_entity.text
        if text == "Singlplayer":
            start_game_singlplayer()
        if text == "Multiplayer":
            save_test()
        if text == "Exit":
            ExitButton().on_click()
        if text == "Fullscreen":
            window.fullscreen = True
        if text == "Not Fullscreen":
            window.fullscreen = False
        if text == "New Game" or text == "Restart":
            if_death()
            destroy_all_and_respawn()
        Menu.Menu.close()
    if key == "i" and game_started:
        mouse.locked = not mouse.locked
        inventory.enabled = not inventory.enabled


def spawn():
    global enemys
    enemys = []
    for i in range(1, len(world.rooms) - 1):
        a, b, c = world.rooms[i].position
        enemy = Enemy(
            player,
            healt_bar_player,
            exp_bar,
            inventory,
            position=(a, b, c) + (randint(-14, 14), 1, randint(-14, 14)),
        )
        enemys.append(enemy)


def if_death():
    global game_started, lose
    game_started = False
    healt_bar_player.enabled = True
    mouse.locked = False
    player.enabled = False
    attack.start = False
    Menu.Menu.enabled = False
    lose = Button(text="You lose", color=color.red, scale=0.26)
    lose.on_click = destroy_all_and_respawn
    lose.tooltip = Tooltip(text="<scale:1.2>" + "YOU LOSE")
    save_test()


def update():
    if healt_bar_player.value == 0 and game_started:
        if_death()
    if exp_bar.value == 100:
        exp_bar.value = 0
        player.level += 1


def load_game_stats():
    file = open("Client/items.txt", "r")
    data = json.loads(file.read())
    player.level = data["player.lvl"]
    exp_bar.value = data["player.exp"]
    player.weapon = data["player.eq_weapon"]
    for item in data["items"]:
        print(item)
        print(item[1], item[2])
        inventory.append(item[0], player.level, item[1], item[2])


def save_test():
    file_with_stats = open("items.txt", "w")
    save_data = {
        "player.lvl": player.level,
        "player.exp": exp_bar.value,
        "player.eq_weapon": player.weapon,
        "items": [
            (
                inventory.item_parent.children[i].texture.name,
                inventory.item_parent.children[i].damage,
                inventory.item_parent.children[i].multiplier,
            )
            for i in range(len(inventory.item_parent.children))
        ],
    }
    print(save_data)
    file_with_stats.write(json.dumps(save_data))
    file_with_stats.close()


app.run()
