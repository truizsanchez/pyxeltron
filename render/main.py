import pyxel


class PyxelTron:
    def __init__(self):
        pyxel.init(160, 120, caption="PyxelTron")
        pyxel.image(0).load(0, 0, "assets/tileset.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(64, 64, 0, 0, 0, 8, 8)


if __name__ == '__main__':
    PyxelTron()
