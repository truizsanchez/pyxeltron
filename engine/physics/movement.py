from enum import Enum


class Movement(Enum):
    LINEAR_MOTION = 1
    STEERED = 2


UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'
CARTESIAN = {
    UP: dict(x=0, y=-1),
    DOWN: dict(x=0, y=1),
    RIGHT: dict(x=1, y=0),
    LEFT: dict(x=-1, y=0),
}


def update_position(entity):
    if entity.direction:
        movement = CARTESIAN[entity.direction]
        entity.x = entity.x + (movement['x'] * entity.vx)
        entity.y = entity.y + (movement['y'] * entity.vy)
