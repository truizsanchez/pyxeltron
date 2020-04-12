from aabbtree import AABBTree, AABB


class GameWorld:

    def __init__(self):
        self._entities = dict()
        self._tree = AABBTree()

    def add_entity(self, attr_name, entity):
        self._entities[attr_name] = entity
        box = AABB([(entity.x, entity.x + entity.width),
                    (entity.y, entity.y + entity.width)])
        self._tree.add(box)

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
