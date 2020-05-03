from engine.physics.movement import update_position
from engine.entities.base import BaseEntity


class GameWorld:

    WIDTH = 160
    HEIGHT = 120

    def __init__(self):
        self._entities = dict()

    def add_entity_to_category(self, entity, category):
        try:
            category_value = self._entities[category]
        except KeyError:
            category_value = []
            self._entities[category] = category_value
        return category_value.append(entity)

    def add_entity(self, entity, name):
        self._entities[name] = entity

    def get_entity(self, name):
        return self._entities.get(name)

    def get_entities_by_category(self, category):
        return self._entities.get(category)

    def remove_entity(self, name):
        return self._entities.pop(name)

    def remove_entity_from_category(self, category, entity):
        entities = self._entities[category]
        return entities.remove(entity)

    def _update_positions(self):
        for entity in self.entities:
            update_position(entity, self.WIDTH, self.HEIGHT)
            if entity.__class__.__name__ == 'Ship':
                print(f'{entity.x}  {entity.y}')

    @property
    def entities(self):
        entities = []
        for element in self._entities.values():
            if isinstance(element, BaseEntity):
                entities.append(element)
            elif isinstance(element, list):
                entities.extend(element)
        return entities
