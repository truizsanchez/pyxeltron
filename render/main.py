import pyxel

from engine.game_world import GameWorld
from game.entities.bullet import Bullet
from game.entities.enemy import Enemy
from game.entities.ship import Ship
from render.constants import TILESET, TILESET_PATH, SHIP_PATH, SHIP, PICO8_PALETTE, COLOR_BLACK
from render.entities.bullet import BulletRender
from render.entities.enemy import EnemyRender
from render.entities.ship import ShipRender


class PyxelTron:
    def __init__(self):
        pyxel.init(160, 120, caption="PyxelTron", palette=PICO8_PALETTE)
        pyxel.image(TILESET).load(0, 0, TILESET_PATH)
        pyxel.image(SHIP).load(0, 0, SHIP_PATH)
        self.world = GameWorld()
        self.initialize_world()
        pyxel.run(self.update, self.draw)

    def initialize_world(self):
        self.world.add_entity(Ship(0, 0, render_class=ShipRender), 'ship')
        self.world.add_entity_to_category(Enemy(0, 8, render_class=EnemyRender), 'enemies')

    def render_world(self):
        for entity in self.world.entities:
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
        elif pyxel.btn(pyxel.KEY_SPACE):
            bullet = Bullet(ship.x, ship.y, render_class=BulletRender)
            self.world.add_entity_to_category(bullet, 'bullets')

    def update(self):
        self._handle_input()

    def draw(self):
        pyxel.cls(0)
        self.render_world()


if __name__ == '__main__':
    PyxelTron()
