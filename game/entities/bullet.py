from engine.entities.base import BaseEntity
from engine.physics.movement import Movement


class Bullet(BaseEntity):
    VX_DEFAULT = 5
    VY_DEFAULT = 5
    WIDTH = 8
    HEIGHT = 8
    MOVEMENT = Movement.LINEAR_MOTION
