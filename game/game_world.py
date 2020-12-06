from enum import Enum
from typing import List, Tuple

from engine.entities.base import BaseEntity
from engine.physics.movement import UP, DOWN, RIGHT, LEFT
from engine.game_world import GameWorld
from engine.physics.collisions.rectangle import Rectangle, check_collision
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
        self.add_entity(Ship(64, 64), 'ship')
        self.add_entity_to_category(Enemy(16, 16), 'enemies')
        self.add_entity_to_category(Enemy(24, 8), 'enemies')
        self.add_entity_to_category(Enemy(96, 32), 'enemies')
        self.add_entity_to_category(Enemy(96, 96), 'enemies')
        self.add_entity_to_category(Enemy(8, 92), 'enemies')

    def _handle_actions(self, actions: List[Action]) -> None:
        ship = self.get_entity('ship')
        if not actions:
            ship.direction = None

        for action in actions:
            if action == Action.MOVE_LEFT:
                ship.orientation = LEFT
                ship.direction = LEFT
            elif action == Action.MOVE_RIGHT:
                ship.orientation = RIGHT
                ship.direction = RIGHT
            elif action == Action.MOVE_UP:
                ship.orientation = UP
                ship.direction = UP
            elif action == Action.MOVE_DOWN:
                ship.orientation = DOWN
                ship.direction = DOWN
            else:
                ship.direction = None

            if action == Action.SHOOT:
                bullet = Bullet(ship.x, ship.y, direction=ship.orientation)
                self.add_entity_to_category(bullet, 'bullets')

    def _calculate_direction_from_enemy_to_ship(self, enemy: BaseEntity, ship: BaseEntity) -> None:
        # the enemy chase the ship shortening the longest component distance
        x_distance: int = abs(enemy.x - ship.x)
        y_distance: int = abs(enemy.y - ship.y)
        if x_distance > y_distance:
            if enemy.x < ship.x:
                enemy.orientation = RIGHT
                enemy.direction = RIGHT
            else:
                enemy.orientation = LEFT
                enemy.direction = LEFT
        else:
            if enemy.y < ship.y:
                enemy.orientation = DOWN
                enemy.direction = DOWN
            else:
                enemy.direction = UP
                enemy.orientation = UP

    def _update_enemies(self) -> None:
        enemies: List[BaseEntity] = self.get_entities_by_category('enemies')
        ship: BaseEntity = self.get_entity('ship')
        for enemy in enemies:
            self._calculate_direction_from_enemy_to_ship(enemy, ship)

    def update_scenario(self, actions: List[Action]):
        self._handle_actions(actions)
        self._update_enemies()
        self._update_positions()
        self._evaluate_scenario()

    def _evaluate_scenario(self):
        ship_enemies = self._calculate_collisions_ship_enemies()
        bullet_enemies = self._calculate_collisions_bullets_enemies()
        for bullet, enemy in bullet_enemies:
            self.remove_entity_from_category('enemies', enemy)
            self.remove_entity_from_category('bullets', bullet)
        self._remove_entities_outside_viewport()
        # TODO: return actions after collision evaluation (ship destroyed, enemy down etc)

    def _calculate_collision_between_entities(self, entity1: BaseEntity, entity2: BaseEntity) -> bool:
        rect_entity1 = Rectangle(entity1.x, entity1.y, entity1.width, entity1.height)
        rect_entity2 = Rectangle(entity2.x, entity2.y, entity2.width, entity2.height)
        return check_collision(rect_entity1, rect_entity2)

    def _calculate_collisions_bullets_enemies(self) -> List[Tuple[BaseEntity, BaseEntity]]:
        enemies = self.get_entities_by_category('enemies')
        bullets = self.get_entities_by_category('bullets')
        collisions: List[Tuple[BaseEntity, BaseEntity]] = []
        impacted_bullets = []
        for enemy in enemies:
            bullets = [bullet for bullet in bullets if bullet not in impacted_bullets]
            for bullet in bullets:
                collision = self._calculate_collision_between_entities(enemy, bullet)
                if collision:
                    collisions.append((bullet, enemy,))
                    impacted_bullets.append(bullet)
        return collisions

    def _calculate_collisions_ship_enemies(self) -> List[BaseEntity]:
        ship = self.get_entity('ship')
        enemies = self.get_entities_by_category('enemies')
        collisions: List[BaseEntity] = []
        for enemy in enemies:
            collision = self._calculate_collision_between_entities(enemy, ship)
            if collision:
                collisions.append(enemy)
        return collisions

    def _remove_entities_outside_viewport(self):
        bullets = self.get_entities_by_category('bullets')
        for bullet in bullets:
            if bullet.x < 0 or bullet.x > self.WIDTH or bullet.y < 0 or bullet.y > self.HEIGHT:
                self.remove_entity_from_category('bullets', bullet)
