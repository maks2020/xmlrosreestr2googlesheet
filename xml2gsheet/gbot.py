import time
import random
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Own modile
from parser_html import parser_html


def field_in(By_SEL, sel_str, str_in):
    time.sleep(3)
    wait = WebDriverWait(driver, 10)
    obj_act = wait.until(
    EC.presence_of_element_located((By_SEL, sel_str)))
    obj_act.clear()
    time.sleep(1)
    obj_act.send_keys(str_in)


def but_rad_click(By_SEL, sel_str)  :
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    but = wait.until(EC.element_to_be_clickable((By_SEL, sel_str)))
    but.click()


def but_submit(By_SEL, sel_str):
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    but = wait.until(EC.element_to_be_clickable((By_SEL, sel_str)))
    but.submit()
def gbot(login_str, pswd_str):
    # Data for work
    PATH_GECKODRIVER = '../static/chromedriver'
    driver = webdriver.Chrome(PATH_GECKODRIVER)
    # login_str = 'you_login'
    # pswd_str = 'you_psswd'
    int_rndm = random.randrange(10000, 99999)
    prj_name = 'project%s' % int_rndm

    # Get page create project
    url = 'https://console.developers.google.com/projectselector/apis/credentials?hl=RU'
    driver.get(url)

    # Login in account
    if 'Email' in driver.page_source:
        field_in(By.ID, 'Email', login_str)
        but_rad_click(By.ID, 'next')
    field_in(By.ID, 'Passwd', pswd_str)
    but_rad_click(By.ID, 'signIn')

    # Create name project
    but_rad_click(By.LINK_TEXT, 'Создать проект')
    field_in(By.NAME, 'name', prj_name)
    xpath_crt_prj = '//*[@id="p6n-project-creation-dialog-ok-button"]'
    but_rad_click(By.XPATH, xpath_crt_prj)

    # Choice kind of account
    time.sleep(10)
    xpath_chc_knd_accnt = ('/html/body/div[2]/div[2]/div[3]/'
                       'div[1]/div/md-content/div/div[2]/'
                       'div/div[3]/div[2]/div/div')
    but_rad_click(By.XPATH, xpath_chc_knd_accnt)
    xpath_knd_accnt = ('/html/body/div[2]/div[2]/div[3]/'
                       'div[1]/div/md-content/div/div[2]/'
                       'div/div[3]/div[2]/div/div/div/'
                       'section[1]/div/div/div[1]/div[2]')
    but_rad_click(By.XPATH, xpath_knd_accnt)

    # Config display confirmation project
    xpath_dspl_prj = ('/html/body/div[2]/div[2]/div[3]/div[1]/'
                      'div/md-content/div/div[2]/div/div[2]/'
                      'pan-message/div/div[2]/jfk-button')
    but_rad_click(By.XPATH, xpath_dspl_prj)
    # Input name project
    time.sleep(10)
    product_name = 'product_%s' % prj_name
    # xpath_fld_nm_prj = ('//*[@id="p6n-consent-product-name"]')
    field_in(By.ID, 'p6n-consent-product-name', product_name)
    xpath_sv_dspl_prj = ('//*[@id="api-consent-save"]')
    but_rad_click(By.XPATH, xpath_sv_dspl_prj)

    # Choice kind of project
    time.sleep(5)
    xpath_knd_prj = ('/html/body/div[2]/div[2]/div[3]/div[1]/'
                     'div/md-content/div/div[2]/div/form/'
                     'fieldset/div/div/label[6]')
    but_rad_click(By.XPATH, xpath_knd_prj)

    # Input user name
    xpath_usr_nm = ('/html/body/div[2]/div[2]/'
                    'div[3]/div[1]/div/md-content/'
                    'div/div[2]/div/form/oauth-client-editor/'
                    'ng-form/div/label/div[1]/input')
    usr_nm = 'user%d' % int_rndm
    field_in(By.XPATH, xpath_usr_nm, usr_nm)
    xpath_cnfrm_usr_nm = ('/html/body/div[2]/div[2]/div[3]/'
                          'div[1]/div/md-content/div/div[2]/'
                          'div/form/div/div/button')
    but_submit(By.XPATH, xpath_cnfrm_usr_nm)

    # Get client secret data
    time.sleep(5)
    xpath_but_ok_mod_win = ('/html/body/div[6]/md-dialog/'
                            'md-dialog/md-dialog-actions/'
                            'pan-modal-actions/pan-modal-action/a')
    but_rad_click(By.XPATH, xpath_but_ok_mod_win)
    time.sleep(5)
    html_src = driver.page_source

    result = json.loads(parser_html(html_src, usr_nm))

    # Result put in file client_secret.json
    with open('client_secret.json', 'w') as output_file:
        json.dump(result, output_file)


    # Set SheetsAPI
    time.sleep(3)

    # prj_name = 'project12953'

    url_api = ('https://console.developers.google.com/'
               'apis/api/sheets.googleapis.com/'
               'overview?project=%s&hl=RU&duration=PT1H' % prj_name)

    driver.get(url_api)
    time.sleep(4)
    xpath_but_shtap = ('//*[@id="p6n-action-bar-container-main"]/'
                       'div[1]/div/div[2]/div[3]/pan-action-bar-button[1]/'
                       'button/pan-icon')
    but_rad_click(By.XPATH, xpath_but_shtap)
    return None

if __name__ == '__main__':
    gbot('your_login', 'your_psswd')