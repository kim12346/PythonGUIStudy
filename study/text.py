from tkinter import *

root = Tk()
root.title("창 제목입니당") # 제목 설정
root.geometry("640x480") # 창 크기(가로x세로, x좌표, y좌표)

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")# 텍스트의 기본값을 지정

e = Entry(root, width=30) # 로그인 아이디와 같이 엔터를 사용하지 못하는 값
e.pack()
e.insert(0, "한줄만 입력해여")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))# 1: 첫번째 라인, 0: 0번째 인덱스 위치
    print(e.get())

    #내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않게