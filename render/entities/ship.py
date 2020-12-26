from engine.physics.movement import UP, DOWN, RIGHT, LEFT, LEFT_UP, LEFT_DOWN, RIGHT_UP, RIGHT_DOWN
from render.constants import SHIP
from render.entities.base import BaseRender


class ShipRender(BaseRender):
    IMAGE_BANK = SHIP
    WIDTH = 8
    HEIGHT = 8

    UV = {
        UP: {'u': 0, 'v': 0},
        LEFT_UP: {'u': 0, 'v': 0},
        RIGHT_UP: {'u': 0, 'v': 0},
        RIGHT: {'u': 8, 'v': 0},
        DOWN: {'u': 16, 'v': 0},
        LEFT_DOWN: {'u': 16, 'v': 0},
        RIGHT_DOWN: {'u': 16, 'v': 0},
        LEFT: {'u': 24, 'v': 0},
    }

    @property
    def u(self) -> int:
        return self.UV[self.entity.orientation]['u']

    @property
    def v(self) -> int:
        return self.UV[self.entity.orientation]['v']
