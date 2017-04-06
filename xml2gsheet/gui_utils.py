from tkinter import *

def login_gui():

    result = []

    def login_data(login, passwd, cred_list, root):
        cred_list.append(login)
        cred_list.append(passwd)
        root.destroy()

    root = Tk()
    frame = Frame(root, bd=5)
    frame.pack(side=TOP)
    frame1 = Frame(frame, bd=5)
    frame1.pack(side=LEFT, fill=X)

    frame1_1 = Frame(frame1, bd=5)
    frame1_1.pack(side=TOP)

    Label(frame1_1, text='Введите логин Google', font='arial 12').pack(side=LEFT)

    frame1_2 = Frame(frame1, bd=5)
    frame1_2.pack(side=TOP)

    Label(frame1_2, text='Введите пароль Google', font='arial 12').pack(side=LEFT)

    frame1_3 = Frame(frame1, bd=5)
    frame1_3.pack(side=TOP)

    Label(frame1_3, text=' ', font='arial 12').pack(side=LEFT)

    frame2 = Frame(frame, bd=5)
    frame2.pack(side=RIGHT, fill=X)

    frame2_1 = Frame(frame2, bd=5)
    frame2_1.pack(side=TOP)

    input_login = Entry(frame2_1, width=50, font='arial 12')
    input_login.pack(side=LEFT)

    frame2_2 = Frame(frame2, bd=5)
    frame2_2.pack(side=TOP)

    input_passwd = Entry(frame2_2, show='*', width=50, font='arial 12')
    input_passwd.pack(side=LEFT)

    frame2_3 = Frame(frame2, bd=5)
    frame2_3.pack(side=TOP)

    button_login = Button(frame2_3, width=30, text='Вход',font='arial 12',
                    command=(lambda: login_data(input_login.get(), input_passwd.get(), result, root)))
    button_login.pack(side=LEFT)

    root.title('Reestr - login')

    root.mainloop()

    return tuple(result)



def email_usr_gui():

    result = []

    def email_data(email_usr, list_email, root):
        list_email.append(email_usr)
        root.destroy()


    root = Tk()
    frame = Frame(root, bd=5)
    frame.pack(side=TOP)
    frame1 = Frame(frame, bd=5)
    frame1.pack(side=LEFT, fill=X)

    frame1_1 = Frame(frame1, bd=5)
    frame1_1.pack(side=TOP)

    Label(frame1_1, text='Еmail пользователя для доступа', font='arial 12').pack(side=TOP)

    frame2_1 = Frame(frame1, bd=5)
    frame2_1.pack(side=TOP)

    Label(frame1_1, text=' ', font='arial 12').pack(side=TOP)

    frame2 = Frame(frame, bd=5)
    frame2.pack(side=RIGHT, fill=X)

    frame2_1 = Frame(frame2, bd=5)
    frame2_1.pack(side=TOP)

    input_email = Entry(frame2_1, width=50, font='arial 12')
    input_email.pack(side=LEFT)

    frame2_2 = Frame(frame2, bd=5)
    frame2_2.pack(side=TOP)

    button_login = Button(frame2_2, width=30, text='Вход', font='arial 12',
                    command=(lambda: email_data(input_email.get(), result, root)))
    button_login.pack(side=LEFT)

    root.title('Reestr - email')

    root.mainloop()

    return result[0]
