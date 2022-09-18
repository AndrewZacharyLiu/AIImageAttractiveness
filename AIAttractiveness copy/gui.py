from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from eye_tracker import track_eye
from threading import *
import io
from PIL import Image, ImageTk
from urllib.request import urlopen
from importRequests import *



gui = tk.Tk()
#gui.geometry("1920x1080")
gui.title("AI-Thing")
gui.resizable(False, False)

my_font = ("Cambria Math", 10, BOLD)

# left_frame = tk.Frame(gui, width = 960, height = 1080, bg = "blue")
# left_frame.grid(row = 0, column = 0, sticky = tk.NSEW)

canvas1 = Canvas(gui, width = 960, height = 1080)  
canvas1.pack(side=tk.LEFT)
canvas2 = Canvas(gui, width = 960, height = 1080, bg="red")  
canvas2.pack(side=tk.RIGHT)

human_imgs = ["cat.png","cat.png","cat.png","cat.png","cat.png","cat.png","cat.png"]
ai_imgs = ["cat.png","cat.png","cat.png","cat.png","cat.png","cat.png","cat.png"]

direction = False
results = []

global img

def load_image(canvas1,canvas2,indx):
    img = ImageTk.PhotoImage(Image.open(human_imgs[indx]))
    canvas1.create_image(240,540, anchor=W, image=img) 
    canvas1.image = img

    img = ImageTk.PhotoImage(Image.open(ai_imgs[indx]))
    canvas2.create_image(480,540, anchor=CENTER, image=img) 
    canvas2.image = img

    
    
def track():
    track_eye(direction,results)
    right = 0
    left = 0
    for i in results:
        if i:
            right+=1
        else:
            left+=1
    print((left,right))
    if left > right:
        results.append(False)
    else:
        results.append(True)
def find_winner():
    right = 0
    left = 0
    for i in results:
        if i:
            right+=1
        else:
            left+=1
    if right > left:
        print("Right")
    elif left > right:
        print("Left")
    else:
        print("Tie")
def cycle():
    for i in range(0,7):
        load_image(canvas1,canvas2,i)
        track()
    find_winner()
def threading():
    t1 = Thread(target=cycle)
    t1.start()
def main():
    threading()
    gui.mainloop()


if __name__ == "__main__":
    main()


