from game.entities.bullet import Bullet
from game.entities.enemy import Enemy
from game.entities.ship import Ship
from game.entities.shooting_enemy import ShootingEnemy
from render.entities.bullet import BulletRender
from render.entities.enemy import EnemyRender
from render.entities.ship import ShipRender
from render.entities.shooting_enemy import ShootingEnemyRender

render_classes = {
    Bullet: BulletRender,
    Ship: ShipRender,
    Enemy: EnemyRender,
    ShootingEnemy: ShootingEnemyRender,
}
