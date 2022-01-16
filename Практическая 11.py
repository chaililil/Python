#Номер зачетки 217210, следовательно, нужен 10 репозиторий с именем dotnet 
from tkinter import *
from tkinter import messagebox
import json
import requests
from pprint import pprint


def show():
	
	if username.get() == "":
		messagebox.showerror("Ошибка", "Вы не ввели имя репозитория")
	else:
		url = f"https://api.github.com/users/{username.get()}"
		user_data = requests.get(url).json()
		
		dat1 = user_data["company"]
		dat2 = user_data["created_at"]
		dat3 = user_data["email"]
		dat4 = user_data["id"]
		dat5 = user_data["name"]
		dat6 = user_data["url"]
		
		if file1.get() == "":
			messagebox.showerror("Ошибка", "Вы не ввели имя файла")
		else:
			gg = file1.get()
		
			repos = {"company":dat1, "created_at":dat2,
					"email":dat3, "id":dat4,
					"name":dat5, "url":dat6}
		
			with open(gg, "w") as write_file:
				json.dump(repos, write_file, indent = 2)		
	
window = Tk()
window.title("Поиск репозиория")
window.geometry('400x150')
window["bg"] = "#121212"
lbl = Label(window, text="ВВЕДИТЕ ИМЯ РЕПОЗИТОРИЯ", font=("Arial Bold", 16), bg= "#121212", fg = "#fff")
lbl.grid(column=0, row=0, padx = 4, pady = 5, columnspan = 2) 
username = Entry(window, font = ("Arial Bold",20), width = 15, bg = "#666")
username.grid(column=0, row=1, padx = 4, pady = 5) 

#Здесь осуществляется ввод имени файла (вместе с расширением)
lbl1 = Label(window, text="Введите имя файла", font=("Arial Bold", 12), bg= "#121212", fg = "#fff")
lbl1.grid(column=1, row=2) 
file1 = Entry(window, font = ("Arial Bold",12), width = 15, bg = "#666")


file1.grid(column=1, row=3)
btn = Button(window, text = "НАЙТИ", bg= "#ff0000", command = show, height=2, width=15)
btn.grid(column=1, row=1, padx = 4, pady = 5) 


window.mainloop()


