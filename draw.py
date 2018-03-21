from tkinter import *
root = Tk()
root.title('我的繪圖功能')
root.geometry('600x400')

canvas_width = 600
canvas_height = 300
cvs = Canvas(root,
             width=canvas_width,
             height=canvas_height,
             bg="white")
cvs.pack()

img = PhotoImage(file="myphoto.gif")
cvs.create_image(10,10, anchor=NW, image=img)
cvs.create_text(10, canvas_height/2, anchor=NW, text="作者: Andrew Wang")
y = int(canvas_height / 2)
cvs.create_line(0, y, canvas_width, y, fill="red")

mainloop()
