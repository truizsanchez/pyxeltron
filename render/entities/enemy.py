from game.entities.enemy import Enemy
from render.constants import TILESET
from render.entities.base import BaseRender


class EnemyRender(BaseRender):
    ENTITY_CLASS = Enemy
    IMAGE_BANK = TILESET
    U = 24
    V = 0
    WIDTH = 8
    HEIGHT = 8
