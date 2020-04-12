from engine.constants import DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_UP, DIRECTION_DOWN


class BaseEntity:
    STATES = None
    VX_DEFAULT = 2
    VY_DEFAULT = 2
    WIDTH = None
    HEIGHT = None

    def __init__(self, x=None, y=None, render_class=None, **kwargs):
        self.x = x
        self.y = y
        self.render = render_class(self) if render_class else None
        self.vx = kwargs.get('vx', self.VX_DEFAULT)
        self.vy = kwargs.get('vy', self.VY_DEFAULT)
        self.width = kwargs.get('width', self.WIDTH)
        self.height = kwargs.get('height', self.HEIGHT)
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
