from engine.entities.base import BaseEntity


class BaseRender:
    IMAGE_BANK = None

    WIDTH = None
    HEIGHT = None

    def __init__(self, entity: BaseEntity):
        self.entity = entity
