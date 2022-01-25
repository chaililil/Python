from tkinter import *
from tkinter import messagebox
import json
import os

def register():
	
	def show1():
		
		if username.get() == "":
			messagebox.showerror("Ошибка", "Вы не ввели имя пользователя")
		else:
			
			def zametka():
				
				user = username.get()
				
				qwe = os.getcwd()
				path = qwe,"/", tt
				path = ''.join(path)
					
				os.chdir(path)
				
				def zamm():
					
					
					
					def zamm1():
						
						def save1():
			
							with open(zz1, "w") as file:
								file.write(txt.get("1.0",'end-1c'))
								os.chdir(qwe)						
						def exit():
							text1.destroy()	
							os.chdir(qwe)				
						text1 = Tk()
						text1.title(zz)
						text1.geometry('560x250')
						text1["bg"] = "#121212"		
						menu = Menu(text1)
						new_item = Menu(menu)
		
						zam.destroy()
		
						new_item.add_command(label = "Сохранить", command = save1)
			
						new_item.add_separator()
		
						new_item.add_command(label = "Выход", command = exit)
						menu.add_cascade(label = "Файл", menu=new_item)
			
						file = open(zz1, "r") 
						txt = Text(text1, width = 50, height = 10, bg = "#666", fg = "#fff", font=("Arial Bold", 14))
						txt.insert("1.0",(file.read()))
						txt.pack()
		
						text1.config(menu=menu)
						text1.mainloop()						
					
					zz = zamet.get()
					zz1 = zz,".txt"
					zz1 = ''.join(zz1)
					
					try:
						file = open(zz1)
					except IOError as e:
						messagebox.showwarning(title="Заметка не найдена", message="Будет создана новая заметка")
						file = open(zz1, "w")
						zamm1()
					else:
						with file:
							zamm1()
				
				zam = Tk()
				zam.title(tt)
				zam.geometry('358x175')
				zam["bg"] = "#121212"
				reg.destroy()
				lbl = Label(zam, text="Название заметки", font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
				lbl.grid(column=0, row=0, columnspan = 2, padx = 4, pady = 5) 
				zamet = Entry(zam, font = ("Arial Bold",20), bg = "#666", width = 23)
				zamet.grid(column=0, columnspan = 2, row=1, padx = 4, pady = 5) 
				btn = Button(zam, text = "ГОТОВО", font=("Arial Bold", 16), bg= "#ff0000", command = zamm, height=1)
				btn.grid(column=0, row=2, columnspan = 2, padx = 4, pady = 5)
				lbl = Label(zam, text="Количество заметок пользователя:", font=("Arial Bold", 14), bg= "#121212", fg = "#fff")
				lbl.grid(column=0, row=3, pady = 5) 
				path1 = '.'
				num_files1 = len([f for f in os.listdir(path1)
				if os.path.isfile(os.path.join(path1, f))])
				num1 = num_files1

				lbl = Label(zam, text= (num1), font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
				lbl.grid(column=1, row=3, pady = 2)

			tt = username.get()				
			tt1 = os.path.exists(tt)
			
			if tt1 == True:
				messagebox.showwarning(title="Пользователь существует", message="Будут открыты заметки этого пользователя")
				zametka()
			else:
				tt2 = tt, '.txt'
				tt2= ''.join(tt2)
				f = open(tt2, "w")
				messagebox.showinfo(title="Регистрация", message="Регистрация прошла успешно")
				
				num2 = num+1
				lbl = Label(window, text= (num2), font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
				lbl.grid(column=1, row=2, padx = 0, pady = 5)
				
				os.mkdir(tt)
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
			
			def zametka():
				
				user = username.get()
				
				qwe = os.getcwd()
				path = qwe,"/", tt
				path = ''.join(path)
					
				os.chdir(path)
				
				def zamm():
					
					def zamm1():
						
						def save1():
			
							with open(zz1, "w") as file:
								file.write(txt.get("1.0",'end-1c'))
								os.chdir(qwe)							
						def exit():
							text1.destroy()	
							os.chdir(qwe)					
						text1 = Tk()
						text1.title(zz)
						text1.geometry('560x250')
						text1["bg"] = "#121212"		
						menu = Menu(text1)
						new_item = Menu(menu)
		
						zam.destroy()
		
						new_item.add_command(label = "Сохранить", command = save1)
			
						new_item.add_separator()
		
						new_item.add_command(label = "Выход", command = exit)
						menu.add_cascade(label = "Файл", menu=new_item)
			
						file = open(zz1, "r") 
						txt = Text(text1, width = 50, height = 10, bg = "#666", fg = "#fff", font=("Arial Bold", 14))
						txt.insert("1.0",(file.read()))
						txt.pack()
		
						text1.config(menu=menu)
						text1.mainloop()						
					
					zz = zamet.get()
					zz1 = zz,".txt"
					zz1 = ''.join(zz1)
					
					try:
						file = open(zz1)
					except IOError as e:
						messagebox.showwarning(title="Заметка не найдена", message="Будет создана новая заметка")
						file = open(zz1, "w")
						zamm1()
					else:
						with file:
							zamm1()
				
				zam = Tk()
				zam.title(tt)
				zam.geometry('358x175')
				zam["bg"] = "#121212"
				fin.destroy()
				lbl = Label(zam, text="Название заметки", font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
				lbl.grid(column=0, row=0, columnspan = 2, padx = 4, pady = 5) 
				zamet = Entry(zam, font = ("Arial Bold",20), bg = "#666", width = 23)
				zamet.grid(column=0, columnspan = 2, row=1, padx = 4, pady = 5) 
				btn = Button(zam, text = "ГОТОВО", font=("Arial Bold", 16), bg= "#ff0000", command = zamm, height=1)
				btn.grid(column=0, row=2, columnspan = 2, padx = 4, pady = 5)
				lbl = Label(zam, text="Количество заметок пользователя:", font=("Arial Bold", 14), bg= "#121212", fg = "#fff")
				lbl.grid(column=0, row=3, pady = 5) 
				path1 = '.'
				num_files1 = len([f for f in os.listdir(path1)
				if os.path.isfile(os.path.join(path1, f))])
				num1 = num_files1

				lbl = Label(zam, text= (num1), font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
				lbl.grid(column=1, row=3, pady = 2)

			tt = username.get()				
			tt1 = os.path.exists(tt)
			
			if tt1 == True:
				zametka()
			else:
				tt2 = tt, '.txt'
				tt2= ''.join(tt2)
				f = open(tt2, "w")
				messagebox.showwarning(title="Пользователь не найден", message="Будет зарегистрирован новый пользователь")
				
				num2 = num+1
				lbl = Label(window, text= (num2), font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
				lbl.grid(column=1, row=2, padx = 0, pady = 5)
				
				os.mkdir(tt)
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

lbl = Label(window, text="Зарегистрированных пользователей:", font=("Arial Bold", 14), bg= "#121212", fg = "#fff")
lbl.grid(column=0, row=2, padx = 0, pady = 5) 

lbl = Label(window, text= (num), font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
lbl.grid(column=1, row=2, padx = 0, pady = 5)
window.mainloop()
