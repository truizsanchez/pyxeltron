from game.entities.bullet import Bullet
from render.constants import TILESET
from render.entities.base import BaseRender


class BulletRender(BaseRender):
    ENTITY_CLASS = Bullet
    IMAGE_BANK = TILESET
    U = 16
    V = 16
    WIDTH = 8
    HEIGHT = 8
