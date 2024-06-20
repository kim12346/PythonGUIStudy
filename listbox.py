from tkinter import *

root = Tk()
root.title("창 제목입니당") # 제목 설정
root.geometry("640x480") # 창 크기(가로x세로, x좌표, y좌표)

listbox = Listbox(root, selectmode="extended", height=0)
    # extended: 다중선택가능, single: 하나만 선택가능, height = 1: 리스트를 요소를 한개만 보기
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END, "수박")

listbox.pack()



def btncmd():
    listbox.delete(END)
    # END: 맨 뒤에 항목을 삭제, 0: 맨 앞 항목 삭제

    #갯수확인
    #print("리스트에는 ", listbox.size(), "개가 있어요")

    # 항목확인(시작인덱스, 끝 인덱스)
    #print("1번째부터 3번째까지의 항목: ", listbox.get(0, 2))

    # 선택된 항목 확인(위치로 반환 ex) 1, 2, 3)
    #print("선택된 항목: ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않게