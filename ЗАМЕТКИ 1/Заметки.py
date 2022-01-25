from tkinter import *
from tkinter import messagebox
import json
import time

def show():
	
	if username.get() == "":
		messagebox.showerror("Ошибка", "Вы не ввели имя пользователя")
	else:
		
		tt = username.get()
		
		tt1 = tt, '.txt'
		tt1= ''.join(tt1)
		
		def zametka():	
		
			def save1():
			
				with open(tt1, "w") as file:
					file.write(txt.get("1.0",'end-1c'))
	
			def exit():
				text1.destroy()	
		
			text1 = Tk()
			text1.title(username.get())
			text1.geometry('560x250')
			text1["bg"] = "#121212"		
			menu = Menu(text1)
			new_item = Menu(menu)
		
		
			new_item.add_command(label = "Сохранить", command = save1)
		
			new_item.add_separator()
		
			new_item.add_command(label = "Выход", command = exit)
			menu.add_cascade(label = "Файл", menu=new_item)
		
			file = open(tt1, "r") 
			txt = Text(text1, width = 50, height = 10, bg = "#666", fg = "#fff", font=("Arial Bold", 14))
			txt.insert("1.0",(file.read()))
			txt.pack()
		
			text1.config(menu=menu)
			text1.mainloop()
		
		try:
			file = open(tt1)
		except IOError as e:
			messagebox.showinfo(title="Логин не найден", message="Зарегистрирован новый пользователь")
			
			f = open(tt1, "w")			
			zametka()
		
		else:
			with file:
				zametka()	
		
window = Tk()
window.title("Заметки")
window.geometry('400x150')
window["bg"] = "#121212"
lbl = Label(window, text="ВВЕДИТЕ ИМЯ ПОЛЬЗОВАТЕЛЯ", font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
lbl.grid(column=0, row=0, padx = 4, pady = 5, columnspan = 2) 
username = Entry(window, font = ("Arial Bold",20), width = 15, bg = "#666")
username.grid(column=0, row=1, padx = 4, pady = 5) 
btn = Button(window, text = "НАЧАТЬ", bg= "#ff0000", command = show, height=2, width=15)
btn.grid(column=1, row=1, padx = 4, pady = 5) 
window.mainloop()
