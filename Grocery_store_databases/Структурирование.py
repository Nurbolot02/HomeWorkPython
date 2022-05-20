import tkinter as tk
from tkinter import *
from tkinter import messagebox


def add_item(title = 'Ввести'):

    def done(id, name, pd):

        items[id] = {'name': name, 'PD': pd}
        main_window.deiconify()
        add_window.destroy()

    main_window.withdraw()
    add_window = tk.Tk()
    add_window.geometry('300x180')
    add_window.resizable(False, False)
    add_window.title('Add Window')

    #  Add text

    id_lbl = Label(add_window, text='Введите ID')
    name_lbl = Label(add_window, text='Введите название')
    pd_lbl = Label(add_window, text='Введите дату производства')

    id_lbl.place(relx=0.03, rely=0.3)
    name_lbl.place(relx=0.03, rely=0.4)
    pd_lbl.place(relx=0.03, rely=0.5)

    # Add entrys

    id, name, pd = StringVar(), StringVar(), StringVar()

    id_entry = Entry(add_window, textvariable=id)
    name_entry = Entry(add_window, textvariable=name)
    pd_entry = Entry(add_window, textvariable=pd)

    id_entry.place(relx=0.55, rely=0.3)
    name_entry.place(relx=0.55, rely=0.4)
    pd_entry.place(relx=0.55, rely=0.5)

    # Add button done

    done_btn = Button(add_window, text='Add', command=lambda: done(int(id_entry.get()), name_entry.get(), pd_entry.get()))

    done_btn.place(relx=0.5, rely=0.8)

    add_window.mainloop()
def show_item():

    def show_action(key):

        global requested_lbl

        try:
            requested_lbl.destroy()
            requested_lbl = Label(text=items[key])
            requested_lbl.place(relx=0.3, rely=0.8)

        except NameError:

            try:
                requested_lbl = Label(text=items[key])
                requested_lbl.place(relx=0.3, rely=0.8)

            except KeyError:
                messagebox.showerror('Ошибка', 'ID не существует')

        except KeyError:
            messagebox.showerror('Ошибка', 'ID не существует')

    show_id = StringVar()

    show_btn = Button(main_window, text='Show', command= lambda: show_action(int(show_id.get())))
    show_lbl = Label(main_window, text="ID:")
    show_entry = Entry(main_window, textvariable=show_id)

    show_btn.place(relx=0.77, rely=0.67)
    show_lbl.place(relx=0.22, rely=0.7)
    show_entry.place(relx=0.3, rely=0.7)
def del_item():

    def del_action(key):

        try:
            del items[key]
        except KeyError:
            messagebox.showerror('Ошибка', 'ID не существует')


    show_id = StringVar()

    show_btn = Button(main_window, text='Del', command= lambda: del_action(int(show_id.get())))
    show_lbl = Label(main_window, text="ID:")
    show_entry = Entry(main_window, textvariable=show_id)

    show_btn.place(relx=0.77, rely=0.67)
    show_lbl.place(relx=0.22, rely=0.7)
    show_entry.place(relx=0.3, rely=0.7)


items = {
    1: {'name': 'Чипсы', 'PD': '22.04.2022'},
    2: {'name': 'Лепёшки', 'PD': '22.03.2022'}
}

w = 33

main_window = tk.Tk()
main_window.geometry('300x180')
main_window.resizable(True,True)
main_window.title('Main Window')

add_btn = tk.Button(
    main_window,
    text="Добавить элемент",
    width=w,
    command=add_item
)
add_btn.place(
    relx=0.1,
    rely=0.05
)

show_btn = tk.Button(
    main_window,
    text="Посмотреть элемент по ID",
    width=w,
    command=show_item
)
show_btn.place(
    relx=0.1,
    rely=0.25
)

del_btn = tk.Button(
    main_window,
    text="Удалить элемент по ID",
    width=w,
    command=del_item
)
del_btn.place(
    relx=0.1,
    rely=0.45
)

main_window.mainloop()