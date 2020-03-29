class BaseEntity:
    STATES = None

    def __init__(self, x=None, y=None, vx=None, vy=None):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
