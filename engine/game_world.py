from game.entities.ship import Ship


class GameWorld:
    def __init__(self):
        self.ship = Ship(0, 0, 0, 0)
