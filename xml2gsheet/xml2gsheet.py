import os
from datetime import datetime as dt
from gsheetapi import add_row
from gsheetapi import main

today = dt.now()
file_store = 'f_store.txt'
path_files = '../static'
files_list = os.listdir(path_files)
if len(files_list) != 0:
    if file_store not in os.listdir('./'):
        with open(file_store, 'a') as storege_file:
            storege_file.write(('%d-%d-%d %d:%d'% (today.year, today.month, today.day, today.hour, today.minute)) + '\n')
    #         for file in files_list:
    #             storege_file.write(file + '\n')
    with open(file_store, 'r') as storege_file:
        files_storege = storege_file.readlines()
    for file in files_list: 
        if file not in files_storege:
            path_file = path_files + '/' + file
            add_row(path_file)
            main()
            with open(file_store, 'a') as storege_file:
                storege_file.write(file + '\n')
        else:
            continue
