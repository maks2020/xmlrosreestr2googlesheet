from datetime import datetime

from sheetapi import get_values_sheet


def srch_cad_num(srch_num):
    values = get_values_sheet()
    for row in values:
        if srch_num in row:
            res = ('Кадастровый номер: %s\nВремя записи в кадастр: %s\n'
                    'Кадастровая стоимость: %s\nВремя записи в реестр: %s'
                     % (row[0], row[1], row[2], row[3]))
    return res

def srch_same(list_file):
    now = datetime.now()
    with open('static/log.txt', 'a')  as output_file:
        output_file.write('Добавление %d-%d-%d / %d : 0%d\n' %
                          (now.day, now.month, now.year,
                            now.hour, now.minute))
    rows_gsheet = get_values_sheet()
    if rows_gsheet != None:
        temp_list = list_file[:]
        for row_new in temp_list:
            for row_gsheet in rows_gsheet:
                if row_new[0] in row_gsheet:
                    with open('static/log.txt', 'a')  as output_file:
                        output_file.write('%s - есть в реестре\n' % row_new[0])
                    list_file.remove(row_new)
    with open('static/log.txt', 'a')  as output_file:
        for row_new in list_file:
            output_file.write('%s - добавлено в реестр\n' % row_new[0])
    return list_file

