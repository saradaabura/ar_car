import tkinter as tk
from datetime import datetime

root = tk.Tk()

# init
file_path = "/home/raspi5/ar_auto/test.txt"
root.geometry("800x600")
sz = "70"
ft = ("Arial", sz)

# ラベルを初期化時に作成
data0 = tk.Label(root, fg="white", text="DEC_MKR", font=ft, bg="black")
status0 = tk.Label(root, fg="green", text="OK", font=ft, bg="black")
data1 = tk.Label(root, fg="white", text="X", font=ft, bg="black")
status1 = tk.Label(root, fg="green", text="0", font=ft, bg="black")
data2 = tk.Label(root, fg="white", text="Y", font=ft, bg="black")
status2 = tk.Label(root, fg="green", text="0", font=ft, bg="black")
data3 = tk.Label(root, fg="white", text="IMGSZ", font=ft, bg="black")
status3 = tk.Label(root, fg="green", text="0", font=ft, bg="black")
data4 = tk.Label(root, fg="white", text="CTR", font=ft, bg="black")
status4 = tk.Label(root, fg="red", text="ERROR", font=ft, bg="black")

# グリッド位置とプロパティを指定
positions = [
    (data0, 0, 0, 'w'), (status0, 0, 1, 'e'),
    (data1, 0, 2, 'w'), (status1, 0, 3, 'e'),
    (data2, 0, 4, 'w'), (status2, 0, 5, 'e'),
    (data3, 1, 0, 'w'), (status3, 1, 1, 'e'),
    (data4, 1, 2, 'w'), (status4, 1, 3, 'e'),
]

# まとめて配置
for widget, row, column, sticky in positions:
    widget.grid(row=row, column=column, sticky=sticky)

# 時刻を表示するラベルの追加
time_label = tk.Label(root, fg="yellow", font=ft, bg="black")
time_label.grid(row=2, column=0, columnspan=6, pady=20)

# ラベルのテキストを更新する関数
def update_labels():
    # 必要に応じてラベルのテキストを更新
    with open(file_path, "r") as file:
        data = file.read()
    values = data.strip("()").split(",")
    
    # 空の文字列を無視してfloatに変換
    fvalues = [value.strip("' ") for value in values if value.strip()]
    
    # 値が期待通りに存在するか確認
    if len(fvalues) >= 5:
        print(fvalues)
        status0.config(text=int(fvalues[0]))
        status1.config(text=int(float(fvalues[1])))
        status2.config(text=int(float(fvalues[2])))
        status3.config(text=int(float(fvalues[3])))
        status4.config(text=fvalues[4])
    else:
        print("データが不完全です。")


# 時刻を更新する関数
def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    time_label.config(text=current_time)
    update_labels()  # ラベルを更新
    root.after(50, update_time)  # 1秒ごとに更新

# 時刻の更新を開始
update_time()

root.tk_setPalette(background="black")
root.mainloop()
