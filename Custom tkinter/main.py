import customtkinter as ctk
import pars
import datetime
from PIL import Image


# Главное окно
window=ctk.CTk()
window.title('Customtkinter')
window.geometry("600x550") # Размер окна
window.maxsize(width=680,height=520) # Размер окна максимальный предел
window.minsize(width=680,height=520) # Размер окна минимальный предел
window.resizable(width=False,height=False)

# Тема экрана и switch
switch_var=ctk.StringVar(value="on")
def sw():
    if switch_var.get()=='dark':
        ctk.set_appearance_mode('system')
    elif switch_var.get()=='white':
        ctk.set_appearance_mode('light')

switch=ctk.CTkSwitch(window,
                     text="Style",
                     text_color="grey",
                     command=sw,
                     variable=switch_var,
                     onvalue="white",
                     offvalue="dark"
                     )
switch.pack(pady=30)
switch.place(x=520,y=485)

# Фрейм
frame=ctk.CTkFrame(master=window,
                   width=200,
                   height=200,
                   fg_color="grey",
                   corner_radius=15).place(x=450,y=280)

# tabview
tabview=ctk.CTkTabview(window,width=400,
                       bg_color="transparent",
                       corner_radius=20,
                       border_width=2,
                       border_color="red",
                       segmented_button_fg_color="red",
                       segmented_button_selected_hover_color="white",
                       segmented_button_unselected_color="blue",
                       text_color="black")
tabview.pack()
tabview.place(x=30,y=5)
tabview.add("Stocks").grid_columnconfigure(0,weight=1)
tabview.add("Exchange").grid_columnconfigure(0,weight=1)

# Переход по tabview
text=ctk.CTkLabel(tabview.tab("Stocks"),
                  text=f'Компания\tЦена акции\tОбъем торгов'
                  f'\n{pars.company_name[12:13]}\t{pars.company_info[12][:1]}\t\t{pars.company_info[12][3:4]}'
                  # f'\n{pars.company_name[1:2]}\t{pars.company_info[1][:1]}\t\t{pars.company_info[1][3:4]}'
                  f'\n{pars.company_name[2:3]}\t{pars.company_info[2][:1]}\t{pars.company_info[2][3:4]}'
                  f'\n{pars.company_name[3:4]}\t{pars.company_info[3][:1]}\t\t{pars.company_info[3][3:4]}'
                  f'\n{pars.company_name[4:5]}\t{pars.company_info[4][:1]}\t\t{pars.company_info[4][3:4]}'
                  f'\n{pars.company_name[6:7]}\t\t{pars.company_info[6][:1]}\t\t{pars.company_info[6][3:4]}'
                  f'\n{pars.company_name[7:8]}\t\t{pars.company_info[7][:1]}\t\t{pars.company_info[7][3:4]}'
                  f'\n{pars.company_name[9:10]}\t{pars.company_info[9][:1]}\t{pars.company_info[9][3:4]}'
                  # f'\n{pars.company_name[10:11]}\t\t{pars.company_info[10][:1]}\t{pars.company_info[10][3:4]}'
                  f'\n{pars.company_name[11:12]}\t{pars.company_info[11][:1]}\t\t{pars.company_info[11][3:4]}'
                  f'\n{pars.company_name[29:30]}\t\t{pars.company_info[29][:1]}\t\t{pars.company_info[29][3:4]}'
                  ,text_color="grey",
                  font=("Comic Sans",14))
# Переход по tabview
text_2=ctk.CTkLabel(tabview.tab("Exchange"),
                  text=f'Currency\t\t\tPrice(RUB)'
                  f'\n{pars.exchange_name[8]}\t\t{pars.exchange_price[8]}'
                  f'\n{pars.exchange_name[11]}\t\t\t{pars.exchange_price[11]}'
                  f'\n{pars.exchange_name[29]}\t\t{pars.exchange_price[29]}',
                  text_color="grey",
                  font=("Comic Sans",14))
text.pack()
text_2.pack()

# TextBox
textbox=ctk.CTkTextbox(window,
                       width=200,
                       height=200,
                       scrollbar_button_color="blue",
                       corner_radius=15,
                       border_color="blue",
                       border_width=2,
                       fg_color="teal",
                       text_color='black')#
textbox.pack()
textbox.place(x=450,y=40)
label_cripto=ctk.CTkLabel(window,
                          text="Cripto Price",
                          text_color="grey",
                          font=("docker",14))
label_cripto.pack()
label_cripto.place(x=510,y=5)

cripto=[]
for i,j in zip(pars.cripto_name,pars.cripto_price):
    rows=i+' '+j
    cripto.append(rows)

cripto_rows = '\n'.join(cripto)

textbox.insert("0.0",f"{cripto_rows}")

dt_now = str(datetime.datetime.now())

label_date=ctk.CTkLabel(window,
                        text=f"Date {dt_now[:10]}\nTime{dt_now[10:16]}",
                        text_color="grey",
                        font=("docker",14),
                        bg_color="transparent")
label_date.pack()
label_date.place(x=500,y=245)


# OptionMenu
def enviar():
    rows=city.get()
    for i in range(len(pars.weather_city)):
        if rows==pars.weather_city[i]:
            lab.configure(text=pars.weather_tmp[i])
    pass

city=ctk.CTkOptionMenu(window,
                       values=pars.weather_city,
                       font=("docker",14),
                       fg_color="black",
                       text_color="grey",
                       bg_color="grey")
city.pack(pady=20)
city.set("Wether")
city.place(x=480,y=305)
lab=ctk.CTkLabel(window,
                 text="*_*",
                 width=200,
                 height=25,
                 text_color='black',
                 font=("arial bold",16),
                 bg_color = "grey")
lab.pack(pady=10)
lab.place(x=450,y=375)

# Кнопка
btn=ctk.CTkButton(window,
                  text="Enter",
                  command=enviar,
                  fg_color="black",
                  text_color="grey",
                  font=("arial bold",14),
                  bg_color="grey").place(x=480,y=340)

# Картинки
img_cod=ctk.CTkImage(light_image=Image.open(r"C:\Users\kerie\Desktop\pythonProject1\7ae296b1ea840340beb0.jpg"),
                        dark_image=Image.open(r"C:\Users\kerie\Desktop\pythonProject1\7ae296b1ea840340beb0.jpg"),
                        size=(350,200))

img1=ctk.CTkLabel(window,text=None,
                  image=img_cod).place(x=55,y=280)


img_w=ctk.CTkImage(light_image=Image.open(r"C:\Users\kerie\Desktop\pythonProject1\Wether.png"),
                        dark_image=Image.open(r"C:\Users\kerie\Desktop\pythonProject1\Wether.png"),
                        size=(80,40))

img2=ctk.CTkLabel(window,text=None,image=img_w).place(x=510,y=410)


window.mainloop()