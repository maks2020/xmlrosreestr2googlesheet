import os
from datetime import datetime as dt
from sheetapi import add_row_sheet
from parse_xml import parse_xml_attr, parse_xml_tag

def xml2gsheet(path_files):
    today = dt.now()
    file_store = 'f_store.txt'
    # path_files = '../static'
    files_list = os.listdir(path_files)
    if len(files_list) != 0:
<<<<<<< HEAD
        #if file_store not in os.listdir('./'):
         #   with open(file_store, 'a') as storege_file:
          #      storege_file.write(('%d-%d-%d %d:%d'% (today.year, today.month, today.day, today.hour, today.minute)) + '\n')
        #with open(file_store, 'r') as storege_file:
        #    files_storege = storege_file.readlines()
        rows_val = []
        for file in files_list: 
            #if file not in files_storege:
            path_file = path_files + '/' + file
            parse_xml = parse_xml_attr(path_file) + parse_xml_tag(path_file)
            rows_val.append(parse_xml)
                #with open(file_store, 'a') as storege_file:
                #    storege_file.write(file + '\n')
            #else:
            #    continue
=======
        # if file_store not in os.listdir('./'):
        #     with open(file_store, 'a') as storege_file:
        #         storege_file.write(('%d-%d-%d %d:%d'% (today.year, today.month, today.day, today.hour, today.minute)) + '\n')
        # with open(file_store, 'r') as storege_file:
        #     files_storege = storege_file.readlines()
        rows_val = []
        for file in files_list: 
            # if file not in files_storege:
            if file[-3:] == 'xml':
                path_file = path_files + '/' + file
                parse_xml = parse_xml_attr(path_file) + parse_xml_tag(path_file)
                rows_val.append(parse_xml)
            #     with open(file_store, 'a') as storege_file:
            #         storege_file.write(file + '\n')
            # else:
            #     continue
>>>>>>> ccd20d1f2e9303465a120723133eabfa9884cbb5
        add_row_sheet(rows_val)
