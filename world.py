import json
import random
import json_keys as jk
from space import Space


class World:

    def __init__(self):
        self._spaces = {}  # Key = id (int), value = Space with that id
        self._space_list = []

    def build_world(self, world_file_json):
        with open(world_file_json) as f:
            spaces = json.load(f)
            for space_info in spaces[jk.SPACES]:
                s = Space(space_info[jk.NAME], space_info[jk.ID])
                self._spaces[space_info[jk.ID]] = s
                s.description_short = space_info.get(jk.DESC_SHORT, "They forgot me!")
                s.description_long = space_info.get(jk.DESC_LONG, "They really forgot me!")
                for neighbor in space_info[jk.NEIGHBORS]:
                    s.add_neighbor_id(neighbor[jk.DIR], neighbor[jk.N_ID])
        for key_id, value_space in self._spaces.items():
            for key_direction, value_n_id in value_space.neighbors.items():
                if value_n_id in self._spaces.keys():
                    value_space.add_neighbor_objects(key_direction, self._spaces[value_n_id])
                else:
                    print(f'Key Error {value_n_id}')
        self._space_list = list(self._spaces)

    def get_random_space_ids(self):
        return random.choice(self._space_list)

    def get_random_space_object(self):
        return self._spaces[self.get_random_space_ids()]
