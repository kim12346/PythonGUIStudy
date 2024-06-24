from tkinter import *

root = Tk()
root.title("창 제목입니당") # 제목 설정
root.geometry("640x480+100+300") # 창 크기(가로x세로, x좌표, y좌표)

root.resizable(False, False)# x너비, y높이 값 변경 불가
root.mainloop() # 창이 닫히지 않게