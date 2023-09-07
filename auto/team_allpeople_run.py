#   coding: utf-8
#   This file is part of potentialmind.

#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2019/09/16"

from temple_auto_people import get_all, write_post
import pandas as pd
from copy import deepcopy

EMPTY_INFO = ['...', 'pic1', '...', '...', None, '#']

CN2EN = {"教师": "Teachers",
         "博士后": "Postdoc",
         "博士生": "Ph.D",
         "研究生1年级": "Master 1",
         "研究生2年级": "Master 2",
         "研究生3年级": "Master 3",
         "本科生": "Undergraduate",
         "2022年已毕业学生": "Graduated",
         "2021年已毕业学生": "Graduated",
         "2020年已毕业学生": "Graduated",
         "2019年已毕业学生": "Graduated",
         "2018年已毕业学生": "Graduated",
         "2017年已毕业学生": "Graduated",
         "2016年之前已毕业学生": "Graduated"}


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
        

def read_data(fn, data_type=None):
    a = pd.read_csv(fn)
    if data_type is not None:
        need_process = a[a['职位'] == data_type]
    else:
        need_process = a
        
    if data_type == '老师':
        intro_style = 1
    else:
        intro_style = 0
        
    data = [OnePerson(i[1], style=intro_style).data for i in need_process.iterrows()]
    return data


def general(data_name, name_index=None, web_name=None, data=None, output_filename='test.html', is_wri=True):
    if web_name is not None:
        pass
    else:
        web_name = data_name
    
    if data is not None:
        data = data
    else:
        phdall = read_data(fn='team_allpeople_data.csv', data_type=None)
        sss = [a[0] for a in phdall]
        index_dic = dict(zip(sss, range(len(sss))))
        
        data = []
        for i in name_index:
            tt = []
            for j in i:
                try:
                    tt.append(phdall[index_dic[j]])
                    print("Done: %s" % j)
                except KeyError:
                    print("Can't find data of %s, set empty" % j)
                    tt.append(EMPTY_INFO)
                    
            data.append(tt)
        # data = [[phdall[index_dic[j]] for j in i] for i in name_index]
        
    w = get_all(data=data, page_engname=CN2EN[web_name], page_name=web_name)
    if is_wri:
        write_post(fn=output_filename, data=w)
    else:
        return w


def _read_json(fn):
    import json
    with open(fn, 'r', encoding='utf-8') as f:
        all_peoples = json.load(f)
    return all_peoples
    

def deal_many_part(data, output_filename='test.html'):
    head_end_linenumber = 91
    tail_start_linenumber = -3
    
    dd = [general(**i) for i in data]
    tmp_dd = []
    for m in range(len(dd)):
        if m == 0:
            tmp_dd.append('\n'.join(dd[m].split('\n')[:tail_start_linenumber]))
        elif m == (len(dd)-1):
            tmp_dd.append('\n'.join(dd[m].split('\n')[head_end_linenumber:]))
        else:
            tmp_dd.append('\n'.join(dd[m].split('\n')[head_end_linenumber:tail_start_linenumber]))
    
    write_post(fn=output_filename, data='\n'.join(tmp_dd))
    

def run(teacher=1, phd=0, ungrad=0, domaster=0, graded=0):
    all_people = _read_json('team_allpeople_index.index')
    teach_dict = all_people['teachers']
    phd_dict = all_people['phds']
    postdoc = all_people['postdoc']
    master1_dict = all_people['master1']
    master2_dict = all_people['master2']
    master3_dict = all_people['master3']
    undergraduated_dict = all_people['undergraduated']

    graduated2022_dict = all_people['graduated2022']
    graduated2021_dict = all_people['graduated2021']
    graduated2020_dict = all_people['graduated2020']
    graduated2019_dict = all_people['graduated2019']
    graduated2018_dict = all_people['graduated2018']
    graduated2017_dict = all_people['graduated2017']
    graduated2016_dict = all_people['graduated2016']
    
    phd_and_postdoc = [{"data_name": "博士生", "web_name": "博士后", "name_index": postdoc, "is_wri": False},
                  {"data_name": "博士生", "web_name": "博士生", "name_index": phd_dict, "is_wri": False}]
    master = [{"data_name": "硕士3年级", "web_name": "研究生3年级", "name_index": master3_dict, "is_wri": False},
              {"data_name": "硕士2年级", "web_name": "研究生2年级", "name_index": master2_dict, "is_wri": False},
              {"data_name": "硕士1年级", "web_name": "研究生1年级", "name_index": master1_dict, "is_wri": False}]
    graduated = [{"data_name": "已毕业学生", "web_name": "2022年已毕业学生",
                  "name_index": graduated2022_dict, "is_wri": False},
                 {"data_name": "已毕业学生", "web_name": "2021年已毕业学生",
                  "name_index": graduated2021_dict, "is_wri": False},
                  {"data_name": "已毕业学生", "web_name": "2020年已毕业学生",
                  "name_index": graduated2020_dict, "is_wri": False},
                 {"data_name": "已毕业学生", "web_name": "2019年已毕业学生",
                  "name_index": graduated2019_dict, "is_wri": False},
                 {"data_name": "已毕业学生", "web_name": "2018年已毕业学生",
                  "name_index": graduated2018_dict, "is_wri": False},
                  {"data_name": "已毕业学生", "web_name": "2017年已毕业学生",
                  "name_index": graduated2017_dict, "is_wri": False},
                 {"data_name": "已毕业学生", "web_name": "2016年之前已毕业学生",
                  "name_index": graduated2016_dict, "is_wri": False}]
    head_dir = 'old_docs'
    if teacher:
        general(data_name="老师", web_name="教师", name_index=teach_dict, output_filename='../%s/teachers.html' % head_dir)
    if phd:
        # general(data_name="博士生", name_index=phd_dict, output_filename='../docs/phds.html')
        deal_many_part(phd_and_postdoc, output_filename='../%s/phds.html' % head_dir)
    if ungrad:
        general(data_name="本科生", web_name="本科生", name_index=undergraduated_dict,
                output_filename='../%s/undergraduates.html' % head_dir)
    if domaster:
        deal_many_part(master, output_filename='../%s/masters.html' % head_dir)
    if graded:
        deal_many_part(graduated, output_filename='../%s/graduated.html' % head_dir)


if __name__ == '__main__':
    # run(teacher=1, phd=1, ungrad=1, domaster=1, graded=1)
    run(teacher=1, phd=1, ungrad=1, domaster=1, graded=1)

