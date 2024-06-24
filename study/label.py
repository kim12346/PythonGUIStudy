from tkinter import *

root = Tk()
root.title("GUI") # 제목 설정
root.geometry("640x480")
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="파이썬/check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또만나요")

    global photo2
    photo2 = PhotoImage(file="파이썬/check2.png")
    label2.config(image=photo2)
btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop() # 창이 닫히지 않게