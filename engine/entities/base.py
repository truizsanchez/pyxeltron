from engine.constants import DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_UP, DIRECTION_DOWN


class BaseEntity:
    STATES = None
    VX_DEFAULT = 2
    VY_DEFAULT = 2

    def __init__(self, x=None, y=None, vx=None, vy=None, render_class=None, **kwargs):
        self.x = x
        self.y = y
        self.vx = vx if vx is not None else self.VX_DEFAULT
        self.vy = vy if vy is not None else self.VY_DEFAULT
        self.render = render_class(self) if render_class else None
        self.direction = kwargs.get('direction', DIRECTION_RIGHT)

    def move_left(self):
        self.x = self.x - self.vx
        self.direction = DIRECTION_LEFT

    def move_right(self):
        self.x = self.x + self.vx
        self.direction = DIRECTION_RIGHT

    def move_up(self):
        self.y = self.y - self.vy
        self.direction = DIRECTION_UP

    def move_down(self):
        self.y = self.y + self.vy
        self.direction = DIRECTION_DOWN
