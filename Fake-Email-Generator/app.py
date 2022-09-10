from  tkinter import *
from  tkinter import  ttk
from tkinter import filedialog
from tkinter import messagebox
from guerrillamail import GuerrillaMailSession
from threading import Thread
from time import strftime
def submit():
    start_function=Thread(target=email_generator_function)
    start_function.start()
def email_generator_function():
    try:
        list1.delete(0, END)
        num_email = (data_select.get())
        if num_email == 'SELECT':
            messagebox.showinfo(title='info', message=f'\n  | Select Number Email | ')
        else:
            messagebox.showinfo(title='info', message=f'\n  | Selected Successfully | ')
            prog = ttk.Progressbar(Frame3, orient=HORIZONTAL, length=885)
            prog.place(x=10, y=655)
        n = 0
        while n < int(num_email):
            session = GuerrillaMailSession()
            email_list = (session.get_session_state()['email_address'])
            list1.insert(n, f'Email {n + 1} : {email_list}')
            n += 1
            prog.config(value=n, maximum=int(num_email))
            Frame3.update()
    except:pass
root=Tk()
root.geometry("1200x800")
root.config(bg="#3d0b0b")
root.title('Fake Email Generator')
root.resizable(0,0)
#=======================  Frame 1  ===============================
Frame1=Frame(root,width=300,height=800,bg="#000000")
Frame1.place(x=0,y=0)
# logo
logo_path=PhotoImage(file="img/logo.png")
Label_logo=Label(Frame1,image=logo_path,bg="#000000").place(x=4,y=60)
# button generator
Button_generator=Button(Frame1,text='generator',fg="#000000",bg='#5ce1e6',width=20,height=2,border=2).place(x=66,y=350)
# button setting
Button_setting=Button(Frame1,text='setting',fg="#000000",bg='#5ce1e6',width=20,height=2,border=2).place(x=66,y=500)
# button exit
Button_exit=Button(Frame1,text='exit',fg="#000000",bg='#5ce1e6',width=20,height=2,border=2, command=lambda: [root.destroy()]).place(x=66,y=650)
# label time
def time():
	string = strftime('%H:%M:%S %p')
	lbl_time.config(text = string)
	lbl_time.after(1000, time)
lbl_time = Label(Frame1, font = ('calibri', 20, 'bold'),
			background = '#000000',
			foreground = 'white')
lbl_time.place(x=60,y=250)
time()
#=======================  Frame 2  ===============================
Frame2=Frame(root,width=900,height=120,bg="#5ce1e6")
Frame2.place(x=300,y=0)
# Label_fake_email_generator
Label_titel=Label(Frame2,text='Fake Email Generator ',bg="#5ce1e6",fg="#000000",font=('calibri',40)).place(x=150,y=20)
#=======================  Frame 3  ===============================
Frame3=Frame(root,width=1000,height=670,bg="#3d0b0b")
Frame3.place(x=300,y=120)
# button SUBMIT
Button_SUBMIT=Button(Frame3,text='SUBMIT',bg="#3d0b0b",fg='white',width=15,height=1,border=2,anchor="center",command=submit).place(x=500,y=50)
# Combobox select
select = ["SELECT",
         "1",
         "5",
         "10",
         "15",
         "20",
         "25", ]
data_select = ttk.Combobox(Frame3,values=select, height=70, state="readonly", width=10, font=('', 12),background="#3d0b0b",foreground="black",)
data_select.set(select[0])
data_select.place(x=50, y=55)
# List email
list1=Listbox(Frame3,selectmode="multipe",selectbackground="#5ce1e6",bg="white",width=52,height=16,border=0,highlightthickness=0,font=('',20))
list1.place(x=10,y=120)
root.mainloop()
