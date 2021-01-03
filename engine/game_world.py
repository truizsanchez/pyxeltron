from typing import List, Dict, Union, Tuple

from engine.physics.movement import update_position
from engine.entities.base import BaseEntity


class GameWorld:

    WIDTH = 160
    HEIGHT = 120

    def __init__(self):
        self._entities: Dict[str, Union[List[BaseEntity], BaseEntity]] = dict()

    def add_entity(self, entity: BaseEntity, name: str) -> None:
        self._entities[name] = entity

    def get_entity(self, name: str) -> BaseEntity:
        return self._entities.get(name)

    def remove_entity(self, name: str) -> None:
        self._entities.pop(name)

    def add_entity_to_category(self, entity: BaseEntity, category: str) -> None:
        try:
            category_value = self._entities[category]
        except KeyError:
            category_value = []
            self._entities[category] = category_value
        category_value.append(entity)

    def get_entities(self, category: Union[str, List, Tuple]) -> List[BaseEntity]:
        if isinstance(category, str):
            entities = self._entities.get(category, [])
        else:
            entities = []
            for k in category:
                entities.extend(self._entities.get(k, []))
        return entities

    def remove_entity_from_category(self, entity: BaseEntity, category: str) -> None:
        entities = self._entities[category]
        entities.remove(entity)

    def clear_category(self, category: str) -> None:
        self._entities[category] = []

    def _update_positions(self) -> None:
        for entity in self.entities:
            update_position(entity, self.WIDTH, self.HEIGHT)

    @property
    def entities(self) -> List[BaseEntity]:
        entities = []
        for element in self._entities.values():
            if isinstance(element, BaseEntity):
                entities.append(element)
            elif isinstance(element, list):
                entities.extend(element)
        return entities
