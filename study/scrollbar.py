from tkinter import *

root = Tk()
root.title("창 제목입니당") # 제목 설정
root.geometry("640x480") # 창 크기(가로x세로, x좌표, y좌표)

frame = Frame(root)
frame.pack()


scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")


#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10,yscrollcommand = scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일") #1일, 2일...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 상하로 움직이는것에 대한 처리

root.mainloop() # 창이 닫히지 않게