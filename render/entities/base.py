class BaseRender:
    IMAGE_BANK = None

    WIDTH = None
    HEIGHT = None

    def __init__(self, entity):
        self.entity = entity
