from tkinter import *
import math
import tkinter.messagebox


root= Tk()
root.title("OOP_Project_by_Hammad_Mughees_Arshed")
root.configure(background= "green")
root.resizable(width =False, height =False)
root.geometry("480x675+0+0")


calc= Frame(root)
calc.grid()
class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
    def numberEnter(self, num):
        self.result =False
        firstnum = txtDisplay.get()
        secondnum= str(num)
        if self.input_value:
            self.current= secondnum
            self.input_value =False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)
    def sum_of_total(self):
        self.result =True
        (self.current) =float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total= float(txtDisplay.get())










        


    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="multi":
            self.total*=self.current
        if self.op=="divide":
            self.total/=self.current
        if self.op=="mod":
            self.total%=self.current
        self.input_value= True
        self.check_sum= False
        self.display(self.total)
    def operation(self, op):
        (self.current) =float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
    def clear_entry(self):
        self.result= False
        self.current="0"
        self.display(0)
        self.input_value=True
    def all_Clear_Entry(self):
        self.clear_entry()
        self.total=0
    def mathsPM(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)
    def pi(self):
        self.result+ False
        self.current= math.pi
        self.display (self.current)
    def tau(self):
        self.result+ False
        self.current= math.tau
        self.display (self.current)
    def e(self):
        self.result+ False
        self.current= math.e
        self.display (self.current)
    def tan(self):
        self.result+ False
        self.current= math.tan
        self.display (self.current)
    def cos(self):
        self.result+ False
        self.current= math.cos
        self.display (self.current)
    def sin(self):
        self.result+ False
        self.current= math.sin
        self.display (self.current)
    def squared(self):
        self.result+ False
        self.current= math.sqrt(float(txtDisplay.get()))
        self.display (self.current)
    def cos(self):
        self.result = False
        self.current= math.cos(math.radians(float(txtDisplay.get())))
        self.display (self.current)
    def cosh(self):
        self.result = False
        self.current= math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def sin(self):
        self.result = False
        self.current= math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def sinh(self):
        self.result = False
        self.current= math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def tan(self):
        self.result = False
        self.current= math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def tanh(self):
        self.result = False
        self.current= math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def expm1(self):
            self.result = False
            self.current= math.expm1(float(txtDisplay.get()))
            self.display (self.current)
    def lgamma(self):
        self.result = False
        self.current= math.lgamma(float(txtDisplay.get()))
        self.display(self.current)
    def degrees(self):
        self.result = False
        self.current= math.degrees(float(txtDisplay.get()))
        self.display(self.current)
    def log2(self):
        self.result = False
        self.current= math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def log10(self):
        self.result = False
        self.current= math.log10(float(txtDisplay.get()))
        self.display(self.current)
    def log1p(self):
            self.result = False
            self.current= math.log1p(float(txtDisplay.get()))
            self.display (self.current)
    def radians(self):
        self.result = False
        self.current= math.radians(float(txtDisplay.get()))
        self.display(self.current)
    def exp(self):
        self.result = False
        self.current= math.exp(float(txtDisplay.get()))
        self.display(self.current)
    def Trunc(self):
        self.result = False
        self.current= math.trunc(float(txtDisplay.get()))
        self.display(self.current)
    def ceil(self):
        self.result = False
        self.current= math.ceil(float(txtDisplay.get()))
        self.display(self.current)














added_value = Calc()
txtDisplay=Entry(calc, font=('arial',20,'bold'), bg="brown", bd=22, width=29, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")


numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20,'bold'), bd=4, text= numberpad[i]))
        btn[i].grid(row=j, column =k, pady=1)
        btn[i]["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
        i+=1
#======================================================
btnClear = Button(calc, text=chr(67), width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="red", command = added_value.clear_entry).grid(row=1, column=0, pady=1)
btnallClear = Button(calc, text=chr(67)+ chr(69), width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="red", command = added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)


btnSq = Button(calc, text="sqrt", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.squared).grid(row=1, column=2, pady=1)
btnAdd = Button(calc, text="+", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command= lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)


btnSub = Button(calc, text="-", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = lambda : added_value.operation("sub")).grid(row=2, column=3, pady=1)
btnMult = Button(calc, text="*", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = lambda : added_value.operation("multi")).grid(row=3, column=3, pady=1)
btnDiv = Button(calc, text="/", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = lambda : added_value.operation("divide")).grid(row=4, column=3, pady=1)
btnZero = Button(calc, text="0", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = lambda : added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
btnDot =Button(calc, text=".", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = lambda : added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
btnPM = Button(calc, text="+-", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.mathsPM).grid(row=5, column=2, pady=1)
btnEqual = Button(calc, text="=", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown",command = added_value.sum_of_total).grid(row=5, column=3, pady=1)


#==============================================Scientific==================


btnPi = Button(calc, text="n", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.pi).grid(row=1, column=4, pady=1)
btnCos = Button(calc, text="cos", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.cos).grid(row=1, column=5, pady=1)


btnSin = Button(calc, text="sin", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.sin).grid(row=1, column=6, pady=1)
btntan= Button(calc, text="tan", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.tan).grid(row=1, column=7, pady=1)


#==============================================================
btn2Pi = Button(calc, text="2Pie", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.tau).grid(row=2, column=4, pady=1)
btnacos = Button(calc, text="acos", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.cosh).grid(row=2, column=5, pady=1)
btnasin = Button(calc, text="asin", width=6,height=3, font=('arial', 20,'bold'), bd=4, bg="brown",
                 command = added_value.sinh).grid(row=2, column=6, pady=1)
btnatan = Button(calc, text="atan", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.tanh).grid(row=2, column=7, pady=1)
#==============================================================
btnlog = Button(calc, text="log", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown").grid(row=3, column=4, pady=1)
btnExp = Button(calc, text="Exp", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.exp).grid(row=3, column=5, pady=1)
btnTrunc = Button(calc, text="Trunc", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                bg="brown", command = added_value.Trunc).grid(row=3, column=6, pady=1)
btnE = Button(calc, text="E", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.e).grid(row=3, column=7, pady=1)




#==============================================================
btnlog2 = Button(calc, text="log2", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.log2).grid(row=4, column=4, pady=1)
btndeg = Button(calc, text="deg", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.degrees).grid(row=4, column=5, pady=1)
btnrad = Button(calc, text="rad", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.radians).grid(row=4, column=6, pady=1)
btnceil = Button(calc, text="ceil", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.ceil).grid(row=4, column=7, pady=1)
#=============================================================================
btnlog10 = Button(calc, text="log10", width=6,height=2, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.log10).grid(row=5, column=4, pady=1)
btnlog1p = Button(calc, text="log1p", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.log1p).grid(row=5, column=5, pady=1)
btnexpm1 = Button(calc, text="expm1", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.expm1).grid(row=5, column=6, pady=1)


btngamma = Button(calc, text="gamma", width=6,height=3, font=('arial', 20,'bold'), bd=4,
                  bg="brown", command = added_value.lgamma).grid(row=5, column=7, pady=1)
lblDisplay =Label(calc, text="scientific Calculator", font=('arial', 30, 'bold'), justify = CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)














#=                         menu++and++function            ======


def iExit():
    iExit =tkinter.messagebox.askyesno("scintificCalculator","CONFIRM IF YOU WANT TO EXIT ")
    if iExit > 0:
        root.destroy()
        return
def Scientific():
    root.resizable(width =False, height =False)
    root.geometry("944x668+0+0")
def Standard():
    root.resizable(width =False, height =False)
    root.geometry("480x668+0+0")
    
    
menubar = Menu(calc)


filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label = "Standard", command= Standard )
filemenu.add_command(label = "scintific", command= Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command= iExit)


editmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label="edit", menu=editmenu)
editmenu.add_command(label = "cut")
editmenu.add_command(label = "copy")
editmenu.add_separator()
editmenu.add_command(label = "paste")




helpmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label = "veiwhelp")




root.config(menu=menubar)
root.mainloop()
