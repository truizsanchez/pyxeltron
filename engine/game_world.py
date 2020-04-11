
class GameWorld:

    def add_entity(self, attr_name, value):
        self.__setattr__(attr_name, value)

    def get_entity(self, attr_name):
        entity = None
        try:
            entity = self.__getattribute__(attr_name)
        except AttributeError:
            pass
        return entity

    def remove_entity(self, attr_name):
        self.__delattr__(attr_name)

    @property
    def entities(self):
        items = []
        for entity in self.__dict__.items():
            items.append(entity)
        return items
