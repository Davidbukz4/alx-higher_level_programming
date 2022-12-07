#!/usr/bin/python3

attack = {'quick': (lambda: print('Quick Attack')),
            'power': (lambda: print('Power attack')),
            'miss': (lambda: print('Missed Attack'))}

import random

attackKey = random.choice(list(attack.keys()))
attack[attackKey]()
