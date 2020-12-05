from render.entities.base import BaseRender


class StaticRender(BaseRender):
    U = None
    V = None

    @property
    def u(self) -> int:
        return self.U

    @property
    def v(self) -> int:
        return self.V
