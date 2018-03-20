from tkinter import *

my_window = Tk()
my_window.title('Hello World!')
my_window.geometry('400x400')

# 加入一個字串變數，用來控制 Label 的 textvariable
label_var = StringVar()
label_var.set('Hello Windows!')

# 原本的 text 改成 textvariable
my_label = Label(my_window, textvariable = label_var, bg = 'yellow')
my_label.pack()

my_enter = Entry(my_window, width = 20)
my_enter.pack()

# 新增一個 Button 的 command 的處理函數
def click_me():
    label_var.set(my_enter.get())

# 加入 Button 物件
my_button = Button(my_window, text = 'Click Me!', command = click_me)
my_button.pack()

# 進入事件迴圈
my_window.mainloop()
