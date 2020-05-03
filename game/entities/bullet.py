from engine.entities.base import BaseEntity
from engine.physics.movement import Movement, PositionType


class Bullet(BaseEntity):
    VX_DEFAULT = 5
    VY_DEFAULT = 5
    WIDTH = 8
    HEIGHT = 8
    MOVEMENT_TYPE = Movement.LINEAR_MOTION
    POSITION_TYPE = PositionType.BOUNDLESS
