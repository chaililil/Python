from tkinter import *
from tkinter import messagebox
import json
import time
import os

def register():
	
	def show1():
		
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
		
				reg.destroy()
		
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
				messagebox.showinfo(title="Регистрация", message="Регистрация прошла успешно")
				f = open(tt1, "w")
				
				num1 = num+1		
				lbl = Label(window, text= (num1), font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
				lbl.grid(column=1, row=2, padx = 0, pady = 5)
				
				zametka()
		
			else:
				with file:
					messagebox.showwarning(title="Пользователь существует", message="Будет открыта существующая заметка")
					zametka()
			
	reg = Tk()
	reg.title("Регистрация")
	reg.geometry('360x150')
	reg["bg"] = "#121212"
	lbl = Label(reg, text="Зарегистрируйте имя пользователя", font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
	lbl.grid(column=0, row=0, padx = 4, pady = 5, columnspan = 2) 
	username = Entry(reg, font = ("Arial Bold",20), width = 23, bg = "#666")
	username.grid(column=0, row=1, padx = 4, pady = 5) 
	btn = Button(reg, text = "ГОТОВО", font=("Arial Bold", 16), bg= "#ff0000", command = show1, height=1, width=15)
	btn.grid(column=0, row=2, padx = 4, pady = 5, columnspan = 2)
	
	
def poisk():
	
	def show2():
	
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
				
				fin.destroy()	
		
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
				messagebox.showwarning(title="Пользователь не найден", message="Будет зарегестрирован новый пользователь")
				f = open(tt1, "w")
				
				num2 = num+1
				lbl = Label(window, text= (num2), font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
				lbl.grid(column=1, row=2, padx = 0, pady = 5)
							
				zametka()
		
			else:
				with file:
					zametka()
			
	
	fin = Tk()
	fin.title("Поиск заметки")
	fin.geometry('360x150')
	fin["bg"] = "#121212"
	lbl = Label(fin, text="Введите имя пользователя", font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
	lbl.grid(column=0, row=0, padx = 4, pady = 5, columnspan = 2) 
	username = Entry(fin, font = ("Arial Bold",20), width = 23, bg = "#666")
	username.grid(column=0, row=1, padx = 4, pady = 5) 
	btn = Button(fin, text = "ГОТОВО", font=("Arial Bold", 16), bg= "#ff0000", command = show2, height=1, width=15)
	btn.grid(column=0, row=2, padx = 4, pady = 5, columnspan = 2)
	
path = '.'
num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])
num = num_files-1

window = Tk()
window.title("Заметки")
window.geometry('390x150')
window["bg"] = "#121212"

btn = Button(window, text = "Новый пользователь", font=("Arial Bold", 16), bg= "#ff0000", command = register, height=1, width=31)
btn.grid(column=0, row=0, padx = 4, pady = 7, columnspan = 3) 

btn = Button(window, text = "Найти заметку", font=("Arial Bold", 16), bg= "#ff0000", command = poisk, height=1, width=31)
btn.grid(column=0, row=1, padx = 4, pady = 0, columnspan = 3) 

lbl = Label(window, text="Текущее количество пользователей:", font=("Arial Bold", 14), bg= "#121212", fg = "#fff")
lbl.grid(column=0, row=2, padx = 0, pady = 5) 

lbl = Label(window, text= (num), font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
lbl.grid(column=1, row=2, padx = 0, pady = 5)
window.mainloop()
