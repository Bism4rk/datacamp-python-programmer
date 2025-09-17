import numpy as np

names = ['Blaziken', 'Altaria', 'Aggron', 'Chesnaught', 'Abomasnow', 'Caterpie', 'Delibird']

poke_list= [('Blaziken', np.int64(530), np.float64(88.33333333333333)),  ('Altaria', np.int64(490), np.float64(81.66666666666667)), ('Aggron', np.int64(530), np.float64(88.33333333333333)), ('Chesnaught', np.int64(530), np.float64(88.33333333333333)), ('Abomasnow', np.int64(494), np.float64(82.33333333333333)), ('Caterpie', np.int64(195), np.float64(32.5)), ('Delibird', np.int64(330), np.float64(55.0))]

# Create a list of lists with each pokémon's HP, attack, defense, special attack, special defense, and speed
stats = np.array([
    [80, 120, 70, 110, 70, 80],
    [75, 100, 70, 110, 70, 80],
    [70, 130, 80, 60, 80, 90],
    [88, 110, 100, 80, 100, 80],
    [90, 92, 75, 92, 75, 80],
    [45, 30, 35, 20, 20, 45],
    [45, 55, 40, 30, 30, 75]
])