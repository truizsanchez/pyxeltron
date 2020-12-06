from typing import List

import pyxel

from game.game_world import PyxelTronGameWorld, Action
from render.constants import TILESET, TILESET_PATH, SHIP_PATH, SHIP, PICO8_PALETTE, COLOR_BLACK, CAPTION
from settings import DEBUG


class PyxelTron:
    def __init__(self):
        self.world = PyxelTronGameWorld()
        pyxel.init(self.world.WIDTH, self.world.HEIGHT, caption=CAPTION, palette=PICO8_PALETTE)
        pyxel.image(TILESET).load(0, 0, TILESET_PATH)
        pyxel.image(SHIP).load(0, 0, SHIP_PATH)
        self.world.initialize()
        pyxel.run(self.update, self.draw)

    def render_world(self) -> None:
        for entity in self.world.entities:
            if entity.render:
                pyxel.blt(
                    entity.x,
                    entity.y,
                    entity.render.IMAGE_BANK,
                    entity.render.u,
                    entity.render.v,
                    entity.render.WIDTH,
                    entity.render.HEIGHT,
                    COLOR_BLACK
                )

    def _handle_input(self) -> List[Action]:
        actions = []
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_LEFT):
            actions.append(Action.MOVE_LEFT)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            actions.append(Action.MOVE_RIGHT)
        elif pyxel.btn(pyxel.KEY_UP):
            actions.append(Action.MOVE_UP)
        elif pyxel.btn(pyxel.KEY_DOWN):
            actions.append(Action.MOVE_DOWN)
        if pyxel.btnp(pyxel.KEY_SPACE):
            actions.append(Action.SHOOT)
        return actions

    def update(self) -> None:
        actions = self._handle_input()
        self.world.update_scenario(actions)

    def draw(self) -> None:
        pyxel.cls(0)
        self.render_world()
        if DEBUG:
            ship_enemies = self.world._collisions['ship_enemies']
            bullet_enemies = self.world._collisions['bullet_enemies']
            if len(ship_enemies) > 0:
                msg = f'{ship_enemies} DEATH'
                pyxel.text(100, 100, msg, 4)
            if len(bullet_enemies) > 0:
                msg = f'{bullet_enemies} KILL'
                pyxel.text(100, 110, msg, 4)


if __name__ == '__main__':
    PyxelTron()
