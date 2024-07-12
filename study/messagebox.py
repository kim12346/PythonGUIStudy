import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("창 제목입니당") # 제목 설정
root.geometry("640x480") # 창 크기(가로x세로, x좌표, y좌표)

#기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.") # 제목, 표시되는 알림
def warn():
    msgbox.showinfo("경고", "해다 ㅇ좌석은 매진되었습니다.")
def error():
    msgbox.showerror("에러", "결제오류가 발생했습니다.")
def okcancle():
    msgbox.askokcancel("확인 / 취소", "해당좌석은 유아동반석입니다ㅏ. 예매해시겠습니가?")
def retrycancle():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    print("응답: ", response) #True, False, None => 예1, 아니오0, 그 외
    if response == 1: # 재시도
        print("재시도")
    elif response == 0: # 취소
        print("취소")
def yesno():
    msgbox.askyesno("예/아니오", "해당좌석은 역방향입니다. 예매하시겠습니까?")
def yesnocancle():
    response = msgbox.askyesnocancel(title=None, message="예매내역이 저장되지 않았습니다. \n저장하시겠습니까?")
    #네: 저장 후 종료
    #아니오: 저장 하지않고 종료
    #취소: 프로그램 종료 취소(현재 화면에서 계속 작업)
    print("응답: ", response) #True, False, None => 예1, 아니오0, 그 외
    if response == 1: # 네
        print("예")
    elif response == 0: # 아니오
        print("아니오")
    else:
        print("취소")
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancle, text="확인 취소").pack()
Button(root, command=retrycancle, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancle, text="예 아니오 취소").pack()


root.mainloop() # 창이 닫히지 않게