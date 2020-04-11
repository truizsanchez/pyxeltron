class BaseEntity:
    STATES = None
    RENDER_CLASS = None
    VX_DEFAULT = 2
    VY_DEFAULT = 2

    def __init__(self, x=None, y=None, vx=None, vy=None):
        self.x = x
        self.y = y
        self.vx = vx if vx is not None else self.VX_DEFAULT
        self.vy = vy if vy is not None else self.VY_DEFAULT

    def move_left(self):
        self.x = self.x - self.vx

    def move_right(self):
        self.x = self.x + self.vx

    def move_up(self):
        self.y = self.y - self.vy

    def move_down(self):
        self.y = self.y + self.vy
