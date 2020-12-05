from engine.physics.movement import Movement, RIGHT, PositionType


class BaseEntity:
    STATES = None
    VX_DEFAULT = 2
    VY_DEFAULT = 2
    WIDTH = None
    HEIGHT = None
    MOVEMENT_TYPE = Movement.STEERED
    POSITION_TYPE = PositionType.BOUNDED

    def __init__(self, x=None, y=None, render_class=None, **kwargs):
        from render import glue

        self.x: int = x
        self.y: int = y
        if not render_class:
            render_class = glue.render_classes.get(self.__class__)
        self.render = render_class(self) if render_class else None
        self.vx: int = kwargs.get('vx', self.VX_DEFAULT)
        self.vy: int = kwargs.get('vy', self.VY_DEFAULT)
        self.width: int = kwargs.get('width', self.WIDTH)
        self.height: int = kwargs.get('height', self.HEIGHT)
        self.orientation: str = kwargs.get('direction', RIGHT)
        self.direction: str = kwargs.get('direction', None)
        self.movement_type: int = kwargs.get('movement', self.MOVEMENT_TYPE)
        self.position_type: int = kwargs.get('position_type', self.POSITION_TYPE)
