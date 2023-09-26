class Being:

    def __init__(self, space_obj=None):
        self._space_obj = space_obj

    @property
    def space_obj(self):
        return self._space_obj

    @space_obj.setter
    def space_obj(self, space):
        self._space_obj = space
