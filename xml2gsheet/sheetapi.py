import json

import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


def autoz():
    CREDENTIALS_FILE = '../static/project.json'  # имя файла с закрытым ключом
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http=httpAuth)

    return service, httpAuth


def drive_service(email_user, spreadsheet_dic):
    service, httpAuth = autoz()
    driveService = discovery.build('drive', 'v3', http=httpAuth)
    shareRes = driveService.permissions().create(
        fileId=spreadsheet_dic['spreadsheetId'],
        body={'type': 'user', 'role': 'writer', 'emailAddress': email_user},  # доступ на чтение кому угодно
        fields='id'
    ).execute()


def create_file(email_user):
    service, httpAuth = autoz()
    sheet_list = 'Лист1'
    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': 'Reestr', 'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': sheet_list,
                                   'gridProperties': {'rowCount': 999, 'columnCount': 4}}}]
    }).execute()

    drive_service(email_user, spreadsheet)

    values = [
        [
            'Кадастровый номер',
            'Дата кадастра',
            'Кадастровая стоимость',
            'Дата реестра'
        ]
    ]

    body = {
      'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet['spreadsheetId'], valueInputOption = 'RAW', range=sheet_list,
        body=body).execute()
    with open('../static/reestr_config.json', 'w') as output_file:
        json.dump(spreadsheet, output_file)


def read_config():
    with open('../static/reestr_config.json') as input_file:
        spreadsheet = json.load(input_file)
    return spreadsheet


def get_values_sheet():

    spreadsheet = read_config()

    service, dummy = autoz()

    spreadsheetId = spreadsheet['spreadsheetId']

    rangeName = 'Лист1!A1:D'

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        result = None
    else:
        result = values
    return result


def add_row_sheet(values):

    spreadsheet = read_config()

    spreadsheetId = spreadsheet['spreadsheetId']

    service, dummy = autoz()

    rangeName = 'Лист1'

    body = {
      'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId, valueInputOption = 'RAW', range=rangeName,
        body=body).execute()

    return result


if __name__ == '__main__':

    create_file('kroti1972@gmail.com')