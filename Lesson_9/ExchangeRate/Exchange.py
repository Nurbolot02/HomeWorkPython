import datetime
import tkinter as tk
import requests
EXtext = ''
startEX = 0



# KGS =data['Valute']['KGS']
# row = 0
# col = 0

def getEntry(f = False,):
    try:
        value = name.get()
    except:
        value = '1'
        print("Empty")
    if value.isdigit():
        return int(value)
    else:
        return 1

def get_value(f = False, RUB = 1):
    global row, col, EXtext, Last_RUB, startEX
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    date_vlue = data['Valute']

    RUB = getEntry()
    EXtext = ''
    Curse = ['KGS', 'KZT', 'USD', 'EUR', 'TRY', 'CNY']
    for i in date_vlue.items():
        # print(i[1]['Name'], i[1]['Nominal'] / i[1]['Value'])
        # print(float('{0:.3f}'.format(i[1]['Nominal'] / i[1]['Value'])))
        if i[0] == Curse[0] or i[0] == Curse[1] or i[0] == Curse[2] or i[0] == Curse[3] or i[0] == Curse[4] or i[
            0] == Curse[5]:
            EXtext += f"{RUB} - RUB == {float('{0:.3f}'.format(RUB * (i[1]['Nominal'] / i[1]['Value'])))} - {i[0]} \n"
    if startEX > 0:
        label_2['text'] = EXtext
    startEX +=1


win = tk.Tk()
label_1 = tk.Label(win, text='Hello!',
                   font=('Arial', 15, 'bold'),
                   fg= 'white',
                   background='#000',
                   padx=20,
                   pady=20,
                   width=50,
                   anchor='s')
label_1.pack()
get_value()
label_2 = tk.Label(win, text=EXtext,
                       font=('Arial', 15, 'bold'),
                       fg='white',
                       background='#000',
                       padx=2,
                       pady=2,
                       anchor='s')
label_2.pack()

btn1 = tk.Button(win, text='Convert',
                 activebackground='green',
                 command=get_value
                 )
photo_path = 'img/ExC.png'
photo = tk.PhotoImage(file= photo_path)
win.iconphoto(False,photo)
h = 300
w = 1000
#win.resizable(False,False)
win.geometry(f'{w}x{h}')
win.config(background='#000')
win.title('Конвертер валют')

name = tk.Entry(win)
name.pack()
btn1.pack()

win.mainloop()



