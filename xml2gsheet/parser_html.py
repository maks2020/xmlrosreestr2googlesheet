import json

from bs4 import BeautifulSoup

def parser_html(html_src, user_name):
    soup = BeautifulSoup(html_src, 'html.parser')
    td_values = soup.select('td.p6n-api-credential-table-actions > a')
    td_users = soup.select('td.p6n-api-credential-table-label > a')
    result = ''
    for val, td_user in zip(td_values,td_users):
        temp_td_user = td_user.get_text().strip()
        if user_name == temp_td_user:
            result = val.get('content')
    return result

def parser_nm_prj(html_src):
    soup = BeautifulSoup(html_src, 'html.parser')
    return soup.select('#dialogContent_2 > div > section > p > span')[0].get_text().strip()







