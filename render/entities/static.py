from render.entities.base import BaseRender


class StaticRender(BaseRender):
    U = None
    V = None

    @property
    def u(self):
        return self.U

    @property
    def v(self):
        return self.V
