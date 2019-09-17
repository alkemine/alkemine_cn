#   coding: utf-8
#   This file is part of potentialmind.

#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2019/09/16"

from auto_people import get_row, write_post
import pandas as pd
from copy import deepcopy

EMPTY_INFO = ['...', 'pic1', '...', '...', None, '#']


class OnePerson(object):
    
    def __init__(self, data):
        assert isinstance(data, pd.Series)
        homepage_for_person = data['个人主页地址'] if isinstance(data['个人主页地址'], str) else '#'
        self.data = [data['中文姓名'], data['英文姓名'], data['自我介绍100字以内'], data['个人邮箱'], None, homepage_for_person]
        

def read_data(fn, type):
    a = pd.read_csv(fn)
    need_process = a[a['职位'] == type]
    data = [OnePerson(i[1]).data for i in need_process.iterrows()]
    return data

def undergraduate():
    data = [[EMPTY_INFO, EMPTY_INFO],
            [EMPTY_INFO],
            [EMPTY_INFO],
            [EMPTY_INFO],
            [EMPTY_INFO]]
    w = get_row(data=data)
    write_post(fn='test', data=w)

def teacher():
    a = read_data(fn='data.csv', type='老师')
    w = get_row(data=[[a[0]], [a[1]], [a[2]]])
    write_post(fn='test', data=w)
    
def phd():
    phdall = read_data(fn='data.csv', type='博士生')
    sss = [a[0] for a in phdall]
    index_dic = dict(zip(sss, range(len(sss))))
    data = [[phdall[index_dic['彭琼']], phdall[index_dic['王冠杰']], phdall[index_dic['彭力宇']], phdall[index_dic['张震']]],
            [phdall[index_dic['于亚东']], phdall[index_dic['黄永达']], EMPTY_INFO, phdall[index_dic['吴忌征']]],
            [phdall[index_dic['张毕堃']], phdall[index_dic['胡述伟']] ],
            [EMPTY_INFO, phdall[index_dic['张康']]]]
    w = get_row(data=data)
    write_post(fn='test', data=w)

def m3():
    phdall = read_data(fn='data.csv', type='硕士3年级')
    sss = [a[0] for a in phdall]
    index_dic = dict(zip(sss, range(len(sss))))
    # print(index_dic)
    # exit()
    data = [[phdall[index_dic['李杰']], ],
            [phdall[index_dic['吴浩']], ],
            [phdall[index_dic['崔京京']], ]]
    w = get_row(data=data)
    write_post(fn='test', data=w)


def m2():
    phdall = read_data(fn='data.csv', type='硕士2年级')
    sss = [a[0] for a in phdall]
    index_dic = dict(zip(sss, range(len(sss))))
    # print(index_dic)
    # exit()
    data = [[phdall[index_dic['李开旗']], ],
            [phdall[index_dic['孟喆']], ],
            [phdall[index_dic['陈启凡']],],]
    w = get_row(data=data)
    write_post(fn='test', data=w)


def m1():
    phdall = read_data(fn='data.csv', type='硕士1年级')
    sss = [a[0] for a in phdall]
    index_dic = dict(zip(sss, range(len(sss))))
    # print(index_dic)
    # exit()
    data = [[phdall[index_dic['王冰']], phdall[index_dic['宁兴洋']]],
            [phdall[index_dic['王雷']], phdall[index_dic['王二鹏']]],
            [phdall[index_dic['刘阳']], ],
            [phdall[index_dic['孙雨奇']], ],
            [phdall[index_dic['熊一庭']], ],]
    w = get_row(data=data)
    write_post(fn='test', data=w)

def graduated():
    phdall = read_data(fn='data.csv', type='已毕业学生')
    sss = [a[0] for a in phdall]
    index_dic = dict(zip(sss, range(len(sss))))
    # print(index_dic)
    # exit()
    data = [[phdall[index_dic['萨百晟']], ],
            [phdall[index_dic['郭忠路']], ],
            [phdall[index_dic['程影星']], ],
            ]
    w = get_row(data=data)
    write_post(fn='test', data=w)


if __name__ == '__main__':
    undergraduate()
