chance_dict = \
    [
        # healing 2
        [
            [
                {'white': 0.2, 'green': 0.2, 'red': 0.2, 'black': 0.4}
            ]
        ],
        # healing 3
        [
            # surgery 0
            [
                # field 0
                {'white': 0.2, 'green': 0.3, 'red': 0.3, 'black': 0.2},
                # field 1
                {'white': 0.3, 'green': 0.3, 'red': 0.2, 'black': 0.2},
                # field 2
                {'white': 0.4, 'green': 0.3, 'red': 0.1, 'black': 0.2},
            ],
            # surgery 1
            [
                # field 0
                {'white': 0.3, 'green': 0.2, 'red': 0.3, 'black': 0.2},
                # field 1
                {'white': 0.4, 'green': 0.2, 'red': 0.2, 'black': 0.2},
                # field 2
                {'white': 0.5, 'green': 0.2, 'red': 0.1, 'black': 0.2},
            ],
            # surgery 2
            [
                # field 0
                {'white': 0.4, 'green': 0.1, 'red': 0.3, 'black': 0.2},
                # field 1
                {'white': 0.5, 'green': 0.1, 'red': 0.2, 'black': 0.2},
                # field 2
                {'white': 0.6, 'green': 0.1, 'red': 0.1, 'black': 0.2},
            ],
        ],
        # healing 4
        [
            # surgery 0
            [
                # field 0
                {'white': 0.4, 'green': 0.2, 'red': 0.2, 'black': 0.2},
                # field 1
                {'white': 0.5, 'green': 0.2, 'red': 0.1, 'black': 0.2},
                # field 2
                {'white': 0.6, 'green': 0.2, 'red': 0.0, 'black': 0.2},
            ],
            # surgery 1
            [
                # field 0
                {'white': 0.5, 'green': 0.1, 'red': 0.2, 'black': 0.2},
                # field 1
                {'white': 0.6, 'green': 0.1, 'red': 0.1, 'black': 0.2},
                # field 2
                {'white': 0.7, 'green': 0.1, 'red': 0.0, 'black': 0.2},
            ],
            # surgery 2
            [
                # field 0
                {'white': 0.6, 'green': 0.0, 'red': 0.2, 'black': 0.2},
                # field 1
                {'white': 0.7, 'green': 0.0, 'red': 0.1, 'black': 0.2},
                # field 2
                {'white': 0.8, 'green': 0.0, 'red': 0.0, 'black': 0.2},
            ],
        ],
    ]


def chances(healer_one, assistant_one=None, assistant_two=None):
    result = chance(*healer_one)
    if assistant_one:
        mod = 1 - result['white']
        temp = chance(*assistant_one)
        result['white'] += mod * temp['white']
        result['green'] = mod * temp['green']
        result['red'] = mod * temp['red']
        result['black'] = mod * temp['black']
    if assistant_two:
        mod = 1 - result['white']
        temp = chance(*assistant_two)
        result['white'] += mod * temp['white']
        result['green'] = mod * temp['green']
        result['red'] = mod * temp['red']
        result['black'] = mod * temp['black']
    return result


def chance(healing, surgery=0, field=0):
    assert (healing == 2 and surgery == 0 and field == 0) or (3 <= healing <= 4)
    assert 0 <= surgery <= 2
    assert 0 <= field <= 2
    return chance_dict[healing - 2][surgery][field]
