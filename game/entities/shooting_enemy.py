import logging
from datetime import datetime

from engine.physics.movement import vector_between_entities, cartesian_to_polar
from game.entities.enemy import Enemy


class ShootingEnemy(Enemy):
    VX_DEFAULT = 0
    VY_DEFAULT = 0
    WIDTH = 6
    SHOOTING_COOLDOWN = 2  # seconds

    def __init__(self, x=None, y=None, render_class=None, **kwargs):
        super().__init__(x, y, render_class, **kwargs)
        self.shooting_cooldown = datetime.now()

    def evaluate_shooting(self):
        now = datetime.now()
        if (now - self.shooting_cooldown).total_seconds() > self.SHOOTING_COOLDOWN:
            self.shooting_cooldown = now
            return True
        return False

    def shoot(self, ship):
        x, y = vector_between_entities(self, ship)
        _, angle = cartesian_to_polar(x, y)
        msga = f'ship: x: {ship.x}, y: {ship.y}'
        msg = f'x: {x}, y: {y}, distance: {_}, angle: {angle}'
        logging.warning(msg)

