from render.constants import TILESET
from render.entities.static import StaticRender


class BulletRender(StaticRender):
    IMAGE_BANK = TILESET
    U = 16
    V = 16
    WIDTH = 8
    HEIGHT = 8
