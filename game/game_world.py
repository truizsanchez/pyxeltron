from datetime import datetime
from enum import Enum
from typing import List, Tuple

from engine.entities.base import BaseEntity
from engine.physics.movement import UP, DOWN, RIGHT, LEFT, LEFT_UP, LEFT_DOWN, RIGHT_UP, RIGHT_DOWN
from engine.game_world import GameWorld
from engine.physics.collisions.rectangle import Rectangle, check_collision
from game.entities.bullet import Bullet
from game.entities.enemy import Enemy
from game.entities.ship import Ship
from game.entities.shooting_enemy import ShootingEnemy
from game.levels import levels

INITIAL_LIVES = 3
PAUSE_COOLDOWN = 1  # seconds


class Action(Enum):
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    MOVE_UP = 3
    MOVE_DOWN = 4
    MOVE_LEFT_UP = 5
    MOVE_LEFT_DOWN = 6
    MOVE_RIGHT_UP = 7
    MOVE_RIGHT_DOWN = 8
    SHOOT = 9


class ResultType(Enum):
    SHIP_SHOOTING = 1
    SHIP_DESTROYED = 2
    ENEMY_DOWN = 3
    LEVEL_CLEARED = 4


class ApplicationState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3
    GAME_FINISHED = 4
    PAUSE_COOLDOWN = 5


class ResultData:
    def __init__(self, result_type, data=None):
        self.result_type = result_type
        self.data = data

    def __str__(self):
        return self.result_type

    def __repr__(self):
        return str(self.result_type)


class PyxelTronGameWorld(GameWorld):

    def __init__(self):
        super().__init__()
        self._results = []
        self.state = None
        self.level = 1
        self.n_levels = len(levels)
        self.lives = INITIAL_LIVES
        self.pause_cooldown = None
        self.current_time = datetime.now()

    def initialize(self):
        self.add_entity(Ship(64, 64), 'ship')
        self.state = ApplicationState.PLAYING
        self.load_level(1)

    def load_level(self, number: int):
        self._clear_scenario()
        self.level = number
        ship_coordinates = levels[number]['ship']
        enemies_coordinates = levels[number]['enemies']
        shooting_enemies_coordinates = levels[number]['shooting_enemies']
        self.add_entity(Ship(ship_coordinates[0], ship_coordinates[1]), 'ship')
        for enemy in enemies_coordinates:
            self.add_entity_to_category(Enemy(enemy[0], enemy[1]), 'enemies')
        for enemy in shooting_enemies_coordinates:
            self.add_entity_to_category(ShootingEnemy(enemy[0], enemy[1]), 'shooting_enemies')

    def _clear_scenario(self):
        self.clear_category('bullets')
        self.clear_category('enemies')
        self.clear_category('shooting_enemies')

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
            elif action == Action.MOVE_LEFT_UP:
                ship.orientation = LEFT_UP
                ship.direction = LEFT_UP
            elif action == Action.MOVE_LEFT_DOWN:
                ship.orientation = LEFT_DOWN
                ship.direction = LEFT_DOWN
            elif action == Action.MOVE_RIGHT_UP:
                ship.orientation = RIGHT_UP
                ship.direction = RIGHT_UP
            elif action == Action.MOVE_RIGHT_DOWN:
                ship.orientation = RIGHT_DOWN
                ship.direction = RIGHT_DOWN

            else:
                ship.direction = None

            if action == Action.SHOOT:
                self._results.append(ResultData(ResultType.SHIP_SHOOTING))
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
        enemies: List[BaseEntity] = self.get_entities(['enemies', 'shooting_enemies'])
        ship: BaseEntity = self.get_entity('ship')
        for enemy in enemies:
            self._calculate_direction_from_enemy_to_ship(enemy, ship)

    def update_scenario(self, actions: List[Action]):
        self.current_time = datetime.now()
        if self.state == ApplicationState.PAUSE_COOLDOWN:
            if (self.current_time - self.pause_cooldown).total_seconds() > PAUSE_COOLDOWN:
                self.pause_cooldown = None
                self.state = ApplicationState.PLAYING
            return []
        else:
            self._handle_actions(actions)
            self._update_enemies()
            self._update_positions()
            return self._evaluate_scenario()

    def _evaluate_scenario(self):
        ship_collision = self._calculate_collisions_ship_enemies()
        bullet_enemies = self._calculate_collisions_bullets_enemies()
        for bullet, enemy in bullet_enemies:
            self._results.append(ResultData(ResultType.ENEMY_DOWN, enemy))
            self.remove_entity_from_category(enemy, 'enemies')
            self.remove_entity_from_category(bullet, 'bullets')
        self._remove_entities_outside_viewport()
        enemies = self.get_entities(['enemies', 'shooting_enemies'])
        if not enemies:
            self._evaluate_scenario_changing()
        if ship_collision:
            self._evaluate_ship_collision(ship_collision)
        results = self._results
        self._results = []
        return results

    def _evaluate_ship_collision(self, ship_collision):
        self._results.append(ResultData(ResultType.SHIP_DESTROYED, ship_collision))
        self.lives -= 1
        if self.lives == 0:
            self.state = ApplicationState.GAME_OVER
        else:
            self.state = ApplicationState.PAUSE_COOLDOWN
            self.pause_cooldown = datetime.now()

    def _evaluate_scenario_changing(self):
        if self.level < self.n_levels:
            self._results.append(ResultData(ResultType.LEVEL_CLEARED))
        else:
            self.state = ApplicationState.GAME_FINISHED

    def _calculate_collision_between_entities(self, entity1: BaseEntity, entity2: BaseEntity) -> bool:
        rect_entity1 = Rectangle(entity1.x, entity1.y, entity1.width, entity1.height)
        rect_entity2 = Rectangle(entity2.x, entity2.y, entity2.width, entity2.height)
        return check_collision(rect_entity1, rect_entity2)

    def _calculate_collisions_bullets_enemies(self) -> List[Tuple[BaseEntity, BaseEntity]]:
        enemies = self.get_entities(['enemies', 'shooting_enemies'])
        bullets = self.get_entities('bullets')
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

    def _calculate_collisions_ship_enemies(self) -> BaseEntity:
        ship = self.get_entity('ship')
        enemies = self.get_entities(['enemies', 'shooting_enemies'])
        for enemy in enemies:
            collision = self._calculate_collision_between_entities(enemy, ship)
            if collision:
                return enemy

    def _remove_entities_outside_viewport(self):
        bullets = self.get_entities('bullets')
        for bullet in bullets:
            if bullet.x < 0 or bullet.x > self.WIDTH or bullet.y < 0 or bullet.y > self.HEIGHT:
                self.remove_entity_from_category(bullet, 'bullets')
