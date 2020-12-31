from game.entities.enemy import Enemy


class ShootingEnemy(Enemy):
    VX_DEFAULT = 0.3
    VY_DEFAULT = 0.3
    WIDTH = 6
    SHOOTING_COOLDOWN = 2  # seconds
