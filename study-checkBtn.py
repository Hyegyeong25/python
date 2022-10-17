
from tkinter import *
from tkinter import messagebox

window = Tk()

#함수 선언 부분
def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크 버튼이 꺼졌어요."+str(chk.get()))
    else :
        messagebox.showinfo("", "체크 버튼이 켜졌어요."+str(chk.get()))

# main code
chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요:", variable = chk, command = myFunc)

cb1.pack()
window.mainloop()