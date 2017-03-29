import xml.etree.ElementTree as ET
from datetime import datetime


def parse_xml(file):
    row_table = []
    values_row = []
    tree = ET.parse(file)
    root = tree.getroot()
    root_parcel = root.find('{urn://x-artefacts-rosreestr-ru/outgoing/kpzu/6.0.1}Parcel')
    cadastral_number = root_parcel.attrib['CadastralNumber']
    cadastral_cost = root_parcel.find('{urn://x-artefacts-rosreestr-ru/outgoing/kpzu/6.0.1}CadastralCost').attrib['Value']
    now = datetime.now()
    date_create_row = 'date: %d-%d-%d time: %d:%d' % (now.day, now.month, now.year,
                                                        now.hour, now.minute)
    values_row.append(cadastral_number)
    values_row.append(cadastral_cost)
    values_row.append(date_create_row)
    row_table.append(values_row)
    return row_table


