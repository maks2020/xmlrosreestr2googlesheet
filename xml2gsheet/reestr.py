from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory
from time import sleep
import os

from srch_utils import srch_cad_num
from gbot import gbot
from sheetapi import create_file, add_row_sheet
from gui_utils import login_gui, email_usr_gui
from parse_xml import parse_xml_attr, parse_xml_tag
from srch_utils import srch_same



def gui_rstr():

    data_app = {}
    data_app['work_dir'] = ''
    data_app['url_gsheet'] = ''

    def inf(cad_num):
        showinfo(title='Результат поиска кадастрового номера',
                message=srch_cad_num(cad_num))

    def dir_start():
        data_app['work_dir'] = askdirectory(title='Выбирете директорию')
        sleep(1)
        var.set('dir = %s' % data_app['work_dir'])
        root.update_idletasks()


    root = Tk()

    frame = Frame(root, bd=5)
    frame.pack(side=TOP, fill=X)
    Label(frame, text='Введите кадастровый номер', font='arial 12').pack(side=LEFT)
    frame1 = Frame(root, height=1, bd=5)
    frame1.pack(side=TOP, fill=X)
    frame1_1 = Frame(frame1, bd=5)
    frame1_1.pack(side=LEFT)
    in_cad_num = Entry(frame1_1, width=50, font='arial 12')
    in_cad_num.pack(side=LEFT)
    button1 = Button(frame1, width=30, text='Запросить информацию',font='arial 12',
                    command=(lambda: inf(in_cad_num.get())))
    button1.pack(side=RIGHT, fill=X)
    frame2 = Frame(root, bd=5)
    frame2.pack(side=TOP, fill=X)
    var = StringVar()
    var.set('Выберете директорию c XML файлами ==>')
    Label(frame2, textvariable = var, font='arial 12').pack(side=LEFT)
    button2 = Button(frame2, width=30, text='Выбрать',
                    font='arial 12', command=(lambda: dir_start())) # for Windows add initialdir='c:\\'
    button2.pack(side=RIGHT)


    # frame3 = Frame(root, bd=5)
    # frame3.pack(side=TOP, fill=X)
    #
    # Label(frame3, text='Вставьте URL Google sheet (необязательный параметр)', font='arial 12').pack(side=LEFT)
    #
    #
    frame4 = Frame(root, bd=5)
    frame4.pack(side=TOP, fill=X)

    # frame4_1 = Frame(frame4, bd=5)
    # frame4_1.pack(side=RIGHT)
    #
    # in_url = Entry(frame4_1, width=50, font='arial 12')
    # in_url.pack(side=LEFT)

    # data_app['url_gsheet'] = in_url.get()

    # frame4_12 = Frame(frame4_1, bd=5)
    # frame4_12.pack(side=TOP, fill=X)

    button_add_data = Button(frame4, width=30, text='Ввести данные',
                        font='arial 12', command=(lambda: root.destroy()))
    button_add_data.pack(side=RIGHT)

    root.title('Reestr')

    root.mainloop()

    return data_app


def if_not_exist():
    files_static = os.listdir('../static')
    if 'project.json' not in files_static:
        login, passwd = login_gui()
        gbot(login, passwd)
    if 'reestr_config.json' not in files_static:
        create_file(email_usr_gui())
    return None


def func_main(dict_data):
    path_files = dict_data['work_dir']
    if_not_exist()
    files_list = os.listdir(path_files)
    if len(files_list) != 0:
        rows_val = []
        for file in files_list:
            if file[-3:] == 'xml':
                path_file = path_files + '/' + file
                parse_xml = parse_xml_attr(path_file) + parse_xml_tag(path_file)
                rows_val.append(parse_xml)

        add_row_sheet(srch_same(rows_val))


if __name__ == '__main__':
    while True:
        data_app = gui_rstr()
        func_main(data_app)
