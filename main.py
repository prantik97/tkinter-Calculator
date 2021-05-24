from tkinter import *


def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root = Tk()
root.geometry("324x657")
root.title("Prantik's Calculator")
root.wm_iconbitmap("Wineass-Ios7-Redesign-Calculator.ico")

scvalue=StringVar()
scvalue.set("")
screen= Entry(root,textvar=scvalue,font="lucida 35 bold").pack(fill=X,ipadx=8,ipady=8,padx=5)

f = Frame(root, bg="white")
b=Button(f,text="9",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="8",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="7",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

f.pack()


f = Frame(root, bg="white")
b=Button(f,text="6",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="5",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="4",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

f.pack()

f = Frame(root, bg="white")
b=Button(f,text="3",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="2",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="1",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

f.pack()

f = Frame(root, bg="white")
b=Button(f,text="0",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="-",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="+",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

f.pack()

f = Frame(root, bg="white")
b=Button(f,text="*",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="/",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="%",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

f.pack()

f = Frame(root, bg="white")
b=Button(f,text="C",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="=",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b=Button(f,text="00",padx=5,pady=5,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

f.pack()

root.mainloop()