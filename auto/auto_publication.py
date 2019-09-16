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
from auto.auto_people import get_temple, write_post


def get_one_paper(pic_name, paper_name, paper_abstract, paper_href='#', num='1'):
    __paper_temple_fn = os.path.join(os.path.dirname(__file__), 'temples', 'temple_paper_publication_one')
    config = get_temple(__paper_temple_fn)
    variables = {"number": num,
                 "paper_href": paper_href,
                 "paper_pic_name": '%s.jpg' % pic_name,
                 "paper_name": paper_name,
                 "paper_abstract": paper_abstract}

    _input = config.safe_substitute(**variables) + '\n'
    write_post('test', _input, 'w')
    return _input


def get_all_paper(data):

    __all_papers_fn = os.path.join(os.path.dirname(__file__), 'temples', 'temple_paper_publication_all')
    config = get_temple(__all_papers_fn)
    all_papers = [get_one_paper(*i) for i in data]
    variables = {"all_papers": ''.join(all_papers)}
    _input = config.safe_substitute(**variables)
    write_post('test.html', _input, 'w')
    return _input


if __name__ == '__main__':
    d1 = ['pic1', 'PUBLICATION1', 'sdkfjlss  gdgjdlkg gdslfjs gdlgjl', '#', 1]
    a = get_all_paper([d1, d1, d1, d1, d1])
    print(a)