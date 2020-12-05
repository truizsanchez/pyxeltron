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
CARTESIAN = {
    UP: dict(x=0, y=-1),
    DOWN: dict(x=0, y=1),
    RIGHT: dict(x=1, y=0),
    LEFT: dict(x=-1, y=0),
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
