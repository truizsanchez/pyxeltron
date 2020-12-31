import logging


def debug_scenario_data(game_world):
    ship = game_world.get_entity('ship')
    enemies = game_world.get_entities_by_category('enemies')
    shooting_enemies = game_world.get_entities_by_category('shooting_enemies')
    bullets = game_world.get_entities_by_category('bullets')
    ship_data = ''
    enemies_data = ''
    bullets_data = ''
    if ship:
        ship_data = f'x: {ship.x}, y: {ship.y}'
    for enemy_idx, enemy in enumerate(enemies):
        enemies_data = enemies_data + f'[{enemy_idx}] x: {enemy.x}, y: {enemy.y}\n'
    for bullet_idx, bullet in enumerate(bullets):
        enemies_data = enemies_data + f'[{bullet_idx}] x: {bullet.x}, y: {bullet.y}\n'
    for enemy_idx, enemy in enumerate(shooting_enemies):
        enemies_data = enemies_data + f'[{enemy_idx}] x: {enemy.x}, y: {enemy.y}\n'
    msg = f'Ship:\n{ship_data}\nEnemies:\n{enemies_data}\nBullets:\n{bullets_data}\n'
    logging.warning(msg)


def debug_scenario_collisions(bullet, enemy):
    bullet_data = f'Bullet {id(bullet)} x: {bullet.x}, y: {bullet.y}\n'
    enemy_data = f'Enemy {id(enemy)} x: {enemy.x}, y: {enemy.y}\n'
    msg = f'Removing elements:\n{bullet_data} {enemy_data}'
    logging.warning(msg)
