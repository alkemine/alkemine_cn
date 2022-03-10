#   coding: utf-8
#   This file is part of potentialmind.

#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/25"

import os
from temple_auto_people import write_post
from collections import defaultdict
from string import Template


def get_temple(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        people_temple = f.read()
    return Template(people_temple)


def get_all_paper(main_content):
    __paper_temple_fn = os.path.join(os.path.dirname(__file__), 'temples', 'tmp_publication')
    config = get_temple(__paper_temple_fn)
    variables = {"main_content": main_content}

    _input = config.safe_substitute(**variables) + '\n'
    # write_post('test.html', _input, 'w')
    return _input


def get_each_year_paper(year, content):
    __paper_temple_fn = os.path.join(os.path.dirname(__file__), 'temples', 'tmp_each_year_paper')
    config = get_temple(__paper_temple_fn)
    variables = {"year": year,
                 "papers": content}

    _input = config.safe_substitute(**variables) + '\n'
    return _input


def get_one_paper(cite_contene, href, pdf_path="#"):
    __paper_temple_fn = os.path.join(os.path.dirname(__file__), 'temples', 'tmp_each_paper')
    config = get_temple(__paper_temple_fn)
    variables = {"cite_contene": cite_contene,
                 "href": href,
                 "doi": href,
                 "local_pdf_path": pdf_path}

    _input = config.safe_substitute(**variables) + '\n'
    return _input


def read_data():
    import pandas as pd
    # try:
    #     a = pd.read_csv('copy.csv')
    # except UnicodeDecodeError as e:
    #     print(e)
    #     print("Use notepad++ convert encoding to UTF8-BOM")
    #     exit()
    
    # import xlrd
    # a = xlrd.open_workbook('copy.xlsx')
    # a = a.sheet_by_index(0)
    # print(a.nrows)
    a = pd.read_excel('copy_allpapers_from_tencentexcel.xlsx')
    # print(a.head())
    # print([print(i) for i in a.iterrows()])
    # exit()
    
    format_str = '%s, %s, %s. %s (%s).'
    lll = defaultdict(list)
    # __pdf_path = os.path.join('\\'.join(os.getcwd().split('\\')[:-1]), 'docs', 'publications', pdf_name)
    __pdf_path = os.path.join('\\'.join(os.getcwd().split('\\')[:-1]), 'docs', 'publications')

    all_files = os.listdir(__pdf_path)
    tmp_ddd = []
    for i in a.iterrows():
        tmp_i = i[1]
        year = str(tmp_i['年份']).strip()
        all_authors = ', '.join(str(tmp_i['所有作者（以英文逗号隔开）']).strip().split(','))
        title = ' '.join(str(tmp_i['题目']).strip().split('_'))
        pdf_name = str(tmp_i['pdf全称（pdf中空格替换为英文下划线_）']).strip()
        pdf_name = pdf_name + '.pdf' if not str(pdf_name).endswith('.pdf') else pdf_name
        if ADDED:
            pdf_path = 'publications/%s' % pdf_name
        else:
            pdf_path = 'login/login.html'
        
        if not (pdf_name in all_files):
            print("can't find:", pdf_name)
        else:
            if pdf_name in tmp_ddd:
                print(pdf_name)
            # else:
            #     os.remove(os.path.join(__pdf_path, pdf_name))
            tmp_ddd.append(pdf_name)
            
        vnp = []
        if str(tmp_i['volume，没有填-']).strip() != '-' and str(tmp_i['volume，没有填-']).strip() != '_':
            vnp.append(str(tmp_i['volume，没有填-']).strip()),
        if str(tmp_i['number，没有填-']).strip() != '-' and str(tmp_i['number，没有填-']).strip() != '_':
            vnp.append(str(tmp_i['number，没有填-']).strip())
        if str(tmp_i['页码']).strip() != '-' and str(tmp_i['页码']).strip() != '_':
            vnp.append(str(tmp_i['页码']).strip())

        ttt = format_str % (all_authors,
                            title,
                            str(tmp_i['期刊']).strip(),
                            ','.join(vnp),
                            year)
        lll[year].append((ttt, str(tmp_i['原文链接']).strip(), pdf_path))

    return lll


def run():
    content = read_data()
    final = []
    import datetime
    num = datetime.datetime.now().year
    for i in range(num, 1997, -1):
        # if i==2020:
        #     content['2020'] = [('loading', '......')]

        each_pp = content[str(i)]
        tmmm = []
        for ee in range(len(each_pp)-1, -1, -1):
            tmmm.append(get_one_paper(*each_pp[ee]))
        tmpcontent = '\n'.join(tmmm)
        # print(tmpcontent)
        final.append(get_each_year_paper(i, tmpcontent))

    wri = get_all_paper('\n'.join(final))
    a = '\\'.join(os.getcwd().split('\\')[:-1])
    final_path = os.path.join(a, 'docs', 'publications_cite.html')
    write_post(final_path, wri, 'w')


if __name__ == '__main__':
    # 是否添加pdf附件
    ADDED = False
    run()
