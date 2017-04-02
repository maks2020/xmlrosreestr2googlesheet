# import html.parser
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

if __name__ == '__main__':
    html = open('test.html').read()
    result = json.loads(parser_html(html, 'user37344'))
    with open('client_secret_.json', 'w') as output_file:
        json.dump(result, output_file)





