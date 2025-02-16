from tkinter import*
from tkinter import messagebox
import ast
from tkinter import ttk
root=Tk()
root.title('login')
root.geometry('950x500+300+200')
root.resizable(0,0)
null=0
ref=[]

######################################################################################################

def login():
    Username=User.get()
    Password=code.get()
   
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
 ##########################################################################################################    
  
    def leave_command():
        windows=Tk()
        windows.title('Sign up')
        windows.geometry('950x500+300+200')   
        windows.configure(bg='#fff')
        windows.resizable(0,0) 
        def getvals(*args):
            my_flag=False
            for str in reasonentry:
                if(len(str.get())<3):
                    my_flag=True
                if(my_flag==False):
                    messagebox.showerror("please enter valid")
                    
            #if reasonentry == null:
                #messagebox.showerror("please enter valid")
                else:
                    messagebox.showinfo("message","sent successfully")
            

        Label(windows,text='LEAVE REQUEST FORM',font="ar 15 bold",bg="white").grid(row=0,column=4)


        name=Label(windows,text="NAME",bg="white")
        name.grid(row=1,column=30)
        namevalue=StringVar
        nameentry=Entry(windows,textvariable_=namevalue)
        nameentry.grid(row=1,column=35)

        spr=Label(windows,text="SPR NO",bg="white")
        spr.grid(row=2,column=30)
        sprvalue=StringVar
        sprentry=Entry(windows,textvariable=sprvalue)
        sprentry.grid(row=2,column=35)


        option3=["CSE-A",
                 "CSE-B",
                 "MECH",
                 "CIVIL",
                 "ECE",
                 "EEE"
            ]
        dep=Label(windows,text="DEPARTMENT",bg="white")
        dep.grid(row=3,column=30)
        tik=ttk.Combobox(windows,value=option3,cursor='hand2')
        tik.grid(row=3,column=35)
        
        option=["MALE",
                "FEMALE"
            ]
            
        label=Label(windows,text="GENDER",bg="white")
        label.grid(row=4,column=30)
        combo_box=ttk.Combobox(windows,value=option,cursor='hand2')
        
        combo_box.grid(row=4,column=35)
        
        option2=["1",
                 "2",
                 "3"
                 ,"4"
                 ,"5"
            ]
        gig=Label(windows,text="NO.OF DAYS",bg="white")
        gig.grid(row=6,column=30)
        leave=ttk.Combobox(windows,value=option2,cursor='hand2')
     
        leave.grid(row=6,column=35)


        reason=Label(windows,text="REASON",bg="white")
        reason.grid(row=7,column=30)
        reasonvalue=StringVar
        reasonentry=Entry(windows,textvariable=reasonvalue)
        reasonentry.grid(row=7,column=35)
        #ref.append(reasonentry)
        

        
        Button(windows,text="SUMMIT",command=getvals,cursor='hand2').grid(row=11,column=35)

        windows.mainloop()

    if Username in r.keys() and Password==r[Username]:
        
        leave_command()
       
    else:
        messagebox.showerror('invalid','invalid username or password')
    
    


###############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Signup_command():
      windows=Toplevel(root)
      windows.title('Sign up')
      windows.geometry('950x500+300+200')   
      windows.configure(bg='#fff')
      windows.resizable(0,0) 

      def Signup():
          Username=User.get()
          Password=code.get()
          conform_password=conform_code.get()

          if Password==conform_password:
             try:
                  file=open('datasheet.txt','r+')
                  d=file.read()
                  r=ast.literal_eval(d)

                  dict2={Username:Password}
                  r.update(dict2)
                  file.truncate(0)
                  file.close()
                  file=open('datasheet.txt','w')
                  w=file.write(str(r))
                  messagebox.showinfo('singnup','successful signup')
                  windows.destroy()
             except:
                   file=open('datasheet.txt','w')
                   pp=str({'Username':'password'})
                   file.write(pp)
                   file.close()



          else:             messagebox.showerror('invalid',"both password should match")

      def sign():
          windows.destroy()



      #img=PhotoImage(file="C:\\cse\\hi.png")
      #Label(windows,image=img,border=0,bg='white').place(x=50,y=90)
      frame=Frame(windows,width=350,height=390,bg="white")
      frame.place(x=480,y=70)
      heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
      heading.place(x=100,y=5)
###########------------------------------------------------------------------------------------------------
      def on_enter(e):
          User.delete(0,'end')
      def on_leave(e):
          if User.get()=='':
             User.insert(0,'UserName')
      User=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
      User.place(x=30,y=80)
      User.insert(0,'UserName')
      User.bind("<FocusIn>",on_enter)
      User.bind("<FocusOut>",on_leave)
      Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
#############------------------------------------------------------------------------------------------
      def on_enter(e):
          code.delete(0,'end')
      def on_leave(e):
          if code.get()=='':
              code.insert(0,'Password')
      code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
      code.place(x=30,y=150)
      code.insert(0,'password')
      code.bind("<FocusIn>",on_enter)
      code.bind("<FocusOut>",on_leave)
      Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

##############--------------------------------------------------------------------------------------------
      def on_enter(e):
          conform_code.delete(0,'end')
      def on_leave(e):
          if conform_code.get()=='':
              conform_code.insert(0,'Conform Password')

      conform_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
      conform_code.place(x=30,y=220)
      conform_code.insert(0,'Conform Password')
      conform_code.bind("<FocusIn>",on_enter)
      conform_code.bind("<FocusOut>",on_leave)
      Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)
#-----------------------------------------------------------------------------------------------------------
      Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=Signup).place(x=35,y=280)
      lable=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
      lable.place(x=90,y=340)
      signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
      signin.place(x=200,y=340)
      windows.mainloop()
###############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
            

##img=PhotoImage(file="C:\\cse\\hi.png")
#Label(root,image=img,border=0,bg='white').place(x=50,y=90)
frame=Frame(root,width=350,height=390,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
###########------------------------------------------------------------------------------------------------
def on_enter(e):
    User.delete(0,'end')
def on_leave(e):
    if User.get()=='':
        User.insert(0,'UserName')
User=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
User.place(x=30,y=80)
User.insert(0,'UserName')
User.bind("<FocusIn>",on_enter)
User.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
#############--------------------------------------------------------------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

##############------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Login',bg='#57a1f8',fg='white',border=0,command=login).place(x=35,y=280)
lable=Label(frame,text="I don't have an account",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
lable.place(x=90,y=340)
Sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=Signup_command)
Sign_up.place(x=230,y=340)
root.mainloop()
