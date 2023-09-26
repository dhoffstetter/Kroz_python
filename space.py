import random


class Space:

    def __init__(self, name, space_id):
        self._name = name
        self._namespace_id = space_id
        self._description_short = ""
        self._description_long = ""
        self._neighbors = {}  # Key = direction string, value = id int
        self._neighbor_objects = {}  # Key = direction string, value = Space

    def __str__(self):
        return f'{self.__class__.__name__}: {self._name} {self._neighbors} {self._description_short} {self._description_long}'

    def __repr__(self):
        return f'{self.__class__.__name__}: {self._name} {self._neighbors} {self._description_short} {self._description_long}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description_short(self):
        return self._description_short

    @description_short.setter
    def description_short(self, short_desc):
        self._description_short = short_desc

    @property
    def description_long(self):
        return self._description_long

    @description_long.setter
    def description_long(self, long_desc):
        self._description_long = long_desc

    @property
    def namespace_id(self):
        return self._namespace_id

    @property
    def neighbors(self):
        return self._neighbors

    @property
    def neighbor_objects(self):
        return self._neighbor_objects

    def print_class(self):
        print(self)

    def add_neighbor_id(self, direction, space_id):
        self._neighbors[direction] = space_id

    def add_neighbor_objects(self, direction, space):
        self._neighbor_objects[direction] = space

    def get_neighbor_object_at_direction(self, direction):
        if direction in self._neighbor_objects:
            return self._neighbor_objects[direction]
        return None

    def moving_options_string(self):
        if len(self.neighbor_objects) == 0:
            return "You ain't going anywhere..."
        return "You can go " + ', '.join(self.neighbor_objects.keys()) + "."

    def move(self, direction):
        if direction in self._neighbor_objects:
            return self.neighbor_objects[direction]
        return None

    def move_to_random_valid_space(self):
        if len(self.neighbor_objects) == 0:
            return None
        n_obj_key = random.choice(list(self.neighbor_objects))
        return self._neighbor_objects[n_obj_key]

    def is_any_neighbor_space_occupied(self, other):
        return any(n == other.namespace_id for n in self.neighbors.values())

    def in_same_space(self, other):
        return self._namespace_id == other.namespace_id
