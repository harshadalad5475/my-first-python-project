from tkinter import *

root = Tk()
root.title("Drawing App")
root.geometry("800x600")

canvas = Canvas(root, bg="white", width=800, height=550)
canvas.pack()

last_x = None
last_y = None

def start_draw(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y,
                           fill="black", width=3,
                           capstyle=ROUND, smooth=True)

    last_x = event.x
    last_y = event.y

def stop_draw(event):
    global last_x, last_y
    last_x = None
    last_y = None

def clear_canvas():
    canvas.delete("all")

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

Button(root, text="Clear", command=clear_canvas,
       font=("Arial", 12)).pack(pady=10)


root.mainloop()