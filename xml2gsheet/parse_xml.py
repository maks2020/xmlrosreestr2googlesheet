import xml.etree.ElementTree as ET
from datetime import datetime
import re

def parse_xml_attr(file):
    tree = ET.parse(file)
    root = tree.getroot()
    str_cad_num = 'CadastralNumber'
    date_create = 'DateCreated'
    def rec(root_item, str_search):
        res_func = ''
        for child in root_item:
            if str_search in child.attrib:
                res_func = child.attrib[str_search]
            else:
                if rec(child, str_search) != '':
                    res_func = (rec(child, str_search))
    return [rec(root, str_cad_num),
            rec(root, date_create)]

def parse_xml_tag(file):
    tree = ET.parse(file)
    root = tree.getroot()
    str_cad_cost = 'CadastralCost'
    cad_cost_val = 'Value'
    def rec(root_item, str_tag, str_attrib):
        res_func = ''
        for child in root_item:
            if re.search(str_tag, child.tag):
                res_func = child.attrib[str_attrib]
            else:
                if rec(child, str_tag, str_attrib) != '':
                    res_func = (rec(child, str_tag, str_attrib))
        return res_func
    now = datetime.now()
    date_create_row = '%d-%d-%d / %d:%d' % (now.day, now.month, now.year,
                                            now.hour, now.minute)
    return [rec(root, str_cad_cost, cad_cost_val),
            date_create_row]


if __name__=='__main__':

    file_xml = '../static/kp_c77cb5e8-da19-43f7-8f0e-07e9f668d6ad.xml'

    print(parse_xml_attr(file_xml))
