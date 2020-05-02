from engine.physics.movement import UP, DOWN, RIGHT, LEFT
from render.constants import SHIP
from render.entities.base import BaseRender


class ShipRender(BaseRender):
    IMAGE_BANK = SHIP
    WIDTH = 8
    HEIGHT = 8

    UV = {
        UP: {'u': 0, 'v': 0},
        RIGHT: {'u': 8, 'v': 0},
        DOWN: {'u': 16, 'v': 0},
        LEFT: {'u': 24, 'v': 0},
    }

    @property
    def u(self):
        return self.UV[self.entity.orientation]['u']

    @property
    def v(self):
        return self.UV[self.entity.orientation]['v']
