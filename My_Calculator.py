from tkinter import *

def add (n1,n2):
    return n1+n2
def subtract (n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide (n1,n2):
    if n2==0:
        return "ERROR"
    return n1/n2

def update_entry(value):
    current_text = entry.get()  # Get the current text in the entry widget
    entry.delete(0, END)  # Clear the entry widget
    entry.insert(END, current_text + str(value))  # Insert the new value

def equalsto():
    present_text = entry.get()
    for i in present_text:
        if i in ['+', '-', '*', '/']:  # Check if i is any of the operators
            operator_index = present_text.index(i)
            n1 = present_text[:operator_index]
            n2 = present_text[operator_index + 1:]
            if i == '+':
                entry.delete(0, END)  # Clear the entry widget
                entry.insert(END, add(int(n1), int(n2)))
            elif i == '-':
                entry.delete(0, END)  # Clear the entry widget
                entry.insert(END, subtract(int(n1), int(n2)))
            elif i =='*':
                entry.delete(0, END)  # Clear the entry widget
                entry.insert(END, multiply(int(n1), int(n2)))
            else:
                entry.delete(0, END)  # Clear the entry widget
                entry.insert(END, divide(int(n1), int(n2)))

def reset():
    entry.delete(0, END)  # Clear the entry widget


root = Tk()
root.geometry("450x375")
root.title("My Calculator")
entry = Entry(root)
entry.grid(ipadx=163, ipady=25)

frame0 = Frame(root, borderwidth=4, bg="purple")
a = Button(frame0, fg="black", text="9", command=lambda t=9: update_entry(t))
a.grid(row=1, column=1, ipadx=60, ipady=12, padx=4)
b = Button(frame0, fg="black", text="8", command=lambda t=8: update_entry(t))
b.grid(row=1, column=2, ipadx=60, ipady=12, padx=4)
c = Button(frame0, fg="black", text="7", command=lambda t=7: update_entry(t))
c.grid(row=1, column=3, ipadx=60, ipady=12,padx=4)

d = Button(frame0, fg="black", text="6", command=lambda t=6: update_entry(t))
d.grid(row=2, column=1, ipadx=60, ipady=12, padx=4)
e = Button(frame0, fg="black", text="5", command=lambda t=5: update_entry(t))
e.grid(row=2, column=2, ipadx=60, ipady=12, padx=4)
f = Button(frame0, fg="black", text="4", command=lambda t=4: update_entry(t))
f.grid(row=2, column=3, ipadx=60, ipady=12, padx=4)

g = Button(frame0, fg="black", text="3", command=lambda t=3: update_entry(t))
g.grid(row=3, column=1, ipadx=60, ipady=12, padx=4)
h = Button(frame0, fg="black", text="2", command=lambda t=2: update_entry(t))
h.grid(row=3, column=2, ipadx=60, ipady=12, padx=4)
i = Button(frame0, fg="black", text="1", command=lambda t=1: update_entry(t))
i.grid(row=3, column=3, ipadx=60, ipady=12, padx=4)

j = Button(frame0, fg="black", text="+", command=lambda t="+": update_entry(t))
j.grid(row=4, column=1, ipadx=59, ipady=12, padx=4)
k = Button(frame0, fg="black", text="0", command=lambda t=0: update_entry(t))
k.grid(row=4, column=2, ipadx=60, ipady=12, padx=4)
l = Button(frame0, fg="black", text="=", command=lambda t="=": equalsto())
l.grid(row=4, column=3, ipadx=59, ipady=12, padx=4)

m = Button(frame0, fg="black", text="-", command=lambda t="-": update_entry(t))
m.grid(row=5, column=1, ipadx=61, ipady=12, padx=4)
n = Button(frame0, fg="black", text="/", command=lambda t="/": update_entry(t))
n.grid(row=5, column=2, ipadx=60, ipady=12, padx=4)
o = Button(frame0, fg="black", text="*", command=lambda t="*": update_entry(t))
o.grid(row=5, column=3, ipadx=60, ipady=12, padx=4)

p = Button(frame0, fg="black", text="00", command=lambda t="00": update_entry(t))
p.grid(row=6, column=1, ipadx=58, ipady=12, padx=4)
q = Button(frame0, fg="black", text="C", command=lambda: reset())
q.grid(row=6, column=2, ipadx=59, ipady=12, padx=4)
r = Button(frame0, fg="black", text="000", command=lambda t="000": update_entry(t))
r.grid(row=6, column=3, ipadx=54, ipady=12, padx=4)

frame0.grid(columnspan=3, rowspan=6)

root.mainloop()
