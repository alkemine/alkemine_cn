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
from auto_people import get_temple, write_post


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
    d1 = ['pub1', "Origin of high thermoelectric performance with wide range of compositions for BixSb2-xTe3 "
                  "single quintu-ple layer", "Composition regulation of semiconductors can engineer the band "
                                             "structures and hence optimize their properties " \
    "for better applications. Herein, we report the BixSb2􀀀xTe3 (BST) single QL with high ZT values (1.2 to 1.5) " \
    "at 300 K across a wide range of compositions 0 < x  1. The improved description of band structures by the " \
    "unfold method reveals the multi-valley bands near the Fermi energy. The high power factor of p-type BST single " \
    "QL originates from the robust multi- valley character of valence bands. The wide composition range is ensured " \
    "by the valence bands maximum dominated by the antibonding states of Sb-Te2 bonds, which would be affected " \
    "little by the disorder. The optimal composition for BST single QL is attributed to the different " \
    "contributionsfrom Sb and Bi to the valence band edge. This work paves the way for the further combination " \
    "of large power factor and low thermal conductivity across a wide range of compositions.", '#', 1]
    
    a = get_all_paper([d1, d1, d1, d1, d1])
    print(a)