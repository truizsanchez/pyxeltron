from render.constants import TILESET
from render.entities.static import StaticRender


class EnemyRender(StaticRender):
    IMAGE_BANK = TILESET
    U = 24
    V = 0
    WIDTH = 8
    HEIGHT = 8
