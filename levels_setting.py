import csv

SIZE = HEIGHT, WIDTH = 1280, 720
FPS = 60
font = 'data/Fonts/NormalFont.ttf'
font_size = 18
health_bar_width, energy_bar_width = 20, 20
health_bar_height, energy_bar_height = 200, 150


def import_csv(way):
    with open(way, encoding='utf-8') as file:
        spisok = csv.reader(file, delimiter=',')
        spisok = [i for i in spisok]
        return spisok


pict_items = {
    'трава': ['data/grass/grass_1.png',
              'data/grass/grass_2.png',
              'data/grass/grass_3.png',
              'data/grass/grass_4.png',
              'data/grass/grass_5.png',
              'data/grass/grass_6.png',
              'data/grass/grass_7.png',
              'data/grass/grass_8.png',
              ]

}

slovar_layouts = {
    'границы': import_csv('data/level_graphics/obstical_границы.csv'),
    'трава': import_csv('data/level_graphics/obstical_обекты.csv'),
    'монстры': import_csv('data/level_graphics/monsters_monsters.csv')
}

player_animation = {
    'up': ['data/animations/main_charecter/up/up_1.png',
           'data/animations/main_charecter/up/up_2.png',
           'data/animations/main_charecter/up/up_3.png',
           'data/animations/main_charecter/up/up_4.png'
           ],
    'down': ['data/animations/main_charecter/down/down_1.png',
             'data/animations/main_charecter/down/down_2.png',
             'data/animations/main_charecter/down/down_3.png',
             'data/animations/main_charecter/down/down_4.png'
             ],

    'right': ['data/animations/main_charecter/right/right_1.png',
              'data/animations/main_charecter/right/right_2.png',
              'data/animations/main_charecter/right/right_3.png',
              'data/animations/main_charecter/right/right_4.png'
              ],

    'left': ['data/animations/main_charecter/left/left_1.png',
             'data/animations/main_charecter/left/left_2.png',
             'data/animations/main_charecter/left/left_3.png',
             'data/animations/main_charecter/left/left_4.png'
             ],

    'attack_up': 'data/animations/main_charecter/attack/attack_up.png',
    'attack_down': 'data/animations/main_charecter/attack/attack_down.png',
    'attack_left': 'data/animations/main_charecter/attack/attack_left.png',
    'attack_right': 'data/animations/main_charecter/attack/attack_right.png',
    'down_idle': 'data/animations/main_charecter/idle/main_idle.png',
    'up_idle': 'data/animations/main_charecter/idle/up_idle.png',
    'left_idle': 'data/animations/main_charecter/idle/left_idle.png',
    'right_idle': 'data/animations/main_charecter/idle/right_idle.png',
    'dead': 'data/animations/main_charecter/Dead.png'
}

weapons = {
    'lance': {'cooldown': 400,
              'damage': 25,
              'attack_cooldown': '',
              'image': ['data/weapons/lance_up.png',
                        'data/weapons/lance_down.png',
                        'data/weapons/lance_right.png',
                        'data/weapons/lance_left.png']
              }
}
monsters = {
    'bamboo': {'health': 100, 'damage': 15, 'type_attack': 'bamboo', 'resistance': 2,
               'speed': 2, 'attack_radius': 50, 'notice_radius': 300, 'attack_cooldown': 800,
               'idle': ['data/monsters/bamboo/idle_1.png',
                        'data/monsters/bamboo/idle_2.png',
                        'data/monsters/bamboo/idle_3.png',
                        'data/monsters/bamboo/idle_4.png',
                        ]
               },
    'slime': {'health': 100, 'damage': 20, 'type_attack': 'slime', 'resistance': 2,
              'speed': 3, 'attack_radius': 50, 'notice_radius': 350, 'attack_cooldown': 400,
              'idle': ['data/monsters/slime/idle_1.png',
                       'data/monsters/slime/idle_2.png',
                       'data/monsters/slime/idle_3.png',
                       'data/monsters/slime/idle_4.png',
                       ]
              }
}
