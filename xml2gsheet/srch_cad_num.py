from sheetapi import get_values_sheet


def srch_cad_num(srch_num):
    values = get_values_sheet()
    for row in values:
        if srch_num in row:
            res = ('Кадастровый номер: %s\nВремя записи в кадастр: %s\n'
                    'Кадастровая стоимость: %s\nВремя записи в реестр: %s'
                     % (row[0], row[1], row[2], row[3]))
    return res

