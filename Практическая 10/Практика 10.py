from tkinter import *
from decimal import *
from tkinter.ttk import Radiobutton 
  

def calculator():  
	
	def btn(digit):
		return Button(cal, text=digit, font=("Arial Bold", 12), bd = 4, bg= "#666", fg = "#fff", command = lambda : add_digit(digit))
	
	def add_digit(digit):
		value = calc.get() + str(digit)
		if value[0] == "0":
			value = value[1:]
		calc.delete(0, END)
		calc.insert(0,value)
		
	def add_operation(operation):
		value = calc.get()
		if value[-1] in "-+/*":
			value = value[:-1]
		calc.delete(0, END)
		calc.insert(0,value+operation)
	
	def calculation(operation):
		return Button(cal, text=operation, font=("Arial Bold", 12), bd = 4,bg= "#666", fg = "#fff", command = lambda : add_operation(operation))
	
	def result(operation):
		return Button(cal, text=operation, font=("Arial Bold", 12), bd = 4,bg= "#666", fg = "#fff", command = calculate)	 
	
	def calculate():
		value = calc.get()
		calc.delete(0, END)
		calc.insert(0, eval(value))
	   
	cal = Tk()
	cal.title("Калькулятор")
	cal.geometry("287x275")
	cal["bg"] = "#121212"
	calc = Entry(cal, justify = RIGHT, font = ("Arial Bold",20), width = 15)
	calc.insert(0,"0")
	calc.grid(row = 0, column = 0, columnspan = 3)
	btn("1").grid(row = 1, column = 0, stick = "wens", padx = 2, pady = 5)
	btn("2").grid(row = 1, column = 1, stick = "wens", padx = 2, pady = 5)
	btn("3").grid(row = 1, column = 2, stick = "wens", padx = 2, pady = 5)
	btn("4").grid(row = 2, column = 0, stick = "wens", padx = 2, pady = 5)
	btn("5").grid(row = 2, column = 1, stick = "wens", padx = 2, pady = 5)
	btn("6").grid(row = 2, column = 2, stick = "wens", padx = 2, pady = 5)
	btn("7").grid(row = 3, column = 0, stick = "wens", padx = 2, pady = 5)
	btn("8").grid(row = 3, column = 1, stick = "wens", padx = 2, pady = 5)
	btn("9").grid(row = 3, column = 2, stick = "wens", padx = 2, pady = 5)
	btn("0").grid(row = 4, column = 0, stick = "wens", padx = 2, pady = 5)
	
	
	
	calculation("/").grid(row = 2, column = 3, stick = "wens", padx = 2, pady = 5)
	calculation("*").grid(row = 3, column = 3, stick = "wens", padx = 2, pady = 5)
	calculation("-").grid(row = 4, column = 3, stick = "wens", padx = 2, pady = 5)
	calculation("+").grid(row = 4, column = 2, stick = "wens", padx = 2, pady = 5)
	
	result("=").grid(row = 0, column = 3, rowspan = 2, stick = "wens", padx = 2, pady = 5)
	
	
	
	cal.grid_columnconfigure(0,minsize = 60)
	cal.grid_columnconfigure(1,minsize = 60)
	cal.grid_columnconfigure(2,minsize = 60)
	cal.grid_columnconfigure(3,minsize = 60)
	
	
	cal.grid_rowconfigure(1,minsize = 60)
	cal.grid_rowconfigure(2,minsize = 60)
	cal.grid_rowconfigure(3,minsize = 60)
	cal.grid_rowconfigure(4,minsize = 60)

	
def checkbox():
	
	def change():
		
		box = Tk()
		box.title("Результат")
		box.geometry("200x50")
		box["bg"] = "#666"
		label = Label(box,  font=("Arial Bold", 12), bg= "#666", fg = "#fff")
		label.grid(column = 0, row = 2, columnspan = 3)
		if var.get() == 0:
			label["text"] = "Вы выбрали 1-ый вариант" 
		elif var.get() == 1:
			label["text"] = "Вы выбрали 2-ой вариант" 
		elif var.get() == 2:
			label["text"] = "Вы выбрали 3-ий вариант" 

	
	check = Tk()
	check.title("Чекбокс")
	check.geometry("190x55")
	check["bg"] = "#666"
	var = IntVar(check)
	rad1 = Radiobutton(check, text="Первый", variable = var, value=0)
	rad1.grid(column = 0, row = 0)
	rad2 = Radiobutton(check, text="Второй", variable = var, value=1)
	rad2.grid(column = 1, row = 0)
	rad3 = Radiobutton(check, text="Третий", variable = var, value=2)
	rad3.grid(column = 2, row = 0)
	btn1 = Button(check, text="Клик", command=change, bg= "#ff0000", fg = "#fff")
	btn1.grid(column = 0, row = 1, columnspan = 3,  stick = "wens")
	
	
def text():
	def newtext():
		file = open("text.txt", "r",encoding='utf-8') 
		txt = Text(text1, width = 50, height = 10, bg = "#666", fg = "#fff", font=("Arial Bold", 14))
		txt.insert("1.0",(file.read()))
		txt.pack()
	def exit():
		text1.destroy()	
	
	text1 = Tk()
	text1.title("Работа с текстом")
	text1.geometry('560x250')
	text1["bg"] = "#121212"
	menu = Menu(text1)
	new_item = Menu(menu)
	new_item.add_command(label = "Открыть", command = newtext)
	new_item.add_separator()
	new_item.add_command(label = "Выход", command = exit)
	menu.add_cascade(label = "Файл", menu=new_item)
	text1.config(menu=menu)
	text1.mainloop()
 
window = Tk()
window.title("Якубов Ян Альбертович")
window.geometry('356x150')
window["bg"] = "#121212"
btn1 = Button(window, text="Калькулятор", font=("Arial Bold", 12), command=calculator, bg= "#666", fg = "#fff")
btn1.grid(column=0, row=0, padx = 4, pady = 5) 

btn2 = Button(window, text="Чекбоксы", font=("Arial Bold", 12), command = checkbox, bg= "#666", fg = "#fff")
btn2.grid(column=2, row=0, padx = 4, pady = 5)

btn3 = Button(window, text="Работа с текстом", font=("Arial Bold", 12), command = text, bg= "#666", fg = "#fff")
btn3.grid(column=4, row=0, padx = 4, pady = 5) 


window.mainloop()

