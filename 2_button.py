from tkinter import *

root = Tk()
root.title("GUI") # 제목 설정

btn1 = Button(root, text="버튼1", fg="red", bg="white")
btn1.pack() # pack을 붙여야 화면에 보임

def btncmd():
    print("버튼이 클릭되었어요")
    
photo = PhotoImage(file="파이썬/check.png")
btn6 = Button(root, image=photo, text="동작하는 버튼", command=btncmd)
btn6.pack()

root.mainloop() # 창이 닫히지 않게