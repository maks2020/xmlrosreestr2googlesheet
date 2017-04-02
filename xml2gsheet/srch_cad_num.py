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
    rows_gsheet = get_values_sheet()
    temp_list = list_file[:]
    for row_new in temp_list:
        for row_gsheet in rows_gsheet:
            if row_new[0] in row_gsheet:
                list_file.remove(row_new)
    return list_file

