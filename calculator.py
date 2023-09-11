# Importing the module
from tkinter  import *

# Naming our tkinter 
calculatorGui = Tk()

# Naming our GUI 
calculatorGui.title("CASIO")
calculatorGui.geometry("570x613")
calculatorGui.wm_iconbitmap("2.ico")
# Locking Maximun & Minimum size 
calculatorGui.minsize(570,600)
calculatorGui.maxsize(570,613)

# Giving GUI background colour
calculatorGui.configure(bg="black")

def click2(event):

      global value

      #getting the button text in a variable
      text2 = event.widget.cget("text")
      if screenValue.get().isdigit():
            int(display.update())
      
      #Formula of square and cube storing in a variable
      square = (float(screenValue.get()) * float(screenValue.get()))
      cube = (float(screenValue.get()) * float(screenValue.get()) * float(screenValue.get()))

      # Square and cube button output
      if text2 == "x²":
            screenValue.set(square)
            
      elif text2 == "x³":
            screenValue.set(cube)
      


def click(event):
      
      global screenValue

      #getting the button text in a variable
      text = event.widget.cget("text")

      if text == "=":
            if screenValue.get().isdigit():
                  value = int(screenValue.get())
            else:
                  try:
                        value = eval(screenValue.get())
                  except Exception as e:
                        value= "ERROR"

            screenValue.set(value)
            display.update()

      # Function behind clear button
      elif text == "C":
            screenValue.set(" ")

      else:
            screenValue.set(str(screenValue.get()) + str(text))
            display.update()

# # Creating Monitor (DISPLAY)
screenValue = StringVar()
screenValue.set(" ")

display = Entry(calculatorGui, textvariable=screenValue, font="arial 38", relief=RIDGE)
display.pack(pady=20)


# Creating Buttons
btns = Button(calculatorGui, text="C", font="arial 20 bold", height=2, width=5, bd=2, fg="white", bg="#3697f5", relief=GROOVE)
btns.place(x=2, y=120)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="%", font="arial 20 bold", height=2, width=5, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=108, y=120)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="x²", font="arial 20 bold", height=2, width=5, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=212, y=120)
btns.bind("<Button-1>", click2)

btns = Button(calculatorGui, text="x³", font="arial 20 bold", height=2, width=5, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=317, y=120)
btns.bind("<Button-1>", click2)

btns = Button(calculatorGui, text="+", font="arial 20 bold", height=2, width=8, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=419, y=120)
btns.bind("<Button-1>", click)

# Button 9,8,7,-
btns = Button(calculatorGui, text="9", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=3, y=220)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="8", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=140, y=220)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="7", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=278, y=220)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="-", font="arial 20 bold", height=2, width=8, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=420, y=220)
btns.bind("<Button-1>", click)

# Button 6,5,4,x
btns = Button(calculatorGui, text="6", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=3, y=320)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="5", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=140, y=320)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="4", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=278, y=320)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="*", font="arial 20 bold", height=2, width=8, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=420, y=320)
btns.bind("<Button-1>", click)

# Button 3,2,1,0,÷,=,.
btns = Button(calculatorGui, text="3", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=3, y=420)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="2", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=140, y=420)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="1", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=278, y=420)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="/", font="arial 20 bold", height=2, width=8, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=420, y=420)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="=", font="arial 20 bold", height=2, width=8, bd=2, fg="black", bg="#87F717", relief=GROOVE)
btns.place(x=420, y=518)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text=".", font="arial 20 bold", height=2, width=7, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=275, y=518)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="0", font="arial 20 bold", height=2, width=15, bd=2, fg="white", bg="#6A6A6A", relief=GROOVE)
btns.place(x=3, y=518)
btns.bind("<Button-1>", click)

calculatorGui.mainloop()