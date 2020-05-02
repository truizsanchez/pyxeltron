from engine.physics.movement import DIRECTION_UP, DIRECTION_DOWN, DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_NONE
from render.constants import SHIP
from render.entities.base import BaseRender


class ShipRender(BaseRender):
    IMAGE_BANK = SHIP
    WIDTH = 8
    HEIGHT = 8

    UV = {
        DIRECTION_UP: {'u': 0, 'v': 0},
        DIRECTION_RIGHT: {'u': 8, 'v': 0},
        DIRECTION_DOWN: {'u': 16, 'v': 0},
        DIRECTION_LEFT: {'u': 24, 'v': 0},
        DIRECTION_NONE: {'u': 0, 'v': 0},
    }

    @property
    def u(self):
        return self.UV[self.entity.direction]['u']

    @property
    def v(self):
        return self.UV[self.entity.direction]['v']
