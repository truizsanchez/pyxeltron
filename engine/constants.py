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
