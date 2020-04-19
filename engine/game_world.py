
class GameWorld:

    def __init__(self):
        self._entities = dict()

    def add_entity(self, entity, key=None, category=None):
        if key is None and category is None:
            raise ValueError('key or category is mandatory')
        elif key:
            self._entities[key] = entity
        elif category:
            try:
                category_value = self._entities[category]
            except KeyError:
                category_value = []
                self._entities = category_value
            category_value.add(entity)

    def get_entity(self, attr_name):
        entity = None
        try:
            entity = self._entities[attr_name]
        except AttributeError:
            pass
        return entity

    def remove_entity(self, attr_name):
        return self._entities.pop(attr_name)

    @property
    def entities(self):
        return self._entities.items()
