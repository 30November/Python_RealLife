from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

# from backend_calculator import calculator

root=Tk()
root.title("CALCULATOR")
Label(root,text="calculator".upper(),font=("Swis721 BlkEx BT",20),background="black",foreground="white").pack()

#upper frame
upfrm=LabelFrame(root,text="Expression")
upfrm.pack()

exp=StringVar()
box=Entry(upfrm,textvariable=exp,width=30)
box.pack(padx=5,pady=5)


#middle frame
mainfrm=Frame(root)
mainfrm.pack(padx=5,pady=5)

symbol=[[7,8,9,'(',')'],
        [4,5,6,"/","x"],
        [1,2,3,"+","-"],
        [0,'.','^',"DEL","CLR"]]

data={}

for i in range (4): #3
    for j in range (5): #5
        lbl=symbol[i][j]
        def action(x=lbl):  
            return box.insert(END,x) 

        # create the buttons  
        data[lbl] = Button(mainfrm, text = lbl,width=5 ,command = action) 
        data[lbl].grid(row=i,column=j,padx=2,pady=2)

def delete():
    s=exp.get()
    exp.set(s[:-1])   
    
def clear():box.delete(0,END)

data["DEL"].config(command=delete)
data["CLR"].config(command=clear)

#low frame
low_frm=Frame(root)
low_frm.pack()

def ans():
    try:
        s=list(exp.get())
        for i in range (len(s)):
            if s[i]=='x':s[i]='*'
            if s[i]=='^':s[i]='**'
        value=eval(''.join(s))
        _.config(text=value)
        
    except ZeroDivisionError:
        messagebox.showerror("Message","Can't Divide by 0")
    except:
        messagebox.showerror("Message","Invalid Expression")

Button(low_frm,text="ANSWER",width=20,command=ans).pack()
_=Label(low_frm,text="",font=("Arial",18))
_.pack()  
#continuous
root.mainloop()