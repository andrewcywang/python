from tkinter import *
root = Tk()
root.title('我的繪圖功能')
root.geometry('600x400')

canvas_width = 600
canvas_height = 300
cvs = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
cvs.pack()

img = PhotoImage(file="myphoto.gif")
cvs.create_image(10,10, anchor=NW, image=img)
cvs.create_text(10, canvas_height/2, anchor=NW, text="作者: Andrew Wang")
y = canvas_height / 2
cvs.create_line(0, y, canvas_width, y, fill="red")

x1, y1, x2, y2=140, 10, 590, 290
cvs.create_rectangle(x1, y1, x2, y2,fill='yellow')
cvs.create_oval(x1, y1, x2, y2,fill='green')
cvs.create_arc(x1+90, y1+20, x2-90, y2-20,start=30,extent=270,fill='blue')

points = [10,180,150,200,100,290]
obj = cvs.create_polygon(points, outline='black',fill='red', width=3)

cvs2 = Canvas(root, width=canvas_width, height=40, bg="orange")
cvs2.pack()

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass",
           "info", "questhead", "question", "warning"]
nsteps = len(bitmaps)
step_x = int(canvas_width / nsteps)

for i in range(nsteps):
   cvs2.create_bitmap((i+1)*step_x - step_x/2,20, bitmap=bitmaps[i])

def move_right():
    cvs.move(obj, 2, 0)
    
button = Button(root, text='向右移動', command=move_right).pack()

mainloop()
