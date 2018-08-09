import tkinter as tk
import tkinter.ttk as tt

window = tk.Tk()
window.title('學生基本資料')
window.geometry('400x320')

labName = tk.Label(window, text = '姓名:', justify=tk.RIGHT, width=50)
labName.place(x=10, y=10, width=100, height=20)

varName = tk.StringVar()
varName.set('')
entName = tk.Entry(window, width = 120, textvariable = varName)
entName.place(x=110, y=10, width=120, height=20)

labGrade = tk.Label(window, text = '年級:', justify=tk.RIGHT, width=50)
labGrade.place(x=10, y=40, width=100, height=20)

stdGrade = ('1','2','3')
comGrade = tt.Combobox(window, width=50, values=stdGrade)
comGrade.place(x=110, y=40, width=60, height=20)

labGrade = tk.Label(window, text = '班級:', justify=tk.RIGHT, width=50)
labGrade.place(x=190, y=40, width=100, height=20)

stdClass = ('甲','乙','丙','丁','戊')
comClass = tt.Combobox(window, width=50, values=stdClass)
comClass.place(x=300, y=40, width=60, height=20)

labSex = tk.Label(window, text = '性別:', justify=tk.RIGHT, width=50)
labSex.place(x=10, y=70, width=100, height=20)

varSex = tk.IntVar()
varSex.set(1)       # 預設值1=男
radBoy = tk.Radiobutton(window, variable=varSex, value=1,text='男生')
radBoy.place(x=110, y=70, width=60, height=20)
radGirl = tk.Radiobutton(window, variable=varSex, value=0,text='女生')
radGirl.place(x=190, y=70, width=60, height=20)

# 核取方塊
signin = tk.IntVar()
signin.set(0)       # 預設值0=未報到
chkSignin = tk.Checkbutton(window, text='是否報到', variable=signin,
                        onvalue=1, offvalue=0)
chkSignin.place(x=30, y=100, width=100, height=20)

def addInfo():
    result = '姓名:' + entName.get()
    result += ';年級:' + comGrade.get()
    result += ';班級:' + comClass.get()
    result += ';性別:' + ('男生' if varSex.get() else '女生')
    result += ';報到:' + ('是' if signin.get() else '否')
    lstStudent.insert(0,result)
    
btnAdd = tk.Button(window, text='加入', width=40, command=addInfo)
btnAdd.place(x=150, y=100, width=100, height=20)

btnDel = tk.Button(window, text='刪除', width=40, command=addInfo)
btnDel.place(x=260, y=100, width=100, height=20)

lstStudent = tk.Listbox(window, width=380)
lstStudent.place(x=10, y=130, width=380, height=180)

window.mainloop()
