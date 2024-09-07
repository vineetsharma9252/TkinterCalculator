from tkinter import * 
import tkinter.messagebox as tmg 
import numpy as np 
class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
    def Label(self, fr , text , bg , r ,c ):
        self.L = Label(fr, text=text ,bg = bg).grid(row=r , column=c)
    def Fields(self ,fr,r , c , x = 0 , y = 0):
        self.var= StringVar()
        self.var1value=Entry(fr, textvariable=self.var,width=50,highlightbackground='red',highlightcolor='red').grid(row= r , column=c,padx=x , pady=y)
        return self.var
    def factorial(self  , n):
        fact = 1 
        for i in range(1 , n+1):
            fact = fact*i
        return fact
    def Add(self,f1 , f2 , f3):
        ans = int(f1.get())+int(f2.get())
        print(ans)
        f3.set(str(ans)+"                          O(+)")
    def Subtraction(self , f1 , f2,f3):
        ans =int(f1.get()) - int(f2.get())
        print(ans)
        f3.set(str(ans)+"                          O(-)")
    def Divide(self , f1 , f2,f3):
        ans = int(f1.get())/int(f2.get())
        print(ans)
        f3.set(str(ans)+"                          O(/)")
    def Multiply(self,f1, f2,f3):
        if f1.get() == '' or f2.get() == '':
            tmg.askretrycancel("ValueInsert","Insert Values in both for multiplication")
        ans = int(f1.get())*int(f2.get())
        print(ans)
        f3.set(str(ans)+"                          O(X)")
    def cos(self , f1,f3):
        ans = np.cos(int(f1.get()))
        print(ans)
        f3.set(str(ans)+"                          O(cos)")
    def Combination(self , f1 , f2,f3):
        n= int(f1.get())
        r = int(f2.get())
        ans=self.factorial(n)/(self.factorial(n-r)*self.factorial(r))
        print(ans)
        f3.set(str(ans)+"                          O(nCr)")
    def Permutation(self , f1 , f2,f3):
        n = int(f1.get())
        r = int(f2.get())
        ans = self.factorial(n)/(self.factorial(n-r))
        f3.set(str(ans)+"                          O(nPr)")
    def LogE(self , f1 , f2,f3):
        if f1.get()=='' and f2.get()=='':
            tmg.askretrycancel("ValueInsert","Insert value in one the box or both")
        elif f2.get()=='' and f1.get()!='':
            ans = np.log(int(f1.get()))
            print(ans)
            f3.set(str(ans)+"                          O(ln)")
        elif f1.get() =='' and f2.get()!='':
            ans = np.log(int(f2.get()))
            f3.set(str(ans)+"                          O(ln)")
        else:
            ans = str(np.log(int(f1.get())))+"    "+str(np.log(int(f2.get())))
            print(ans)
            f3.set(str(ans)+"                          O(ln)")
    def tan(self, f1,f3):
        ans = np.tan(int(f1.get()))
        print(ans)
        f3.set(str(ans)+"                          O(tan)")
    def sin(self, f1,f3):
        ans = np.sin(int(f1.get()))
        print(ans)
        f3.set(str(ans)+"                          O(sin)")
    def sinc(self ,f1,f3):
        ans = np.sinc(float(f1.get()))
        print(ans)
        f3.set(str(ans)+"                          O(sin-1)")
    def log10(self , f1 , f2,f3):
        if f1.get()=='' and f2.get()=='':
            tmg.askretrycancel("ValueInsert","Insert value in one the box or both")
        elif f2.get()=='' and f1.get()!='':
            ans = np.log10(int(f1.get()))
            f3.set(str(ans)+"  O(log10)")
            print(ans)
        elif f1.get() =='' and f2.get()!='':
            ans = np.log10(int(f2.get()))
            f3.set(str(ans)+"    O(log10)")
            print(np.log10(int(f2.get())))
        else:
            ans = str((np.log10(int(f1.get()))))+" "+str((np.log10(int(f2.get()))))+"O(log10)"
            f3.set(ans)
            print(ans)
    def fact(self , f1,f3):
        if int(f1.get()) > 50:
            tmg.askretrycancel("RangeError","Please Enter the value < 50 for factorial")
        ans = self.factorial(int(f1.get()))
        f3.set(str(ans)+"                          O(!)")
        print(ans)
    def e(self , f1,f3):
        ans = np.e**int(f1.get()) if f1.get()!='' else np.e**int(f2.get())
        print(ans)
        f3.set(str(ans)+"                          O(e^)")
    def ebut(self):return np.e
    def fraction(self , f1,f3): 
        ans=1/int(f1.get()) 
        print(ans)
        f3.set(str(ans)+"                          O(1/x)")
    def twoexpo(self ,f1,f3):
        ans = 2**int(f1.get())
        f3.set(str(ans)+"                          O(2^x)")
        print(ans)
    def expo(self , f1 , f2,f3):
        ans = int(f1.get())**int(f2.get()) 
        f3.set(str(ans)+"                          O(x^y)")
        print(ans)
    def frame(self , x , y, bg,bw):
        return Frame(self , bg=bg ,borderwidth=bw ,padx=x,pady=y)
    def buttons(self ,fr , r ,c , text , command,x , y , pd=0 ,py=0):
        Button(fr,text=text,command=command,padx=pd , pady=py,bg='black',fg='white').grid(row=r , column=c ,padx=x , pady=y)
if __name__ == '__main__':
    calc = Calculator()
    calc.geometry("800x700")
    calc.minsize(800,700)
    calc.maxsize(800,700) # can set size upto 800x600
    frame_inputs = calc.frame(80,15, "orange",5) # makes a frame of padx = 80 pady= 15 bg = orange , borderwidth = 5 
    frame_inputs.grid(row=2,column=1) # sets frame_input place to row =2 and column = 1 in the grid
    frame_instructions = calc.frame(10,10 , 'blue',5)
    frame_instructions.grid(row=3,column=0)
    calc.Label(frame_inputs,"Answer is  ","blue",2,0) # Makes a Label inside frame_inputs with text "Answer is" bg ="blue" with padx=2  and pady = 0
    f3 = calc.Fields(frame_inputs,2,1 , 20 , 20) # Makes a Field in frame_inputs with row = 2 column =1 in the grid with padx = 20 and pady = 20 
    calc.Label(frame_inputs ,"Enter the first number","green",0 , 0)
    f1 = calc.Fields(frame_inputs,0, 1 ,100, 30)
    calc.Label(frame_inputs, "Enter the second number",'red',1,0)
    frame_buttons= calc.frame(24 , 32 , 'grey',6)
    frame_buttons.grid(row=4,column=1)
    f2 = calc.Fields(frame_inputs, 1, 1 ,100 , 30)
    #Operational buttons 
    calc.buttons(frame_buttons ,3 ,1, "+" ,lambda:calc.Add(f1 , f2,f3) , 10 , 10,10 , 10) # makes a button inside the frame_buttons Frame with row = 3 column = 1 and text="+" commading Add() munipulatig 3 fields  
    calc.buttons(frame_buttons , 4 , 1 , " - ",lambda:calc.Subtraction(f1 , f2,f3) , 10, 10,10,10)
    calc.buttons(frame_buttons , 5 , 1 , " / " , lambda:calc.Divide(f1 , f2,f3),10 , 10,10,10)
    calc.buttons(frame_buttons,6,1 , " * ",lambda:calc.Multiply(f1 , f2,f3),10, 10,10,10)
    calc.buttons(frame_buttons, 7,1 , " ! ",lambda:calc.fact(f1,f3) , 10 , 10 ,10,10)
    calc.buttons(frame_buttons , 8 , 1 , "Lg10",lambda:calc.log10(f1 , f2,f3),10,10,5,10)
    calc.buttons(frame_buttons , 3 , 2 , "nCr",lambda:calc.Combination(f1 , f2,f3) , 10 , 10 ,6,10)
    calc.buttons(frame_buttons, 4 , 2 , "nPr",lambda:calc.Permutation(f1 , f2,f3) , 10 , 10 ,7,10)
    calc.buttons(frame_buttons, 5 , 2 ,"ln",lambda:calc.LogE(f1, f2,f3),10 , 10,10,10 )
    calc.buttons(frame_buttons, 6,2 ,"Sin",lambda:calc.sin(f1,f3),10 , 10,6,10 )
    calc.buttons(frame_buttons,7,2,"Sin-1",lambda:calc.sinc(f1,f3) , 10,10,3,10)
    calc.buttons(frame_buttons, 8,2 ,"Cos",lambda:calc.cos(f1,f3),10 , 10,6,10 )
    calc.buttons(frame_buttons ,3,3 , "tan",lambda:calc.tan(f1,f3),10,10,6,10)
    calc.buttons(frame_buttons,4,3 , 'e^x',lambda:calc.e(f1,f3),10 ,10 , 6 , 10)
    calc.buttons(frame_buttons,5,3,'x^y',lambda:calc.expo(f1 , f2,f3),10,10,6,10 )
    calc.buttons(frame_buttons,6,3,'2^x',lambda:calc.twoexpo(f1,f3),10,10,6,10 )
    calc.buttons(frame_buttons,7,3,'1/x',lambda:calc.fraction(f1,f3),10,10,6,10 )
    calc.buttons(frame_buttons,8,3,'e',lambda:calc.ebut(),10,10,12,10 )
    calc.mainloop()