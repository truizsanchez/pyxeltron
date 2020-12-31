from render.constants import TILESET
from render.entities.static import StaticRender


class ShootingEnemyRender(StaticRender):
    IMAGE_BANK = TILESET
    U = 65
    V = 0
    WIDTH = 6
    HEIGHT = 8
