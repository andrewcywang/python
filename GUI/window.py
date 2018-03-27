import tkinter as tk
import tkinter.messagebox as tm

my_window = tk.Tk()
my_window.title('Hello World!')
my_window.geometry('400x100')

# 加入一個字串變數，用來控制 Label 的 textvariable
label_var = tk.StringVar()
label_var.set('Hello Windows!')

# 原本的 text 改成 textvariable
my_label = tk.Label(my_window, textvariable = label_var, bg = 'yellow')
my_label.pack()

my_enter = tk.Entry(my_window, width = 20)
my_enter.pack()

def click_me():
    label_var.set(my_enter.get())

my_button1 = tk.Button(my_window, text = 'Click Me!', command = click_me)
my_button1.pack()

def show_message():
    tm.showinfo(title = '訊息框', message = '請按下OK按鈕')
                                
# 多加一個 Button 物件
my_button2 = tk.Button(my_window, text = '訊息框', command = show_message)
my_button2.pack()

# 進入事件迴圈
my_window.mainloop()
