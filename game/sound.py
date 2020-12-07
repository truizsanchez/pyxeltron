import pyxel


def play_sound_shooting():
    # note, tone, volume, effect, speed
    pyxel.sound(0).set(
        # "e2e2c2g1",
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
        # "c2",
        "t",  # tone, square
        "6",
        "n",
        10,
    )
    pyxel.play(0, 0, loop=False)
