#   coding: utf-8
#   This file is part of potentialmind.

#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2019/09/16"

from auto_people import get_all, write_post
import pandas as pd
from copy import deepcopy

EMPTY_INFO = ['...', 'pic1', '...', '...', None, '#']

CN2EN = {"教师": "Teachers",
         "博士生": "Ph.D",
         "研究生1年级": "Master 1",
         "研究生2年级": "Master 2",
         "研究生3年级": "Master 3",
         "本科生": "Undergraduate",
         "已毕业学生": "Graduated"}


class OnePerson(object):
    
    def __init__(self, data, style=0):
        # style == 1: 个人简介高度为280px， 否则为180px
        assert isinstance(data, pd.Series)
        if style:
            intro_style = 'person_tech_introduction'
        else:
            intro_style = 'person_introduction'
            
        homepage_for_person = data['个人主页地址'] if isinstance(data['个人主页地址'], str) else '#'
        self.data = [data['中文姓名'], data['英文姓名'], data['自我介绍100字以内'], data['个人邮箱'], None,
                     homepage_for_person, intro_style]
        

def read_data(fn, type):
    a = pd.read_csv(fn)
    need_process = a[a['职位'] == type]
    if type == '老师':
        intro_style = 1
    else:
        intro_style = 0
        
    data = [OnePerson(i[1], style=intro_style).data for i in need_process.iterrows()]
    return data


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
    w = get_all(data=data)
    write_post(fn='test', data=w)


def general(data_name, name_index=None, web_name=None, data=None):
    if web_name is not None:
        pass
    else:
        web_name = data_name
    
    if data is not None:
        pass
    else:
        phdall = read_data(fn='data.csv', type=data_name)
        sss = [a[0] for a in phdall]
        print(sss)
        index_dic = dict(zip(sss, range(len(sss))))
        data = [[phdall[index_dic[j]] for j in i] for i in name_index]
    
    w = get_all(data=data, page_engname=CN2EN[web_name], page_name=web_name)
    write_post(fn='test', data=w)
    
    
if __name__ == '__main__':
    teach_dict = [['孙志梅', '周健', '缪奶华', '司晨', '祝令刚']]
    phd_dict = [['李圳', '杨辉', '邱实'],
                ['彭琼', '于亚东', '刘宾', '张毕堃'],
                ['李强', '黄永达','胡述伟', '张康', '王冠杰'],
                ['彭力宇', '甘宇', '张震', '吴忌征']]
    master1_dict = [['王冰', '王雷', '刘阳', '孙雨奇', '熊一庭'],
                    ['宁兴洋', '王二鹏', '周润晖']]
    master2_dict = [['李开旗', '陈启凡', '陈佳天', '孟喆', '张斌晨'],
                    ['李薇']]
    master3_dict = [['李杰', '吴浩', '崔京京', '焦静云', '陈明威'],
                    ['湛晓雪']]
    
    master = [master1_dict, master2_dict, master3_dict]
    undergraduated_dict = [[EMPTY_INFO, EMPTY_INFO, EMPTY_INFO]]
    graduated_dict = [['郭忠路', '萨百晟', '潘元春', '廖加敏', '程影星'],
                      ['张临川', '张英干', '苏忠亮', '丁宗财', '林道斌']]
    # general(data_name="老师", web_name="教师", name_index=teach_dict)
    # general(data_name="博士生", name_index=phd_dict)
    general(data_name="硕士1年级", web_name="研究生1年级", name_index=master1_dict)
    # general(data_name="硕士2年级", web_name="研究生2年级", name_index=master2_dict)
    # general(data_name="硕士3年级", web_name="研究生3年级", name_index=master3_dict)
    # general(data_name="本科生", web_name="本科生", data=undergraduated_dict)
    # general(data_name="已毕业学生", web_name="已毕业学生", name_index=graduated_dict)
