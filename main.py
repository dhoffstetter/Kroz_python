from space import Space
from world import World
from player import Player
from monster import Monster
from treasure import Treasure

import random
import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':

    def go_nowhere():
        print("Stay put.")
        root.destroy()

    def go_north():
        print("We should go north.")
        p.space_obj = p.space_obj.move('north')
        root.destroy()

    def go_south():
        print("We should go south.")
        p.space_obj = p.space_obj.move('south')
        root.destroy()

    def go_east():
        print("We should go east.")
        p.space_obj = p.space_obj.move('east')
        root.destroy()

    def go_west():
        print("We should go west.")
        p.space_obj = p.space_obj.move('west')
        root.destroy()

    print('Abandon Hope All Ye Who Enter...')

    w = World()
    w.build_world("basic_world.json")

    p = Player()
    p.space_obj = w.get_random_space_object()

    monster_move_list = [0, 1, 2, 3]
    m = Monster('Bob')
    m.space_obj = w.get_random_space_object()
    while p.space_obj == m.space_obj:
        m.space_obj = w.get_random_space_object()

    t = Treasure("Diamond", 10)
    t.space_obj = w.get_random_space_object()
    while p.space_obj == t.space_obj:
        t.space_obj = w.get_random_space_object()

    while True:
        print("monster", m.space_obj.name)
        print("treasure", t.space_obj.name)
        print("player", p.space_obj.name)

        prompt = (
            f'You are in {p.space_obj.name}\nWhat do you want to do?\n'
        ) + p.space_obj.moving_options_string() + '\n'

        if p.space_obj.is_any_neighbor_space_occupied(m.space_obj):
            prompt += f'Be careful there may be a monster named {m.name} close by...\n'

        print(prompt)

        neighbors = p.space_obj.neighbors

        root = tk.Tk()
        root.title("Your move...")

        nowhere_button = ttk.Button(root, text="Nowhere", command=go_nowhere)
        nowhere_button.pack(side="left", fill="x", expand=True)

        if 'north' in neighbors:
            north_button = ttk.Button(root, text="North", command=go_north)
            north_button.pack(side="left", fill="x", expand=True)

        if 'south' in neighbors:
            south_button = ttk.Button(root, text="South", command=go_south)
            south_button.pack(side="left", fill="x", expand=True)

        if 'east' in neighbors:
            east_button = ttk.Button(root, text="East", command=go_east)
            east_button.pack(side="left", fill="x", expand=True)

        if 'west' in neighbors:
            west_button = ttk.Button(root, text="West", command=go_west)
            west_button.pack(side="left", fill="x", expand=True)

        root.mainloop()

        # user_move = input("Well...")
        # if next_space := p.space_obj.move(user_move):
        #     p.space_obj = next_space
        # else:
        #     print("Invalid Move. ")

        if p.space_obj.in_same_space(m.space_obj):
            print(f'You ran into monster {m.name}.  Game over!\n')
            quit(0)

        if p.space_obj.in_same_space(t.space_obj):
            print(f'You found the {t.name}.  You win!\n')
            quit(0)

        num_of_monster_moves = random.choice(monster_move_list)
        for _ in range(num_of_monster_moves):
            if next_monster_space := m.space_obj.move_to_random_valid_space():
                m.space_obj = next_monster_space
                if p.space_obj.in_same_space(m.space_obj):
                    print(f'The monster {m.name} found you.  Game over!\n')
                    quit(0)
            else:
                print("Monster is stuck")
