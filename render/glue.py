from game.entities.bullet import Bullet
from game.entities.enemy import Enemy
from game.entities.ship import Ship
from render.entities.bullet import BulletRender
from render.entities.enemy import EnemyRender
from render.entities.ship import ShipRender

render_classes = {
    Bullet: BulletRender,
    Ship: ShipRender,
    Enemy: EnemyRender
}
