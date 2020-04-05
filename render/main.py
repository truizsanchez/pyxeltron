import pyxel

from render.constants import TILESET, TILESET_PATH
from render.entities.bullet import BulletRender
from render.entities.enemy import EnemyRender
from render.entities.ship import ShipRender


class PyxelTron:
    def __init__(self):
        pyxel.init(160, 120, caption="PyxelTron")
        pyxel.image(TILESET).load(0, 0, TILESET_PATH)
        pyxel.run(self.update, self.draw)

    def _handle_input(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_LEFT):
            pass
        elif pyxel.btn(pyxel.KEY_RIGHT):
            pass
        elif pyxel.btn(pyxel.KEY_UP):
            pass
        elif pyxel.btn(pyxel.KEY_DOWN):
            pass

    def update(self):
        self._handle_input()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, ShipRender.IMAGE_BANK, ShipRender.U, ShipRender.V, ShipRender.WIDTH, ShipRender.HEIGHT)
        pyxel.blt(0, 8, EnemyRender.IMAGE_BANK, EnemyRender.U, EnemyRender.V, EnemyRender.WIDTH, EnemyRender.HEIGHT)
        pyxel.blt(0, 16, BulletRender.IMAGE_BANK, BulletRender.U, BulletRender.V, BulletRender.WIDTH,
                  BulletRender.HEIGHT)


if __name__ == '__main__':
    PyxelTron()
