import tkinter

# variablen
i = 0

# def events

def handleButton(event):
     global i 
     i = i + 1
     w['text'] = "Count >> " + str(i)

def handleButton_2(event):
     global i 
     i = i - 1
     w['text'] = "Count >> " + str(i)

def handleButton_3(event):
     global i 
     i = i * 2
     w['text'] = "Count >> " + str(i)

# visible area

top = tkinter.Tk()

w = tkinter.Label(top,text='Press button...')
w.pack() 

b = tkinter.Button(top,text="+")
b.pack()

b_2 = tkinter.Button(top,text="-")
b_2.pack()

b_3 = tkinter.Button(top,text="Verdoppeln")
b_3.pack()

a = tkinter.Label(top,text='by Robieo')
a.pack() 

# Verweis auf Event

b.bind('<Button-1>', handleButton)
b_2.bind('<Button-1>', handleButton_2)
b_3.bind('<Button-1>', handleButton_3)


top.mainloop()



