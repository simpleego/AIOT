import tkinter as tk
from tkinter import messagebox

# 커피 메뉴/ 가격
menu = {
    "아메리카노":1500,
    "라떼": 2000,
    "카푸치노":2500
}

def select_coffee(coffee):
    try:
        money = int(entry_money.get()) # 사용자가 입력한 동전
        price = menu[coffee]

        if money < price:
            messagebox.showwarning("잔액부족",f"{coffee} 가격은 {price}입니다. ")
        else:
            change = money - price
            label_result.config(text=f"{coffee}가 나왔습니다.\n잔돈: {change}")
    except ValueError:
        messagebox.showerror("입력오류","숫자를 올바르게 입력하세요!!")

# 윈도우 생성
root = tk.Tk()
root.title("커피 자판기")

# 컴포넌트 생성 및 등록

# 레이블 생성 및 등록
label_info = tk.Label(root, text="동전을 넣고 커피를 선택하세요")
label_info.grid(row=0,column=0, columnspan=3, pady=10)

# 동전입력
label_money = tk.Label(root, text="투입 금액:")
label_money.grid(row=1,column=0, padx=10, pady=10)
entry_money = tk.Entry(root)
entry_money.grid(row=1,column=1, padx=10, pady=10)

# 커피 버튼
btn_americano = tk.Button(root, text=f"아메리카노 ({menu['아메리카노']}원)",
                          command=lambda: select_coffee("아메리카노"))
btn_americano.grid(row=2,column=0, padx=10, pady=10)

btn_latte = tk.Button(root, text=f"라떼 ({menu['라떼']}원)", command=lambda: select_coffee("라떼")) 
btn_latte.grid(row=2, column=1, padx=10, pady=10) 

btn_cappuccino = tk.Button(root, text=f"카푸치노 ({menu['카푸치노']}원)", command=lambda: select_coffee("카푸치노"))
btn_cappuccino.grid(row=2, column=2, padx=10, pady=10)


# 결과 출력
label_result = tk.Label(root, text="커피 출력")
label_result.grid(row=3, column=0, columnspan=3, pady=10)

# 컴포넌트 이벤트 등록 및 처리




root.mainloop()