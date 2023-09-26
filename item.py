class Item:

    def __init__(self, name, space_obj=None):
        self._space_obj = space_obj
        self._name = name
        self._description = "Item"
        self._has_owner = False
        self._owner = False

    @property
    def name(self):
        return self._name

    @property
    def space_obj(self):
        return self._space_obj

    @space_obj.setter
    def space_obj(self, space):
        self._space_obj = space

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def has_owner(self):
        return self._has_owner

    def set_owner(self, owner):
        if owner is None:
            self._has_owner = False
            self._owner = None
        else:
            self._has_owner = True
            self._owner = owner


