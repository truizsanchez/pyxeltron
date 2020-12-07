import pyxel


def play_sound_shooting():
    # note, tone, volume, effect, speed
    pyxel.sound(0).set(
        "c2",
        "t",  # tone, square
        "6",
        "n",
        10,
    )
    pyxel.play(0, 0, loop=False)


def play_sound_ship_destroyed():
    # note, tone, volume, effect, speed
    pyxel.sound(0).set(
        "e2e2c2g1",
        "t",  # tone
        "6",
        "n",
        10,
    )
    pyxel.play(0, 0, loop=False)


def play_sound_enemy_down():
    # note, tone, volume, effect, speed
    pyxel.sound(0).set(
        "a1a1g1",
        "s",  # tone
        "6",
        "n",
        10,
    )
    pyxel.play(0, 0, loop=False)
