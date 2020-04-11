from engine.entities.base import BaseEntity
from render.entities.ship import ShipRender


class Ship(BaseEntity):
    RENDER_CLASS = ShipRender
