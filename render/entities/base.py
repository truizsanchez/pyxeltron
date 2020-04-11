class BaseRender:

    IMAGE_BANK = None
    U = None
    V = None
    WIDTH = None
    HEIGHT = None

    def __init__(self, entity):
        self.entity = entity
