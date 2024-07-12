from tkinter import *

root = Tk()
root.title("창 제목입니당") # 제목 설정
root.geometry("640x480") # 창 크기(가로x세로, x좌표, y좌표)

Label(root, text="메뉴를 선택해주세요").pack(side="top") #위쪽정렬
Button(root, text="주문하기").pack(side="bottom")


#메인프레임
frame_buger = Frame(root, relief="solid", bd=1) # 테두리
frame_buger.pack(side="left", fill="both", expand=True) #왼쪽정렬

Button(frame_buger, text="햄버거").pack()
Button(frame_buger, text="치즈햄버거").pack()
Button(frame_buger, text="치킨햄버거").pack()


#음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)#오른쪽 정렬
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()


root.mainloop() # 창이 닫히지 않게