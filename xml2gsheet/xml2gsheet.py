import os

from sheetapi import add_row_sheet
from parse_xml import parse_xml_attr, parse_xml_tag
from srch_cad_num import srch_same

def xml2gsheet(path_files):

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

if __name__ == '__main__':
    pf = ('/Users/mas/Desktop/projects/'
        'andrey_korovin/xml_in_gsheet/'
        'static/')
    xml2gsheet(pf)
