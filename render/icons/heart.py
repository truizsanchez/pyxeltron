from render.constants import TILESET


# TODO: icons have a lot of similarities with renders, but are not associated with
#  entities, review hierarchy

class HeartIcon:

    IMAGE_BANK = TILESET

    WIDTH = 8
    HEIGHT = 8

    U = 32
    V = 57

    @property
    def u(self) -> int:
        return self.U

    @property
    def v(self) -> int:
        return self.V
