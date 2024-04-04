import tkinter as tk
from PIL import Image



#This is the first
root = tk.Tk()
file = "gifs\\i5.gif"

info = Image.open(file)
frames = info.n_frames
im = [tk.PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]



count =0
anim = None


def animation(count):
    global anim
    im2 = im[count]
    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 1
    anim = root.after(80, lambda: animation(count))



def stop_anim():
    root.after_cancel(anim)

gif_label = tk.Label(image="")
gif_label.pack()

start = tk.Button(text="start", command=lambda:animation(count))
start.pack()
stop = tk.Button(text="stop", command=stop_anim)
stop.pack()

root.mainloop()