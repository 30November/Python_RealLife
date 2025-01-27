import csv
import os
def excel(data):
    if not os.path.exists("student.csv"):
        fw=open("student.csv",mode="a",newline='')
        writepen=csv.writer(fw)
        writepen.writerow(["F. Name","M. Name","L. Name",
                           "Mail","DOB","Sex","Cnt no.","Nationality",
                           "State","City","P.C.","Address",
                           "Phy","Chem","Math","PCM%"]) 
    fw=open("student.csv",mode="a",newline='')   
    writepen=csv.writer(fw)
    writepen.writerow(data)
    fw.close()

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from datetime import datetime


#structure
root=Tk()
root.title("FORM")
root.geometry("850x800+5+5")

#heading
Label(text="STUDENT ADMISSION FORM",font=("Arial",25,"bold"),background="grey").pack(fill=X)

#frame 1,Kaushiki
frm_1=LabelFrame(root,text="NAME SECTION",font=('Arial',12,'italic'))
frm_1.pack(padx=5)
Label(frm_1, text="First name",font=('Times New Roman',18,'bold')).grid(row=1,column=0,padx=5,pady=5)
text1= Entry(frm_1, font=('Cambria',15))
text1.grid(row=2,column=0,padx=5,pady=5)
Label(frm_1, text="Middle name",font=('Times New Roman',18,'bold')).grid(row=1,column=1,padx=5,pady=5)
text2= Entry(frm_1, font=('Cambria',15))
text2.grid(row=2,column=1,padx=5,pady=5)
Label(frm_1, text="Last name",font=('Times New Roman',18,'bold')).grid(row=1, column=2,padx=5,pady=5)
text3= Entry(frm_1, font=('Cambria',15))
text3.grid(row=2,column=2,padx=5,pady=5)


#frame 2,Avisikta

frm_2=Frame(root)
frm_2.pack()

right_frm=Frame(frm_2)
right_frm.pack(side=RIGHT)

l2 = Label(right_frm, text='Gender:', width=20, font=('Times New Roman',18,'bold'))
l2.grid(row=0, column=0, padx=10, pady=10)

rvar = StringVar(right_frm,"Others")
r1 = Radiobutton(right_frm, text='Male',font=("Cambria",15), variable=rvar, value="Male")
r1.grid(row=1, column=0, padx=10)
r2 = Radiobutton(right_frm, text='Female',font=("Cambria",15), variable=rvar, value="Female")
r2.grid(row=2, column=0, padx=10)
r3 = Radiobutton(right_frm, text='Others',font=("Cambria",15), variable=rvar, value="Others")
r3.grid(row=3, column=0, padx=10)

left_frm=Frame(frm_2)
left_frm.pack(side=LEFT)

l=Label(left_frm, text='Date of birth:', width=20, font=('Times New Roman',18,'bold'))
l.grid(row=0, column=0, padx=10, pady=10)
dob = DateEntry(left_frm, width=20, bg="white", fg="black", date_pattern='dd/mm/yyyy',
                borderwidth=3, mindate=datetime(2000, 1, 1), maxdate=datetime(2008, 12, 31))
dob.grid(row=1, column=0, padx=10, pady=10)

#frame 3,ANKIT
frm_3=Frame(root)
frm_3.pack()

label_contact_no = Label(frm_3,font=("Times New Roman",18,"bold") ,text="Contact No:")
label_contact_no.grid(row=0, column=0, padx=5, pady=5)
label_email_id = Label(frm_3,font=("Times New Roman",18,"bold") ,text="Email ID:")
label_email_id.grid(row=0, column=1, padx=5, pady=5)
label_nationality = Label(frm_3,font=("Times New Roman",18,"bold") ,text="Nationality:")
label_nationality.grid(row=0, column=2, padx=5, pady=5)

entry_contact_no = Entry(frm_3,font=("Cambria",15))
entry_contact_no.grid(row=1, column=0, padx=5, pady=5)
entry_email_id = Entry(frm_3,width=30,font=("Cambria",15))
entry_email_id.grid(row=1, column=1, padx=5, pady=5)

entry_nationality = StringVar(frm_3, "Indian")
r1 = Radiobutton(frm_3, text="Indian",font=("Cambria",15), variable=entry_nationality, value="Indian")
r1.grid(row=1, column=2, padx=5, pady=5) 
r2 = Radiobutton(frm_3, text="Others",font=("Cambria",15), variable=entry_nationality, value="Others")
r2.grid(row=2, column=2, padx=5, pady=5) 

def update_widgets():
    mode="disabled"
    if entry_nationality.get() == "Indian":
        entry_contact_no.insert(0,"(+91)")
        mode="!"+mode
    else: 
        entry_state.set(None)
        entry_contact_no.delete(0,END)
    statechoose.config(state=mode)

r1.config(command=update_widgets)  
r2.config(command=update_widgets)
 


label_state = Label(frm_3,font=("Times New Roman",18,"bold") ,text="State:")
label_state.grid(row=3, column=0, padx=5, pady=5)
label_city = Label(frm_3,font=("Times New Roman",18,"bold") ,text="City:")
label_city.grid(row=3, column=1, padx=5, pady=5)
label_pincode = Label(frm_3,font=("Times New Roman",18,"bold") ,text="Pincode:")
label_pincode.grid(row=3, column=2, padx=5, pady=5)

entry_state= StringVar(frm_3,None) 
statechoose = Combobox(frm_3, textvariable = entry_state,font=("Cambria",15))  
statechoose['values'] = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
                         'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh'
                         , 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh',
                         'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                         'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
                         'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
statechoose.grid(row=4, column=0, padx=5, pady=5)
update_widgets() 

entry_city = Entry(frm_3,font=("Cambria",15))
entry_city.grid(row=4, column=1, padx=5, pady=5)

entry_pincode = Entry(frm_3,font=("Cambria",15))
entry_pincode.grid(row=4, column=2, padx=5, pady=5)


label_address = Label(frm_3,font=("Times New Roman",18,"bold") ,text="Address:")
label_address.grid(row=5, column=1, padx=5, pady=5)
text_address = Text(frm_3,width=50,height=2,border=5,font=("Cambria",15))
text_address.grid(row=6,column=0, columnspan=3, padx=5, pady=5)

#frame 4,Me
frm_4=LabelFrame(root,text="CLASS 12 MARKS",font=('Arial',12,'italic'))
frm_4.pack(padx=5)

Label(frm_4,text="Physics",font=('Times New Roman',18,'bold')).grid(row=0,column=0)
Label(frm_4,text="Chemistry",font=('Times New Roman',18,'bold')).grid(row=0,column=1)
Label(frm_4,text="Maths",font=('Times New Roman',18,'bold')).grid(row=0,column=2)

phy=IntVar()
chem=IntVar()
math=IntVar()

Entry(frm_4,textvariable=phy,font=('Cambria',15)).grid(row=1,column=0,pady=10,padx=5)
Entry(frm_4,textvariable=chem,font=('Cambria',15)).grid(row=1,column=1,pady=10,padx=5)
Entry(frm_4,textvariable=math,font=('Cambria',15)).grid(row=1,column=2,pady=10,padx=5)


#submission
def submit():
    name=[text1,text2,text3,entry_email_id]
    contact=[entry_contact_no,entry_nationality,entry_state,entry_city,entry_pincode]
    marks=[phy,chem,math]
    
    stk1=[i.get() for i in name]
    if stk1[0]=="" or stk1[2]=="": return messagebox.showwarning("Message","Please enter your name")
    
    stk2=[k.get() for k in contact if k.get()!=""]
    if len(stk2)!=5: return messagebox.showwarning("Message","Fill you Details Completely")

    stk3=[j.get() for j in marks if 0<=j.get()<=100]
    stk3.append(sum(stk3)/3)
    if len(stk3)!=4: return messagebox.showwarning("Message","Marks range is not Valid")

    address=text_address.get("1.0","end-1c")
    if address=="":return messagebox.showwarning("Message","Address is neccesary")

    data=stk1+[dob.get_date(),rvar.get()]+stk2+[address]+stk3
    option=messagebox.askyesno("Message","Hereby inform, once the form get submitted,\n You can't edit it furthur\n Are you sure to submit?")
    
    if option:excel(data)
    
Button(root,text="SUBMIT",font=("Arial",15),width=20,borderwidth=5,command=submit).pack(pady=5)
root.mainloop()


