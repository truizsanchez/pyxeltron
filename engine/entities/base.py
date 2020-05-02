from engine.physics.movement import Movement, DIRECTION_NONE


class BaseEntity:
    STATES = None
    VX_DEFAULT = 2
    VY_DEFAULT = 2
    WIDTH = None
    HEIGHT = None
    MOVEMENT = Movement.STEERED

    def __init__(self, x=None, y=None, render_class=None, **kwargs):
        from render import glue

        self.x = x
        self.y = y
        if not render_class:
            render_class = glue.render_classes.get(self.__class__)
        self.render = render_class(self) if render_class else None
        self.vx = kwargs.get('vx', self.VX_DEFAULT)
        self.vy = kwargs.get('vy', self.VY_DEFAULT)
        self.width = kwargs.get('width', self.WIDTH)
        self.height = kwargs.get('height', self.HEIGHT)
        self.direction = kwargs.get('direction', DIRECTION_NONE)
        self.movement = kwargs.get('movement', self.MOVEMENT)
