from typing import List

import pyxel

from game.game_world import PyxelTronGameWorld, Action, ResultType, ApplicationState
from game.sound import play_sound_shooting, play_sound_ship_destroyed, play_sound_enemy_down
from render.constants import TILESET, TILESET_PATH, SHIP_PATH, SHIP, PICO8_PALETTE, COLOR_BLACK, CAPTION
from render.icons.heart import HeartIcon
from settings import DEBUG


class PyxelTron:
    def __init__(self):
        self.world = PyxelTronGameWorld()
        pyxel.init(self.world.WIDTH, self.world.HEIGHT, caption=CAPTION, palette=PICO8_PALETTE)
        pyxel.image(TILESET).load(0, 0, TILESET_PATH)
        pyxel.image(SHIP).load(0, 0, SHIP_PATH)
        self.world.initialize()
        pyxel.run(self.update, self.draw)

    def render_world(self) -> None:
        if self.world.state in [ApplicationState.PLAYING, ApplicationState.PAUSE_COOLDOWN]:
            for entity in self.world.entities:
                if entity.render:
                    pyxel.blt(
                        entity.x,
                        entity.y,
                        entity.render.IMAGE_BANK,
                        entity.render.u,
                        entity.render.v,
                        entity.render.WIDTH,
                        entity.render.HEIGHT,
                        COLOR_BLACK
                    )
            self._render_playing_ui()
        elif self.world.state == ApplicationState.GAME_FINISHED:
            pyxel.text(30, 50, 'CONGRATULATIONS!', 4)
            pyxel.text(30, 60, 'PRESS C TO PLAY AGAIN', 4)
        elif self.world.state == ApplicationState.GAME_OVER:
            pyxel.text(30, 50, 'GAME OVER', 4)
            pyxel.text(30, 60, 'PRESS C TO PLAY AGAIN', 4)

    def _render_playing_ui(self):
        pyxel.text(1, 1, f'Level {self.world.level}', 4)

        for live in range(self.world.lives):
            x = 130 + live * 10
            pyxel.blt(
                x,
                1,
                HeartIcon.IMAGE_BANK,
                HeartIcon.U,
                HeartIcon.V,
                HeartIcon.WIDTH,
                HeartIcon.HEIGHT,
                COLOR_BLACK
            )

    def _handle_input(self) -> List[Action]:
        actions = []
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.world.state == ApplicationState.PLAYING:
            action_movement = self._handle_input_movement()
            if action_movement:
                actions.append(action_movement)
            if pyxel.btnp(pyxel.KEY_SPACE):
                actions.append(Action.SHOOT)
        elif pyxel.btnp(pyxel.KEY_C):
            self.world.initialize()
        return actions

    def _handle_input_movement(self):
        left_pressed = pyxel.btn(pyxel.KEY_LEFT)
        right_pressed = pyxel.btn(pyxel.KEY_RIGHT)
        up_pressed = pyxel.btn(pyxel.KEY_UP)
        down_pressed = pyxel.btn(pyxel.KEY_DOWN)
        action = None
        if left_pressed and up_pressed:
            action = Action.MOVE_LEFT_UP
        elif left_pressed and down_pressed:
            action = Action.MOVE_LEFT_DOWN
        elif right_pressed and up_pressed:
            action = Action.MOVE_RIGHT_UP
        elif right_pressed and down_pressed:
            action = Action.MOVE_RIGHT_DOWN
        elif left_pressed:
            action = Action.MOVE_LEFT
        elif right_pressed:
            action = Action.MOVE_RIGHT
        elif up_pressed:
            action = Action.MOVE_UP
        elif down_pressed:
            action = Action.MOVE_DOWN
        return action

    def update(self) -> None:
        actions = self._handle_input()
        if self.world.state in [ApplicationState.PLAYING, ApplicationState.PAUSE_COOLDOWN]:
            results = self.world.update_scenario(actions)
            for result in results:
                self._evaluate_result(result)

    def _evaluate_result(self, result):
        if result.result_type == ResultType.SHIP_SHOOTING:
            play_sound_shooting()
        elif result.result_type == ResultType.SHIP_DESTROYED:
            self.world.load_level(self.world.level)
            play_sound_ship_destroyed()
        elif result.result_type == ResultType.ENEMY_DOWN:
            play_sound_enemy_down()
        elif result.result_type == ResultType.LEVEL_CLEARED:
            self.world.level += 1
            self.world.load_level(self.world.level)

    def draw(self) -> None:
        pyxel.cls(0)
        self.render_world()
        if DEBUG:
            msg = f''
            pyxel.text(100, 110, msg, 4)


if __name__ == '__main__':
    PyxelTron()
