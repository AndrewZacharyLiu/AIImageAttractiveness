from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from eye_tracker import track_eye
from threading import *
import io
from PIL import Image, ImageTk
from urllib.request import urlopen
from importRequests import *
import random



gui = tk.Tk()
#gui.geometry("1920x1080")
gui.title("AI-Thing")
gui.resizable(False, False)

my_font = ("Cambria Math", 10, BOLD)

# left_frame = tk.Frame(gui, width = 960, height = 1080, bg = "blue")
# left_frame.grid(row = 0, column = 0, sticky = tk.NSEW)

canvas1 = Canvas(gui, width = 960, height = 1080)  
canvas1.pack(side=tk.LEFT)
canvas2 = Canvas(gui, width = 960, height = 1080)  
canvas2.pack(side=tk.RIGHT)

human_imgs = ["Real/Real/1.jpeg","Real/Real/2.jpeg","Real/Real/3.jpeg","Real/Real/4.jpeg","Real/Real/5.jpeg","Real/Real/6.jpeg","Real/Real/7.jpeg", "Real/Humans_Win.png"]
ai_imgs = ["AI/AI/1.jpeg","AI/AI/2.jpeg","AI/AI/3.jpeg","AI/AI/4.jpeg","AI/AI/5.jpeg","AI/AI/6.jpeg","AI/AI/7.jpeg","AI/AI_Wins.png"]


direction = False
results = []

global img

def load_image(canvas1,canvas2,indx):
    picture=[human_imgs[indx],ai_imgs[indx]]
    rand = random.randrange(0,2)
    if (rand == 1):
        empty=picture[0]
        picture[0]=picture[1]
        picture[1]=empty
    img = ImageTk.PhotoImage(Image.open(picture[0]))
    canvas1.create_image(240,540, anchor=W, image=img) 
    canvas1.image = img

    img = ImageTk.PhotoImage(Image.open(picture[1]))
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
        winner = "AI win"
        img = ImageTk.PhotoImage(Image.open(ai_imgs[7]))
        canvas1.create_image(240,540, anchor=W, image=img) 
        canvas1.image = img

        canvas2.create_image(240,540, anchor=W, image=img) 
        canvas2.image = img
    elif left > right:
        winner = "Humans wins"
        img = ImageTk.PhotoImage(Image.open(human_imgs[7]))
        canvas1.create_image(240,540, anchor=W, image=img) 
        canvas1.image = img

        canvas2.create_image(240,540, anchor=W, image=img) 
        canvas2.image = img
    else:
        winner = "Tie"
    print(winner)
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


