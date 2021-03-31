from tkinter import Tk , Button , TOP
from pynput.keyboard import Key , Controller
import time

x = Tk()
x.title("Spammer by ksh")
x.geometry("200x110")
x.resizable(False , False)




Keyboard = Controller()

def spammer():
   time.sleep(3)
   
   for i in range(100) :
      Keyboard.type("salam")
      Keyboard.press(Key.enter)
      Keyboard.release(Key.enter)



button1 = Button( x , height = 2 , width = 4  ,text = "start" , command = spammer)
button1.pack(side = TOP)

x.mainloop()
