import tkinter.ttk as ttk
import time
from tkinter import *

root = Tk()
root.title("창 제목입니당") # 제목 설정
root.geometry("640x480") # 창 크기(가로x세로, x좌표, y좌표)

#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10ms마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() #작동중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): #1부터 100
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) #progress bar의 값 설정
        progressbar2.update() # ui없데이트
        print(p_var2.get())
btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop() # 창이 닫히지 않게