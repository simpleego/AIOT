import tkinter as win
from tkinter import messagebox

def calc_bmi():
    try:
        height1 = float(height.get()) / 100
        weight1 = float(weight.get())

        bmi = weight1 / (height1 ** 2)

        # BMI 평가
        if bmi < 18.5:
            result = "저체중"
        elif 18.5 <= bmi < 23:
            result = "정상"
        elif 23 <= bmi < 25:
            result = "과체중"
        else:
            result = "비만"

        lbl_result.config(text=f"BMI: {bmi:.2f} ({result})")

    except ValueError:
        messagebox.showerror("입력 오류","숫자를 올바르게 입력하세요")

root = win.Tk() # 윈도우 생성자를 이용해서 윈도우를 생성
root.title("BMI  계산기")

# 키 입력 
lbl_height = win.Label(root, text="키(cm) :")
lbl_height.grid(row=0, column=0, padx=10, pady=10)
height = win.Entry(root)
height.grid(row=0, column=1, padx=10, pady=10)


# 키 입력 
lbl_weight = win.Label(root, text="몸무게(kg) :")
lbl_weight.grid(row=1, column=0, padx=10, pady=10)
weight = win.Entry(root)
weight.grid(row=1, column=1, padx=10, pady=10)

# BMI 계산 버튼
btn = win.Button(root, text="BMI 계산",command=calc_bmi)
btn.grid(row=3, column=1, padx=10, pady=10)


# 결과 출력
lbl_result = win.Label(root, text="BMI  결과")
lbl_result.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()