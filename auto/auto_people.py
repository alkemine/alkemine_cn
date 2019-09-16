#   coding: utf-8
#   This file is part of potentialmind.

#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2019/09/16"

import os
from string import Template


def get_temple(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        people_temple = f.read()
    return Template(people_temple)


def get_one_person_post(name, personal_text, pic_name=None, person_index='#'):
    __people_temple_fn = os.path.join(os.path.dirname(__file__), 'temples', 'temple_people_post')
    config = get_temple(__people_temple_fn)
    variables = {"name": name,
                 "pic_name": '%s.jpg' % (name if not pic_name else pic_name),
                 "personal_text": personal_text,
                 "person_index": person_index}

    _input = config.safe_substitute(**variables) + '\n'
    # write_post('test', _input, 'w')
    return _input


def get_col(data):
    all_col = [get_one_person_post(*i) for i in data]
    __col_temple_fn = os.path.join(os.path.dirname(__file__), 'temples', 'temple_people_col')
    config = get_temple(fn=__col_temple_fn)
    variables = {"many_posts": ''.join(all_col)}
    _input = config.safe_substitute(**variables) + '\n'
    return _input


def get_row(data):
    """
    len(data) == 3
    :param data: [col1, col2, col3]
    :return: str
    """
    assert len(data) == 3
    all_row = [get_col(i) for i in data]
    __row_temple_fn = os.path.join(os.path.dirname(__file__), 'temples', 'temple_people_row')
    config = get_temple(fn=__row_temple_fn)
    variables = {"many_columns": ''.join(all_row)}
    _input = config.safe_substitute(**variables) + '\n'
    return _input


def write_post(fn, data, mode='w'):
    with open(fn, mode, encoding='utf-8') as f:
        f.write(data)


if __name__ == '__main__':
    # write_one_person_post(name='GuanjieWang', pic_name='pic1', personal_text='shasfldkfjskld sdgkjds agghaklj')
    dd = [['GuanjieWang', 'sdlkfjls', 'pic1'], ['sdfs', 'lllll', 'pic1', 'sdklf']]
    a = get_row(data=[dd, dd+dd, dd+dd+dd])
    write_post(fn='test', data=a)
