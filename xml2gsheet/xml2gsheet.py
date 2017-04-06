import os

from gbot import gbot
from sheetapi import create_file, add_row_sheet
from gui_utils import login_gui, email_usr_gui
from parse_xml import parse_xml_attr, parse_xml_tag
from srch_utils import srch_same


def if_not_exist():
    files_static = os.listdir('static')
    if 'project.json' not in files_static:
        login, passwd = login_gui()
        gbot(login, passwd)
    if 'reestr_config.json' not in files_static:
        create_file(email_usr_gui())
    return None


def func_main(dict_data):
    path_files = dict_data['work_dir']
    if_not_exist()
    files_list = os.listdir(path_files)
    if len(files_list) != 0:
        rows_val = []
        for file in files_list: 
            if file[-3:] == 'xml':
                path_file = path_files + '/' + file
                parse_xml = parse_xml_attr(path_file) + parse_xml_tag(path_file)
                rows_val.append(parse_xml)

        add_row_sheet(srch_same(rows_val))

    return None
