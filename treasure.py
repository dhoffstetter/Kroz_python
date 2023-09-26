from item import Item


class Treasure(Item):
    def __init__(self, name, value, space_obj=None):
        self._value = value
        Item.__init__(self, name, space_obj)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

