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
        self.collisions = None

    def render_world(self):
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

    def _handle_input(self):
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
        self.world.update_scenario(actions)

    def update(self):
        self._handle_input()
        self.collisions = self.world.update_collisions()

    def draw(self):
        pyxel.cls(0)
        self.render_world()
        if DEBUG:
            ship_enemies = self.collisions['ship_enemies']
            bullet_enemies = self.collisions['bullet_enemies']
            if len(ship_enemies) > 0:
                pyxel.text(140, 100, 'DEATH', 4)
            if len(bullet_enemies) > 0:
                pyxel.text(140, 110, 'KILL', 4)


if __name__ == '__main__':
    PyxelTron()
