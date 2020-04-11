import pyxel

from engine.game_world import GameWorld
from game.entities.bullet import Bullet
from game.entities.enemy import Enemy
from game.entities.ship import Ship
from render.constants import TILESET, TILESET_PATH


class PyxelTron:
    def __init__(self):
        pyxel.init(160, 120, caption="PyxelTron")
        pyxel.image(TILESET).load(0, 0, TILESET_PATH)
        self.world = GameWorld()
        self.initialize_world()
        pyxel.run(self.update, self.draw)

    def initialize_world(self):
        self.world.add_entity('ship', Ship(0, 0))
        self.world.add_entity('enemy', Enemy(0, 8))
        self.world.add_entity('bullet', Bullet(8, 8))

    def render_world(self):
        for name, entity in self.world.entities:
            pyxel.blt(
                entity.x,
                entity.y,
                entity.RENDER_CLASS.IMAGE_BANK,
                entity.RENDER_CLASS.U,
                entity.RENDER_CLASS.V,
                entity.RENDER_CLASS.WIDTH,
                entity.RENDER_CLASS.HEIGHT
            )

    def _handle_input(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        ship = self.world.get_entity('ship')
        if pyxel.btn(pyxel.KEY_LEFT):
            ship.move_left()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            ship.move_right()
        elif pyxel.btn(pyxel.KEY_UP):
            ship.move_up()
        elif pyxel.btn(pyxel.KEY_DOWN):
            ship.move_down()

    def update(self):
        self._handle_input()

    def draw(self):
        pyxel.cls(0)
        self.render_world()


if __name__ == '__main__':
    PyxelTron()
