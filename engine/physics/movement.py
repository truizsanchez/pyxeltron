from enum import Enum


class Movement(Enum):
    LINEAR_MOTION = 1
    STEERED = 2


DIRECTION_UP = 'up'
DIRECTION_DOWN = 'down'
DIRECTION_RIGHT = 'right'
DIRECTION_LEFT = 'left'
DIRECTION_NONE = 'none'
DIRECTION_MOVEMENT = {
    DIRECTION_UP: dict(x=0, y=-1),
    DIRECTION_DOWN: dict(x=0, y=1),
    DIRECTION_RIGHT: dict(x=1, y=0),
    DIRECTION_LEFT: dict(x=-1, y=0),
    DIRECTION_NONE: dict(x=0, y=0),
}


def update_position(entity):
    if entity.direction is not DIRECTION_NONE:
        movement = DIRECTION_MOVEMENT[entity.direction]
        entity.x = entity.x + (movement['x'] * entity.vx)
        entity.y = entity.y + (movement['y'] * entity.vy)
