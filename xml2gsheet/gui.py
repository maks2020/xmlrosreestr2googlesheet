from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory
from time import sleep

from srch_cad_num import srch_cad_num
from xml2gsheet import xml2gsheet

def inf(cad_num):
    showinfo(title='Результат поиска кадастрового номера',
            message=srch_cad_num(cad_num))

def dir_start():
    data_app['work_dir'] = askdirectory(title='Выбирете директорию')
    sleep(1)
    var.set('dir = %s' % data_app['work_dir'])
    root.update_idletasks()

data_app = {}
data_app['work_dir'] = ''
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


frame3 = Frame(root, bd=5)
frame3.pack(side=TOP, fill=X)

Label(frame3, text='Вставьте URL Google sheet и подтвердите', font='arial 12').pack(side=LEFT)


frame4 = Frame(root, bd=5)
frame4.pack(side=TOP, fill=X)

frame4_1 = Frame(frame4, bd=5)
frame4_1.pack(side=LEFT)

in_url = Entry(frame4_1, width=50, font='arial 12')
in_url.pack(side=LEFT)

button_conf_url = Button(frame4, width=30, text='URL',
                            font='arial 12')
button_conf_url.pack(side=RIGHT)

frame5 = Frame(root, bd=5)
frame5.pack(side=TOP, fill=X)

button_add_data = Button(frame5, width=30, text='Добавить данные',
                font='arial 12', command=(lambda: xml2gsheet(data_app['work_dir'])))
button_add_data.pack(side=RIGHT)
root.title('Reestr')
root.mainloop()
