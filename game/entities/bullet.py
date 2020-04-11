from engine.entities.base import BaseEntity
from render.entities.bullet import BulletRender


class Bullet(BaseEntity):
    RENDER_CLASS = BulletRender
