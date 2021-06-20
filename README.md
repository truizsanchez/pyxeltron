# pyxeltron
Multidirectional shooter using [pyxel retro game engine](https://pypi.org/project/pyxel/)

The game is inspired in classics like [Robotron: 2084](https://en.wikipedia.org/wiki/Robotron:_2084) and [Llamatron](https://en.wikipedia.org/wiki/Llamatron)

The goal of the project is also creating a generic 2D game engine being agnostic to pyxel and rendering in general. 

That's why the project have this structure:
* `engine`. Base class for all entities of the game, the gameworld, collisions and movement
* `game`. Pyxeltron game modelling using the `engine` capabilities (through inheritance etc.), without render definitions.
* `render`. Pyxeltron render (assets, entities mapping, glue file between game engine and render, etc.)

## How to run
Run `render/main.py`

There are also a windows executable packing the game, in `standalone_executable/pyxeltron.exe`

## Roadmap
* Create new types of enemies that shoots, drop bombs etc.
* Add power-up items.
* Local and internet cooperative (2 players).
