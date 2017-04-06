import os
import sys
import time
import random
import shutil

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Own module
from parser_html import parser_nm_prj

def driver_init():
    PATH_GECKODRIVER = '../static/chromedriver'
    driver = webdriver.Chrome(PATH_GECKODRIVER)
    return driver


def field_in(By_SEL, sel_str, str_in, driver):

    time.sleep(3)
    wait = WebDriverWait(driver, 10)
    obj_act = wait.until(
    EC.presence_of_element_located((By_SEL, sel_str)))
    obj_act.clear()
    time.sleep(1)
    obj_act.send_keys(str_in)


def but_rad_click(By_SEL, sel_str, driver):
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    but = wait.until(EC.element_to_be_clickable((By_SEL, sel_str)))
    but.click()


def but_submit(By_SEL, sel_str, driver):
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    but = wait.until(EC.element_to_be_clickable((By_SEL, sel_str)))
    but.submit()


def gbot(login_str, pswd_str):
    driver = driver_init()
    int_rndm = random.randrange(10000, 99999)
    # prj_name = 'project%s' % int_rndm

    # Get page create project
    url = 'https://console.developers.google.com/projectselector/apis/credentials?hl=RU'
    # uncomment url and inter name project if need create key in exist project
    url = 'https://console.developers.google.com/apis/credentials/serviceaccountkey?project=project88490'
    driver.get(url)

    # Login in account
    try:
        if 'Email' in driver.page_source:
            field_in(By.ID, 'Email', login_str, driver)
            but_rad_click(By.ID, 'next', driver)
        field_in(By.ID, 'Passwd', pswd_str, driver)
        but_rad_click(By.ID, 'signIn', driver)
    except:
        driver.quit()

    # Begin commment if need create key in exist project
    #=============================
    # Create name project
    # but_rad_click(By.LINK_TEXT, 'Создать проект', driver)
    # field_in(By.NAME, 'name', prj_name, driver)
    # xpath_crt_prj = '//*[@id="p6n-project-creation-dialog-ok-button"]'
    # but_rad_click(By.XPATH, xpath_crt_prj, driver)
    #
    # # Choice kind of account
    # time.sleep(10)
    # xpath_chc_knd_accnt = ('/html/body/div[2]/div[2]/div[3]/'
    #                    'div[1]/div/md-content/div/div[2]/'
    #                    'div/div[3]/div[2]/div/div')
    # but_rad_click(By.XPATH, xpath_chc_knd_accnt, driver)
    # xpath_knd_accnt = ('/html/body/div[2]/div[2]/div[3]/'
    #                        'div[1]/div/md-content/div/div[2]/'
    #                        'div/div[3]/div[2]/div/div/div/section[1]/'
    #                        'div/div/div[1]/div[3]')
    # but_rad_click(By.XPATH, xpath_knd_accnt, driver)
    # # End comment
    #=====================================

    prj_name = 'project88490'

    #get new service account
    time.sleep(10)
    xpath_chc_srv_knd_accnt = ('/html/body/div[2]/div[2]/div[3]/div[1]/'
                               'div/md-content/div/div[2]/div/form/ng-form/'
                               'div/label/div/jfk-select/div')
    but_rad_click(By.XPATH, xpath_chc_srv_knd_accnt, driver)

    time.sleep(5)

    # Menu item new service account
    css_path_nw_srv_accnt = ('div.goog-menuitem > '
                                'div.goog-menuitem-content > '
                                'jfk-menu-item[jfk-model-value='
                                '"ctrl.newServiceAccount"]')
    but_rad_click(By.CSS_SELECTOR, css_path_nw_srv_accnt, driver)

    time.sleep(2)
    xpath_nm_srv_accnt = ('/html/body/div[2]/div[2]/div[3]/div[1]/div/'
                          'md-content/div/div[2]/div/form/div[1]/div/'
                          'div[1]/ng-form/div/label/div[1]/input')
    nm_srv_accnt = '%s_%s' % ('%s_%s' % (login_str, int_rndm), prj_name)
    field_in(By.XPATH, xpath_nm_srv_accnt, nm_srv_accnt, driver)

    time.sleep(5)

    # Button choice kind of role
    xpath_chc_kid_rl = ('/html/body/div[2]/div[2]/div[3]/div[1]/div/'
                        'md-content/div/div[2]/div/form/div[1]/div/div[2]/'
                        'iam-role-picker/span/span/span/div')
    but_rad_click(By.XPATH, xpath_chc_kid_rl, driver)

    time.sleep(1)
    # Select menu project
    xpath_wrtr_prj = ('/html/body/div[2]/div[2]/'
                      'div[3]/div[1]/div/md-content/'
                      'div/div[2]/div/form/div[1]/div/'
                      'div[2]/iam-role-picker/span/span/'
                      'span/div/div[1]/section[2]/div/div/div[1]/div[1]')
    but_rad_click(By.XPATH, xpath_wrtr_prj, driver)

    time.sleep(1)
    # Select role menu writer
    xpath_wrtr_rl = ('/html/body/div[2]/div[2]/div[3]/'
                     'div[1]/div/md-content/div/div[2]/'
                     'div/form/div[1]/div/div[2]/'
                     'iam-role-picker/span/span/span/'
                     'div/div[2]/section/div/div/div[1]/div[2]')
    but_rad_click(By.XPATH, xpath_wrtr_rl, driver)

    # Download private key
    time.sleep(2)
    xpath_sv_rl = ('/html/body/div[2]/div[2]/div[3]/div[1]/div/'
                   'md-content/div/div[2]/div/form/div[3]/div/button[1]')

    but_rad_click(By.XPATH, xpath_sv_rl, driver)

    time.sleep(5)
    #Parsing name file key
    nm_fl = parser_nm_prj(driver.page_source)

    # # Include Sheet API
    time.sleep(3)

    url_shapi = ('https://console.developers.google.com/'
               'apis/api/sheets.googleapis.com/'
               'overview?project=%s&hl=RU&duration=PT1H' % prj_name)

    driver.get(url_shapi)
    time.sleep(5)

    xpath_but_shtap = ('//*[@id="p6n-action-bar-container-main"]/'
                       'div[1]/div/div[2]/div[3]/pan-action-bar-button[1]/'
                       'button/pan-icon')
    try:
        but_rad_click(By.XPATH, xpath_but_shtap, driver)
    except:
        pass
    time.sleep(3)

    # Include Drive API

    url_drv_api = ('https://console.developers.google.com/apis/'
                   'api/drive.googleapis.com/'
                   'overview?project=%s' % prj_name)
    driver.get(url_drv_api)
    time.sleep(5)

    xpath_but_drv_api = ('//*[@id="p6n-action-bar-container-main"]/'
                     'div[1]/div/div[2]/div[3]/pan-action-bar-button[1]/'
                     'button/pan-icon')
    try:
        but_rad_click(By.XPATH, xpath_but_drv_api, driver)
    except:
        pass
    time.sleep(3)

    # Close browser and shutdown driver
    driver.quit()
    # Copy keys from folder Downloads in folder 'static' of project
    try:
        copy_key(nm_fl)
        result = 1
    except:
        result = None
    return result


def copy_key(name_file):
    if sys.platform == 'darwin' or sys.platform == 'linux':
        src = os.environ['HOME'] + '/Downloads/%s' % name_file
        dist = '../static/project.json'
        shutil.copy2(src, dist)
    elif sys.platform == 'win32':
        src = os.environ['HOMEPATH'] + '\\Downloads\\%s' % name_file
        dist = '..\\static\\project.json'
        shutil.copy2(src, dist)
    return None

if __name__ == '__main__':
    import getpass
    login = input('Input login: ')
    passwd = getpass.getpass('Input passwd: ')
    gbot(login, passwd)