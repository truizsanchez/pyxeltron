from engine.entities.base import BaseEntity
from render.entities.enemy import EnemyRender


class Enemy(BaseEntity):
    RENDER_CLASS = EnemyRender
