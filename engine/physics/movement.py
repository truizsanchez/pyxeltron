import math
from enum import Enum


class Movement(Enum):
    LINEAR_MOTION = 1
    STEERED = 2


class PositionType(Enum):
    BOUNDED = 1
    BOUNDLESS = 2


UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'
LEFT_UP = 'left_up'
LEFT_DOWN = 'left_down'
RIGHT_UP = 'right_up'
RIGHT_DOWN = 'right_down'

CARTESIAN = {
    UP: dict(x=0, y=-1),
    DOWN: dict(x=0, y=1),
    RIGHT: dict(x=1, y=0),
    LEFT: dict(x=-1, y=0),
    LEFT_UP: dict(x=-1, y=-1),
    LEFT_DOWN: dict(x=-1, y=1),
    RIGHT_UP: dict(x=1, y=-1),
    RIGHT_DOWN: dict(x=1, y=1)
}


def truncate_coordinate(coordinate, entity_size, max_value) -> int:
    if coordinate < 0:
        coordinate = 0
    if coordinate + entity_size > max_value:
        coordinate = max_value - entity_size
    return coordinate


def update_position(entity, world_width, world_height) -> None:
    if entity.direction:
        movement = CARTESIAN[entity.direction]
        x = entity.x + (movement['x'] * entity.vx)
        y = entity.y + (movement['y'] * entity.vy)

        if entity.position_type == PositionType.BOUNDED:
            x = truncate_coordinate(x, entity.width, world_width)
            y = truncate_coordinate(y, entity.height, world_height)

        entity.x = x
        entity.y = y


def vector_between_entities(entity1, entity2):
    x = entity2.x - entity1.x
    y = entity2.y - entity1.y
    return x, y


def cartesian_to_polar(x, y):
    distance = math.sqrt(x**2 + y**2)
    angle = math.atan2(x, y)
    angle = math.degrees(angle)
    return distance, angle
