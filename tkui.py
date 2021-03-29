from tkinter import *
#from tkinter import messagebox

def check_temp():
    import requests, json
    api_key= "a444ed4e63d715547e69a7f70467cb04"
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    city_name= city_field.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    result = requests.get(complete_url)
    print(result)

    datafeed = result.json()
    print(datafeed)
    if datafeed['cod'] !='404':
        minfo = datafeed['main']
        current_temp = round((minfo['temp'] - 273.15),2)
        current_pressure = minfo['pressure']
        current_humid = minfo['humidity']

        temp_field.insert (15,str(current_temp)+ ' 摄氏度')
        atm_field.insert(10,str(current_pressure)+ ' 帕斯卡')
        humid_field.insert(15, str(current_humid) + " %")

    else :
        messagebox.showerror("Error","input is not valid try again")
        city_field.delete(0,END)

def clear_all():
    city_field.delete(0,END)
    temp_field.delete(0,END)
    atm_field.delete(0,END)
    humid_field.delete(0,END)

    city_field.focus_set()

if __name__ == '__main__':
    root = Tk()
    root.title('查询温度')
    root.configure(background = "white")
    root.geometry('1600x900')
    print(2)
    headlabel = Label(root, text = '温度测量程序 GUI版本',fg='black',
    bg='white')

    label_city= Label(root, text='城市名字', fg='black', bg = 'blue')
    label_temp= Label(root, text='温度', fg='black',bg='blue')
    label_pressure= Label(root, text='气压',fg='black',bg='blue')
    label_humid= Label(root, text='湿度',fg='black',bg='blue')


    headlabel.grid(row=0,column=1)
    label_city.grid(row=1,column=0,sticky='E')
    label_temp.grid(row=2,column=0,sticky='E')
    label_pressure.grid(row=3, column=0,sticky='E')
    label_humid.grid(row=4,column=0,sticky='E')


    city_field = Entry(root)
    temp_field = Entry(root)
    atm_field = Entry(root)
    humid_field = Entry(root)

    city_field.grid(row=1,column=1,ipadx="100")
    temp_field.grid(row=2,column=1,ipadx='100')
    atm_field.grid(row=3,column=1,ipadx='120')
    humid_field.grid(row=4,column=1,ipadx='120')

    search_butt = Button(root,text="提交", fg='black', bg='green',
    command = check_temp)

    clear_butt = Button(root,text='清除',fg='black', bg='green',
    command = clear_all)

    search_butt.grid(row=1,column=2)
    clear_butt.grid(row=6,column=1)
    print(1)
    root.mainloop()
