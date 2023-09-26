from being import Being


class Monster(Being):

    def __init__(self, name, space_obj=None):
        self._name = name
        self._description = "Big ugly monster."
        Being.__init__(self, space_obj)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

