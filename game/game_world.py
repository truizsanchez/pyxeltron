from enum import Enum

from engine.collisions.rectangle import Rectangle, check_collision
from engine.game_world import GameWorld
from game.entities.bullet import Bullet
from game.entities.enemy import Enemy
from game.entities.ship import Ship


class Action(Enum):
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    MOVE_UP = 3
    MOVE_DOWN = 4
    SHOOT = 5


class PyxelTronGameWorld(GameWorld):

    def initialize(self):
        self.add_entity(Ship(0, 0), 'ship')
        self.add_entity_to_category(Enemy(0, 8), 'enemies')

    def update_scenario(self, actions=None):
        ship = self.get_entity('ship')
        for action in actions:
            if action == Action.MOVE_LEFT:
                ship.move_left()
            elif action == Action.MOVE_RIGHT:
                ship.move_right()
            elif action == Action.MOVE_UP:
                ship.move_up()
            elif action == Action.MOVE_DOWN:
                ship.move_down()
            elif action == Action.SHOOT:
                bullet = Bullet(ship.x, ship.y, vx=ship.vx, vy=ship.vy)
                self.add_entity_to_category(bullet, 'bullets')

    def update_collisions(self):
        ship = self.get_entity('ship')
        enemies = self.get_entities_by_category('enemies')
        rect1 = Rectangle(ship.x, ship.y, ship.width, ship.height)
        for enemy in enemies:
            rect_enemy = Rectangle(enemy.x, enemy.y, enemy.width, enemy.height)
            collision = check_collision(rect1, rect_enemy)
            if collision:
                return True

