from tkinter import *
from tkinter import messagebox
#print('yash')
root = Tk()
root.geometry('1100x600')
root.config(bg="#3867d6")

w = Label(root,
          text="BroBot",
          padx=(100),
          fg = "#f7f1e3")
w.pack()
w.config(font=("Purisa" ,44, "bold"), bg = "#3867d6")

w1 = Label(root,
           text="Your Digital Assistant",
           padx=(100),
           pady=(0),
           fg = "black")

w1.config(font=("Lobster", 20, "italic"), bg = "#3867d6")
w1.pack()

L1 = Label(root,
           text="BroBot - ",
           font = ("black", 15, "bold"),
           width = (10),
           height = (2),
           bg = "#f1c40f",
           relief = "sunken")
L1.pack(pady=(50)) 
E1 = Label(root,
           width = (80),
           height = (6)) 
E1.pack(pady=(0))

L2 = Label(root,
           text="USER - ",
           font = ("black", 15, "bold"),
           width = (10),
           height = (2),
           bg = "#f1c40f",
           relief = "sunken") 
L2.pack( pady= (50))
E2 = Label(root,
           width = (80),
           height = (6)) 
E2.pack()
print('yash')

def helloCallBack(): 
   msg = messagebox.showinfo( "Exit BroBot", "Are you sure you don't wanna talk anymore?") 

B = Button(root,
           text = "Exit",
           command = helloCallBack,
           font = (40),
           width = (10),
           relief = "raised",
           bg= "#f1c40f",
           cursor = "circle") 
B.pack(side = BOTTOM, pady=(30))


root.mainloop()

