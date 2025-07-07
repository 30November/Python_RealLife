from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
# import bar

class makaut:
    def __init__(self, root):
        self.root = root
        self.data={}
        self.rule={"O":10,"E":9,"A":8,"B":7,"C":6,"D":5}

        # Create a dept
        self.dept = LabelFrame(root,text="DEPARTMENT",font=(18))
        self.dept.pack(padx=10, pady=10)
        Button(self.dept, text="COMP", font=("Cambria",15),command=self.sms_cse).grid(pady=5,padx=5,row=0,column=0)
        Button(self.dept, text="ECE", font=("Cambria",15),command=self.sms_ece).grid(pady=5,padx=5,row=0,column=1)
        Button(self.dept, text="1st YEAR", font=("Cambria",15),command=self.first_year).grid(pady=5,padx=5,row=0,column=2)

        # Create a semester
        self.semester = LabelFrame(root,text="SEMESTER",font=(18))
        self.semester.pack(padx=10, pady=10)

        # Create a marks
        self.marks = LabelFrame(root,text="MARKS",font=(18))
        self.marks.pack(padx=10, pady=10)

        # Calulator
        Button(self.root,text="CGPA",command=self.cal).pack()
        # Answer
        self.calc=Label(self.root,text="",font=("Arial",18,"bold"))
        self.calc.pack()

    def widget_destroy(self,frm):
        for wid in frm.winfo_children():
            wid.destroy()

    def widget(self,credit):
        self.data.clear()
        cp=rp=0
        for item in credit:
            self.data[item]=[credit[item],StringVar()]
            Label(self.marks,text=item).grid(row=rp,column=cp)
            Combobox(self.marks,textvariable=self.data[item][1],
                        values=['O', 'E', 'A', 'B', 'C', 'D']).grid(row=rp+1,column=cp,padx=5,pady=5)
            
            if not (cp:=(cp+1)%3): rp+=2

    def first_year(self): #1st
        self.widget_destroy(self.semester)
        self.widget_destroy(self.marks)

        def sms1():
            self.widget_destroy(self.marks)
            credit={"MATH":4,"PHY/CHEM":4,"Elec.":4,
                    "PHY/CHEM(LAB)":1.5,"WORKSHOP/DRAW":3,
                    "Elec(LAB)":1}
            self.widget(credit)
        
        def sms2():
            self.widget_destroy(self.marks)
            credit={"MATH":4,"PHY/CHEM":4,"C-PROM":3,
                    "ENG":2,"WORKSHOP/DRAW":3,
                    "C-PROM(LAB):":2,"PHY/CHEM(LAB)":1.5,
                    "ENG(LAB)":1}
            self.widget(credit)


        Button(self.semester,text="SMS 1",font=("Cambria",15),
               command=sms1).grid(row=0,column=0,padx=5)
        Button(self.semester,text="SMS 2",font=("Cambria",15),
               command=sms2).grid(row=0,column=1,padx=5)
    
    def sms_cse(self): #CSE
        self.widget_destroy(self.semester)
        self.widget_destroy(self.marks)

        def sms3():
            self.widget_destroy(self.marks)
            credit={"MATH":2,"DSA":3,"ECO":3,
                    "CO":3,"ANA&DIGI":3,
                    "DSA(LAB):":2,"CO(LAB)":2,
                    "ANA&DIGI(LAB)":2,"PYTHON":2}
            self.widget(credit)

        def sms4():
            self.widget_destroy(self.marks)
            credit={"MATH":4,"DAA":3,"AUTO":3,
                    "BIO":3,"CA":3,"EVS":1,
                    "DAA(LAB):":2,"CA(LAB)":2}
            self.widget(credit)

        Button(self.semester,text="SMS 3",font=("Cambria",15),
               command=sms3).grid(row=0,column=0,padx=5)
        Button(self.semester,text="SMS 4",font=("Cambria",15),
               command=sms4).grid(row=0,column=1,padx=5)
      
    def sms_ece(self): #ECE
        self.widget_destroy(self.semester)
        self.widget_destroy(self.marks)
        
        def sms4():
            self.widget_destroy(self.marks)
            credit={"Analog Com":3,"DAA":3,"Analog Elec.":3,
                    "BIO":3,"Micro":3,"Num":2,
                    "Analog Com(LAB):":1,"Analog Elec.(LAB)":1,
                    "Micro(LAB)":1,"Num(LAB)":1,"Soft Skill":1}
            self.widget(credit)
        
        def sms3():
            self.widget_destroy(self.marks)
            credit={}
            self.widget(credit)

        Button(self.semester,text="SMS 3",font=('Cambria',15),
               command=sms3).pack()
        Button(self.semester,text="SMS 4",font=('Cambria',15),
               command=sms4).pack()

    def cal(self):
        ans=total=0
        try:
            for i in self.data:
                ans += (self.rule[self.data[i][1].get()]*self.data[i][0])
                total += self.data[i][0]
        
            self.calc.config(text=str(round(ans/total,2)))
        except:
            messagebox.showerror("ERROR","Few subject's Grade neither assign nor valid!!❌")


if __name__ == "__main__":
    root = Tk()
    root.title("CPGA Calculator")
    Label(root,text="CGPA Prediction",font=("Helvetica",30, "bold"),fg="#0059b3", bg="#f0f8ff").pack(side=TOP)
    makaut(root)
    root.mainloop()
