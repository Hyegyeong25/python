
from tkinter import *

window = Tk()

photo = PhotoImage(file = "D:\\2학기\\빅데이터프로그래밍(파이썬)\\gif\\dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()