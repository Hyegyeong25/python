
from tkinter import *
from tkinter import messagebox

#함수 선언 부분
def myFunc() :
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠^^")

# main code
window = Tk()

photo = PhotoImage(file = "D:\\2학기\\빅데이터프로그래밍(파이썬)\\gif\\dog2.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()
window.mainloop()