from tkinter import *

my_window = Tk()
my_window.title('小計算機')
my_window.geometry('400x400')

# 加入一個字串變數，用來控制 Label 的 textvariable
label_var = StringVar()
label_var.set('0')
# 原本的 text 改成 textvariable
my_label = Label(my_window, textvariable = label_var, width = 20, bg = 'yellow')
my_label.pack()

my_label1 = Label(my_window, text = '請輸入第一個數字')
my_label1.pack()
my_enter1 = Entry(my_window, width = 20)
my_enter1.pack()
my_label2 = Label(my_window, text = '請輸入第二個數字')
my_label2.pack()
my_enter2 = Entry(my_window, width = 20)
my_enter2.pack()

# 新增一個 Button 的 command 的處理函數
def click_add():
    label_var.set(int(my_enter1.get()) + int(my_enter2.get()))

# 加入 Button 物件
my_button = Button(my_window, text = '相加', command = click_add)
my_button.pack()

# 進入事件迴圈
my_window.mainloop()
