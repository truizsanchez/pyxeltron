import pyxel


def play_sound_shooting():
    # note, tone, volume, effect, speed
    pyxel.sound(0).set(
        "c2",
        "t",  # tone
        "6",
        "n",
        10,
    )
    pyxel.play(0, 0, loop=False)


def play_sound_ship_destroyed():
    # note, tone, volume, effect, speed
    pyxel.sound(0).set(
        "a0",
        "n",  # tone
        "6",
        "n",
        10,
    )
    pyxel.play(0, 0, loop=False)


def play_sound_enemy_down():
    # note, tone, volume, effect, speed
    pyxel.sound(0).set(
        "c2c2c2",
        "n",  # tone
        "6",
        "n",
        10,
    )
    pyxel.play(0, 0, loop=False)
