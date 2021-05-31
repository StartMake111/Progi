from ursina import *
from ursina.prefabs.exit_button import ExitButton
import numpy


class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            enabled=False,
            model="quad",
            scale=(0.5, 0.8),
            origin=(-0.5, 0.5),
            position=(0.39, 0.41),
            texture="white_cube",
            texture_scale=(5, 8),
            color=color.dark_gray,
        )
        self.player = None
        self.item_parent = Entity(parent=self, scale=(1 / 5, 1 / 8))

    def append(self, item, lvl, dmg=0, mults=0):
        # дабавляет предмет если есть свободное место на это свободное место
        # Draggable делает предмет переносимым с помощью мышки
        pos = self.find_free_spot()
        if pos:
            if dmg + mults == 0:
                a, b = self.set_attributs(lvl)
            else:
                a, b = dmg, mults
            icon = Draggable(
                parent=self.item_parent,
                model="quad",
                origin=(-0.5, 0.5),
                texture=item,
                color=color.white,
                position=pos,
                z=-0.1,
                damage=a,
                multiplier=b,
            )
            name = item.replace("_", " ").title()
            icon.tooltip = Tooltip(
                "<red><scale:1.5>"
                + name
                + "\n<orange><scale:1>"
                + "\n \n \n \n \n \n Уровень предмета :"
                + "<default>"
                + str((int(icon.damage) + int(icon.multiplier)))
                + "\n<orange><scale:1>  Добавочный урон :"
                + "<default>"
                + icon.damage
                + "\n<orange><scale:1>  Мультипликатор урона : "
                + "<default>"
                + icon.multiplier,
                lines=4,
            )
            icon.tooltip.background.color = color.color(0, 0, 0, 0.8)

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= 0.01

        def drop():
            icon.x = int(round(icon.x))
            icon.y = int(round(icon.y))
            icon.z += 0.01
            # остаемся внутри инвенторя
            if icon.x < 0 or icon.x > 4 or icon.y > 0 or icon.y < -7:
                delete_item(icon)
                icon.position = icon.org_pos
                return
            # меняем если место занято
            for c in self.item_parent.children:
                if c == icon:
                    continue
                if c.x == icon.x and c.y == icon.y:
                    c.position = icon.org_pos

        def delete_item(item):
            ask = Text(
                text="Экипировать предмет?", parent=camera.ui, position=(-0.1, -0.1)
            )
            yes = Button(
                parent=camera.ui,
                position=(-0.2, -0.3),
                scale=(0.1, 0.1),
                color=color.lime.tint(-0.25),
                text="Да",
                tooltip=Tooltip("Да"),
                on_click=lambda: item.delete(yes, no, ask),
            )
            no = Button(
                parent=camera.ui,
                position=(0.2, -0.3),
                scale=(0.1, 0.1),
                color=color.lime.tint(-0.25),
                text="Нет",
                tooltip=Tooltip("Нет"),
                on_click=lambda: check(),
            )

            def check():
                destroy(ask)
                destroy(no)
                destroy(yes)
                return True

        def delete(ask, yes, no):
            self.player.weapon = (icon.damage, icon.multiplier)
            destroy(icon)
            destroy(ask)
            destroy(yes)
            destroy(no)

        icon.drag = drag
        icon.drop = drop
        icon.delete_item = delete_item
        icon.delete = delete

    def set_attributs(self, lvl):
        b, c = numpy.random.multinomial(lvl, [2.0 / 3, 2.0 / 3])
        return (str(int(abs(b))), str(int(abs(c))))

    def add_item(self, lvl):
        self.append(random.choice(("shortsword", "longsword", "dagger")), lvl)

    def find_free_spot(self):
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
        if len(taken_spots) > 39:
            return 0
        for y in range(8):
            for x in range(5):
                if not (x, -y) in taken_spots:
                    return (x, -y)


if __name__ == "__main__":
    app = Ursina()
    ec = EditorCamera(enabled=False)
    inventory = Inventory()
    inventory.enabled = True

    def add_item():
        inventory.append(random.choice(("shortsword", "longsword", "dagger")))

    add_item_button = Button(
        scale=(0.1, 0.1),
        x=-0.5,
        color=color.lime.tint(-0.25),
        text="+",
        tooltip=Tooltip("Add random item"),
        on_click=add_item,
    )

    # inventory.load_file()

    def input(key):
        if key == "i":
            inventory.enabled = not inventory.enabled

    app.run()
