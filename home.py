import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector as con
import time
from tkinter import messagebox
win=tk.Tk()
win.title("BOOK STORE")
win.geometry('400x550+300+40')
win.configure(background='green')

lbl_frame=ttk.Label(win,text="    AAS Books Stores        ",font=("algerian",28))
lbl_frame.place(x=0,y=0)

#=============================creating database=======================

mydb=con.connect(host="localhost",user="root",passwd="123123")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists book")
mycursor.execute("use book")
#======================creating required tables =======================
mycursor.execute("create table if not exists book_detail(book_id int auto_increment ,book_name char(24), Author_name char(20),Publication char(30),class int,Board char(10),mrp int,quantity int,primary key(book_id))")
mydb.commit()
#================================Variable===============================
bName = StringVar()
aName = StringVar()
pub = StringVar()
cname = IntVar()
bdname= StringVar()
mname = IntVar()
qname= IntVar()
mrp = IntVar()
bid = IntVar()
#============================function=====================================

def add():
    mycursor.execute("insert into book_detail(book_name,author_name,publication,class,board,mrp,quantity)values('"+bName.get()+"','"+aName.get()+"','"+pub.get()+"','"+str(cname.get())+"','"+bdname.get()+"','"+str(mname.get())+"','"+str(qname.get())+"')")
    mydb.commit()
    tk.messagebox.showinfo("hi","add book successfully")
    
def reset():
   
    bName.set("")
    aName.set("")
    pub.set('')
    cname.set('0')
    bdname.set('')
    mname.set('0')
    qname.set('0')
    uName.set("")
    pword.set("")
    lname.set("")
    add.set("")
    mob.set("")
   
    return


  

#============================add books ===================================
def addbooks():
    
    top=Toplevel()
    top.geometry('500x550+300+40')
    top.title(" Add Books           ")
    top.configure(background='Green')
    lbl_frame=ttk.Label(top,text="              ADD  BOOKS   DETAILS       ",font=("algerian",24))
    lbl_frame.place(x=0,y=0)
    lbl_bname=ttk.Label(top,text="Name of Book    ",font=('algerian',14))
    lbl_bname.place(x=30,y=70)
    txt_bname=ttk.Entry(top,textvariable=bName,font=('algerian',18))
    txt_bname.place(x=200,y=70)
    lbl_aname=ttk.Label(top,text="Author's Name",font=('algerian',14))
    lbl_aname.place(x=30,y=120)
    txt_aname=ttk.Entry(top,textvariable=aName,font=('algerian',18))
    txt_aname.place(x=200,y=120)
    lbl_pub=ttk.Label(top,text="Publication    ",font=('algerian',14))
    lbl_pub.place(x=30,y=170)
    txt_pub=ttk.Entry(top,textvariable=pub,font=('algerian',18))
    txt_pub.place(x=200,y=170)
    lbl_class=ttk.Label(top,text="class               ",font=('algerian',14))
    lbl_class.place(x=30,y=220)
    txt_class=ttk.Entry(top,textvariable=cname,font=('algerian',18))
    txt_class.place(x=200,y=220)

    lbl_board=ttk.Label(top,text="Board                   ",font=('algerian',14))
    lbl_board.place(x=30,y=270)
    txt_board=ttk.Entry(top,textvariable=bdname,font=('algerian',18))
    txt_board.place(x=200,y=270)
    
    
    lbl_mrp=ttk.Label(top,text="MRP                    ",font=('algerian',14))
    lbl_mrp.place(x=30,y=320)
    txt_mrp=ttk.Entry(top,textvariable=mname,font=('algerian',18))
    txt_mrp.place(x=200,y=320)
    lbl_qua=ttk.Label(top,text="Quantity           ",font=('algerian',14))
    lbl_qua.place(x=30,y=370)
    txt_qua=ttk.Entry(top,textvariable=qname,font=('algerian',18))
    txt_qua.place(x=200,y=370)
    btn_add=ttk.Button(top,width=15,text="ADD BOOK",command=add)
    btn_add.place(x=70,y=420)
    btn_set = ttk.Button(top,width=15,text="Reset", command=reset)
    btn_set.place(x=180,y=420)
    btn_exit=ttk.Button(top,width=15,text="EXIT")
    btn_exit.place(x=300,y=420)
    
    btn_exit.config(command=top.destroy)
    txt_bname.focus()
#==================update mrp===================================
def mrp1():
    

    
    #mycursor.execute=("update book_detail set mrp={} where book_id={}".format(mrp.get(),bid.get()))
    mycursor.execute("update book_detail set mrp='"+str(mr.get())+"' where book_id='"+str(bid.get())+"';")
    mydb.commit()

    tk.messagebox.showinfo("Hello showinfo", "updated successfully")
    return
#================search================
def search1():
    
    sql="select mrp,book_name from book_detail where book_id='%s'"%bid.get()
    mycursor.execute(sql)
    result=mycursor.fetchone()
    oldmrp.set(result[0])
    bname.set(result[1])
    
    
#==========================uddate product MRP===========================
def update():
    update=Toplevel()
    update.geometry('400x550+300+40')
    update.title("add books")
    update.configure(background='green')
    global mr,bid,oldmrp,bname
    mr = IntVar()
    bid = IntVar()
    oldmrp=IntVar()
    bname=StringVar()
    lbl_frame=Label(update,text="UPDATE BOOK DETAILS            ",font=("algerian",25))
    lbl_frame.place(x=0,y=0)
    lbl_name=ttk.Label(update,text="Book Id  ",font=('algerian',14))
    lbl_name.place(x=50,y=110)
    txt_name=ttk.Entry(update,textvariable=bid)
    txt_name.place(x=170,y=110)
    lbl_u=ttk.Label(update,text="Book name",font=('algerian',14))
    lbl_u.place(x=50,y=150)
    txt_u=ttk.Entry(update,textvariable=bname)
    txt_u.place(x=170,y=150)
    lbl_u=ttk.Label(update,text="Old Mrp ",font=('algerian',14))
    lbl_u.place(x=50,y=200)
    txt_u=ttk.Entry(update,textvariable=oldmrp)
    txt_u.place(x=170,y=200)
    lbl_up=ttk.Label(update,text=" New MRP ",font=('algerian',14))
    lbl_up.place(x=50,y=250)
    txt_up=ttk.Entry(update,textvariable=mr)
    txt_up.place(x=170,y=250)
    btn_add1=Button(update,width=8,fg="green",bg="pink",text="search",command=search1)
    btn_add1.place(x=300,y=110)
    btn_add=Button(update,width=15,fg="green",bg="yellow",text="SUBMIT",command=mrp1)
    btn_add.place(x=50,y=370)
    btn_exit=Button(update,width=15,fg="black",bg="RED",text="EXIT")
    btn_exit.place(x=200,y=370)
    btn_exit.config(command=update.destroy)
    txt_name.focus()
#====================update qty====================
def mrp2():
    
    
    
    #mycursor.execute=("update book_detail set mrp={} where book_id={}".format(mrp.get(),bid.get()))
    mycursor.execute("update book_detail set quantity='"+str(qty.get())+"' where book_id='"+str(bid.get())+"';")
    mydb.commit()
    tk.messagebox.showinfo("hi","updated successfully")
#================search================
def search2():
    
    sql="select quantity,book_name from book_detail where book_id='%s'"%bid.get()
    mycursor.execute(sql)
    result=mycursor.fetchone()
    oldqty.set(result[0])
    bname.set(result[1])
   
    

#==========================uddate product QUANTITY===========================

def updat():
    updat=Toplevel()
    updat.geometry('400x550+300+40')
    updat.title("UPDATE book QUANTITY")
    updat.configure(background='green')
    global oldqty,qty,bid,bname
    oldqty=IntVar()
    qty = IntVar()
    bid = IntVar()
    bname=StringVar()
    lbl_frame=ttk.Label(updat,text="UPDATE BOOK QUANTITY             ",font=("algerian",25))
    lbl_frame.place(x=0,y=0)
    lbl_name=ttk.Label(updat,text="Book Id",font=('algerian',14))
    lbl_name.place(x=50,y=70)
    txt_name=ttk.Entry(updat,textvariable=bid)
    txt_name.place(x=200,y=70)
    lbl_u=ttk.Label(updat,text="Old Quantity",font=('algerian',14))
    lbl_u.place(x=50,y=150)
    txt_u=ttk.Entry(updat,textvariable=oldqty)
    txt_u.place(x=200,y=150)
    lbl_u=ttk.Label(updat,text="Book name",font=('algerian',14))
    lbl_u.place(x=50,y=200)
    txt_u=ttk.Entry(updat,textvariable=bname)
    txt_u.place(x=200,y=200)
    lbl_up=ttk.Label(updat,text="New Quantity",font=('algerian',14))
    lbl_up.place(x=50,y=250)
    txt_up=ttk.Entry(updat,textvariable=qty)
    txt_up.place(x=200,y=250)
    btn_add1=Button(updat,width=8,fg="black",bg="pink",text="search",command=search2)
    btn_add1.place(x=200,y=100)
    btn_add=Button(updat,width=15,fg="green",bg="yellow",text="SUBMIT",command=mrp2)
    btn_add.place(x=50,y=350)
    btn_exit=Button(updat,width=15,fg="black",bg="red",text="EXIT")
    btn_exit.place(x=200,y=350)
    btn_exit.config(command=updat.destroy)
    txt_name.focus()






#==========================purchase====================================
def purchase():
    #======================creating required tables =======================
    mycursor.execute("create table if not exists book_show(o_id char(10) unique,book_id int,c_name char(24), M_num char(20),B_name char(30),mrp int,quantity int,total int,foreign key(book_id)references book_detail(book_id))")
    mydb.commit()
    #==================format======================================
    root =Toplevel()
    root.geometry("990x680+0+0")
    root.title("AAS BOOKS STORES")
    root.configure(background='skyblue')
    
    Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)
    f1.configure(background='skyblue')
    
    f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
    f2.pack(side=RIGHT)
    f2.configure(background='skyblue')
    
    #------------------TIME--------------
    localtime=time.asctime(time.localtime(time.time()))

    #-----------------INFO TOP------------
    lblinfo = Label(root, font=( 'algerian' ,32, 'bold' ),text="        AAS BOOKS STORES Billing System          ",fg="GREEN",bd=10,anchor='w')
    lblinfo.place(x=0,y=0)
    lblinfo = Label(root, font=( 'algerian' ,20, ),text=localtime,fg="steel blue",anchor=W)
    lblinfo.place(x=0,y=70)

    def Ref():
        
        if int(qty.get())<=int(oldqty.get()):
            bsum=cost.get()
            comrp=float(mrp.get())
            colqty= float(qty.get())
            A= float(qty.get())
            B= oldqty.get()
            C=B-A
            costb=comrp*colqty
            bsum=bsum+costb
        

            costbook = str('%.2f'% (bsum))
            discount=((bsum)*0.10)
            Totalcost=(bsum-discount)

            disc=str('%.2f'% discount)
            OverAllCost=str(bsum-discount)
 
            oldqty.set(C)
            cost.set(costbook)
            dis.set(disc)
            total.set(OverAllCost)
        
            mycursor.execute("insert into book_show(o_id,book_id,c_name,M_num,B_name,mrp,quantity,total)values('"+O_id.get()+"','"+str(B_id.get())+"','"+C_name.get()+"','"+M_num.get()+"','"+B_name.get()+"','"+mrp.get()+"','"+qty.get()+"','"+str(total.get())+"')")
            mydb.commit()
        
       
        
    
            #mycursor.execute=("update book_detail set mrp={} where book_id={}".format(mrp.get(),bid.get()))
            mycursor.execute("update book_detail set quantity='"+str(oldqty.get())+"' where book_id='"+str(B_id.get())+"';")
            mydb.commit()
            B_id.set("0")
            B_name.set("")
            mrp.set("")
            qty.set("")
        else:
            tk.messagebox.showinfo("hi ", "enough quantity is not available")
    def reset():
        B_id.set("0")
        C_name.set("")
        M_num.set("")
        B_name.set("")
        mrp.set("")
        qty.set("")
        cost.set("0.0")
        dis.set("0.0")
        total.set("0.0")   
#================search================
    def search():
   
        sql="select book_name,mrp,quantity from book_detail where book_id='%s'"%B_id.get()
        mycursor.execute(sql)
        result=mycursor.fetchone()
        B_name.set(result[0])
        mrp.set(result[1])
        oldqty.set(result[2])
        txtbook.configure()
        
    
#-----------------------------------------buttons------------------------------------------
    lblTotal = Label(f1,text="---------------------",fg="white")
    lblTotal.grid(row=7,columnspan=3)

    btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="red",command=Ref)
    btnTotal.grid(row=9, column=1)

    btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="red",command=reset)
    btnreset.grid(row=9, column=2)

    btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=root.destroy)
    btnexit.grid(row=9, column=3)
    btnsearch=Button(f1,fg="black",font=('ariel' ,16,'bold'),width=10, text="Search", bg="green",command=search)
    btnsearch.grid(row=2, column=2)

#==============================variable===============================
    B_id= IntVar()
    C_name= StringVar()
    M_num= StringVar()
    B_name= StringVar()
    mrp= StringVar()
    qty= StringVar()
    cost=DoubleVar()
    dis= StringVar()
    total= DoubleVar()
    O_id= StringVar()
    oldqty=IntVar()
#============================
    lblbooks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order no.",fg="blue",bd=10,anchor='w')
    lblbooks.grid(row=1,column=0)
    txtbooks =Entry(f1,font=('ariel' ,16,'bold'), textvariable=O_id , bd=3,insertwidth=4 ,justify='right')
    txtbooks.grid(row=1,column=1)

    lblbook = Label(f1, font=( 'aria' ,16, 'bold' ),text="Book ID",fg="blue",bd=10,anchor='w')
    lblbook.grid(row=2,column=0)
    txtbook = Entry(f1,font=('ariel' ,16,'bold'), textvariable=B_id , bd=3,insertwidth=4 ,justify='right')
    txtbook.grid(row=2,column=1)

    lblcname = Label(f1, font=( 'aria' ,16, 'bold' ),text=" Customer's Name ",fg="blue",bd=10,anchor='w')
    lblcname.grid(row=3,column=0)
    txtcname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=C_name , bd=3,insertwidth=4 ,justify='right')
    txtcname.grid(row=3,column=1)

    lblmob = Label(f1, font=( 'aria' ,16, 'bold' ),text="Mob no. ",fg="blue",bd=10,anchor='w')
    lblmob.grid(row=4,column=0)
    txtmob = Entry(f1,font=('ariel' ,16,'bold'), textvariable=M_num , bd=3,insertwidth=4 ,justify='right')
    txtmob.grid(row=4,column=1)


    lblbname = Label(f1, font=( 'aria' ,16, 'bold' ),text="Book's Name ",fg="blue",bd=10,anchor='w')
    lblbname.grid(row=5,column=0)
    txtbname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=B_name , bd=3,insertwidth=4 ,justify='right')
    txtbname.grid(row=5,column=1)

    lblmrp = Label(f1, font=( 'aria' ,16, 'bold' ),text="MRP ",fg="blue",bd=10,anchor='w')
    lblmrp.grid(row=6,column=0)
    txtmrp = Entry(f1,font=('ariel' ,16,'bold'), textvariable=mrp , bd=3,insertwidth=4 ,justify='right')
    txtmrp.grid(row=6,column=1)

    lblqty = Label(f1, font=( 'aria' ,16, 'bold' ),text="Quantity",fg="blue",bd=10,anchor='w')
    lblqty.grid(row=8,column=0)
    txtqty = Entry(f1,font=('ariel' ,16,'bold'), textvariable=qty , bd=3,insertwidth=4,justify='right')
    txtqty.grid(row=8,column=1)
    lbloqty = Label(f1, font=( 'aria' ,16, 'bold' ),text="Quantity Available",fg="blue",bd=10,anchor='w')
    lbloqty.grid(row=7,column=0)
    txtoqty = Entry(f1,font=('ariel' ,16,'bold'), textvariable=oldqty , bd=6,insertwidth=4,justify='right')
    txtoqty.grid(row=7,column=1)
#==================show purchase======================================================
    def showpurc():
        win=Tk()
        win.title("Tree")
        win.geometry("800x300+200+100")
        
        f1 = Frame(win,width = 900,height=700,relief=SUNKEN)
        f1.pack(side=RIGHT)
        
        
        f2 = Frame(win ,width = 400,height=700,relief=SUNKEN)
        f2.pack(side=LEFT)
        lblsum=ttk.Label(f2,text=C_name)

        tree = ttk.Treeview(f1, columns=("BookId", "BookName", "mrp", "quantity","total"), height=400)
        tree.pack()
        tree.heading('BookId', text="Book id", anchor=W)
        tree.heading('BookName', text="Book name", anchor=W)
        tree.heading('mrp', text="mrp", anchor=W)
        tree.heading('quantity', text="qantity", anchor=W)
        tree.heading('total', text="total", anchor=W)
        
        

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=80)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=90)
        
        



        mydb=con.connect(host="localhost",user="root",passwd="123123")
        mycursor=mydb.cursor()
        mycursor.execute("use book")
        mycursor.execute("SELECT book_id,B_name,mrp,quantity,total FROM `book_show` where o_id={}".format(O_id.get()))
        fetch = mycursor.fetchall()


        for data in fetch:
            tree.insert('', 'end', values=(data))
        mycursor.close()

#--------------------------------------------------------------------------------------


    lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
    lblcost.grid(row=4,column=2)
    txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
    txtcost.grid(row=4,column=3)

    lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Discount",fg="black",bd=10,anchor='w')
    lblService_Charge.grid(row=5,column=2)
    txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=dis , bd=6,insertwidth=4,bg="white" ,justify='right')
    txtService_Charge.grid(row=5,column=3)

    lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="black",bd=10,anchor='w')
    lblTax.grid(row=6,column=2)
    txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=total, bd=6,insertwidth=4,bg="white" ,justify='right')
    txtTax.grid(row=6,column=3)

#--------------------------------------------------------------------------------------

    btnshow=Button(f1,padx=16,pady=8, bd=10 ,fg="pink",font=('ariel' ,16,'bold'),width=10, text="slip",command=showpurc)
    btnshow.grid(row=9, column=0)

    root.mainloop()
#=============================show detail===============================
def show():
    win=Tk()
    win.title("Tree")
    win.geometry("800x300+200+100")

    tree = ttk.Treeview(win, columns=("BookId", "BookName", "AuthorName", "Publication", "Class", "Board","mrp","quantity"), height=400)
    tree.pack()
    tree.heading('BookId', text="Book id", anchor=W)
    tree.heading('BookName', text="Book name", anchor=W)
    tree.heading('AuthorName', text="Author name", anchor=W)
    tree.heading('Publication', text="Publication", anchor=W)
    tree.heading('Class', text="Class", anchor=W)
    tree.heading('Board', text="Board", anchor=W)
    tree.heading('mrp', text="mrp", anchor=W)
    tree.heading('quantity', text="Quantity", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=80)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=90)
    tree.column('#7', stretch=NO, minwidth=0, width=80)



    mydb=con.connect(host="localhost",user="root",passwd="123123")
    mycursor=mydb.cursor()
    mycursor.execute("use book")
    mycursor.execute("SELECT * FROM `book_detail` ORDER BY `book_id` ASC")
    fetch = mycursor.fetchall()


    for data in fetch:
        tree.insert('', 'end', values=(data))
    mycursor.close()

    
#======================creating required tables =======================
mycursor.execute("create table if not exists login(username char(24),password char(24),Name char(20),Address char(30),mob char(10))")
mydb.commit()

#========================login========================================
def login():
    win=Toplevel()
    win.geometry('400x550+300+40')
    win.title(" Add Books           ")
    win.configure(background='Green')
    lbl_frame=ttk.Label(win,text="              Login             ",font=("algerian",24))
    lbl_frame.place(x=0,y=0)
    #================================Variable===============================
       
    lbl_frame=ttk.Label(win,text="    AAS Books Stores        ",font=("algerian",28))
    lbl_frame.place(x=0,y=0)
    btn_add=Button(win,padx=8,pady=4, bd=5,font=('ariel' ,16,'bold'),width=25,fg="black",bg="red",text="AddBooks")
    btn_add.place(x=10,y=130)

    btn_add.config(command=addbooks)
    btn_update=Button(win,padx=8,pady=4, bd=5 ,font=('ariel' ,16,'bold'),width=25,fg="black",bg="red",text="Update MRP")
    btn_update.place(x=10,y=210)

    btn_update.config(command=update)
    btn_updat=Button(win,padx=8,pady=4, bd=5 ,font=('ariel' ,16,'bold'),width=25,fg="black",bg="red",text="Update QUANTITY")
    btn_updat.place(x=10,y=290)
    btn_updat.config(command=updat)
    btn_add=Button(win,padx=8,pady=4, bd=5,font=('ariel' ,16,'bold'),width=25,fg="black",bg="red",text="Show product detail")
    btn_add.place(x=10,y=370)

    btn_add.config(command=show)
    btn_pur=Button(win,padx=8,pady=4, bd=5,font=('ariel' ,16,'bold'),width=25,fg="black",bg="red",text="Purchase Books")
    btn_pur.place(x=10,y=450)
    btn_pur.config(command=purchase)
#================================Variable===============================
uName = StringVar()
pword = StringVar()
lname = StringVar()
add= StringVar()
mob= StringVar()
       
#=========================to register===================================
def ad():
     #================================Variable===============================
    mycursor.execute("insert into login(username,password,Name,Address,mob)values('"+uName.get()+"','"+pword.get()+"','"+lname.get()+"','"+add.get()+"','"+mob.get()+"')")
    mydb.commit()
    uName.set("")
    pword.set("")
    lname.set("")
    add.set("")
    mob.set("")
    tk.messagebox.showinfo("hi","you register successfully")
    


#=======================registration=========================================
def register():
    top=Toplevel()
    top.geometry('400x550+300+40')
    top.title(" Add Books           ")
    top.configure(background='Green')
    lbl_frame=ttk.Label(top,text="              Registration             ",font=("algerian",24))
    lbl_frame.place(x=0,y=0)
    
   
    lbl_u=ttk.Label(top,text="UserName   ",font=('algerian',14))
    lbl_u.place(x=10,y=70)
    txt_u=ttk.Entry(top,textvariable=uName,font=18)
    txt_u.place(x=140,y=70)
    lbl_p=ttk.Label(top,text="Password",font=('algerian',14))
    lbl_p.place(x=10,y=120)
    txt_p=ttk.Entry(top,textvariable=pword,font=18)
    txt_p.place(x=140,y=120)
    lbl_n=ttk.Label(top,text="Name      ",font=('algerian',14))
    lbl_n.place(x=10,y=170)
    txt_n=ttk.Entry(top,textvariable=lname,font=18)
    txt_n.place(x=140,y=170)
    lbl_add=ttk.Label(top,text="Address      ",font=('algerian',14))
    lbl_add.place(x=10,y=220)
    txt_add=ttk.Entry(top,textvariable=add,font=18)
    txt_add.place(x=140,y=220)
    lbl_mob=ttk.Label(top,text="Mob. no.       ",font=('algerian',14))
    lbl_mob.place(x=10,y=270)
    txt_mob=ttk.Entry(top,textvariable=mob,font=18)
    txt_mob.place(x=140,y=270)
       
    btn_add=Button(top,width=12,fg="green",bg="yellow",text="Register",command=ad)
    btn_add.place(x=20,y=420)
    btn_set =Button(top,width=12,fg="green",bg="pink",text="Reset", command=reset)
    btn_set.place(x=140,y=420)
    btn_exit=Button(top,width=12,fg="black",bg="red",text="EXIT")
    btn_exit.place(x=260,y=420)
    
    btn_exit.config(command=top.destroy)
    txt_u.focus()


def si():
   
    
    win.geometry('400x550+300+40')
    win.title(" Add Books           ")
    win.configure(background='Green')
    lbl_frame=ttk.Label(win,text="              Login                        ",font=("algerian",24))
    lbl_frame.place(x=0,y=0)
  

    
    uName = StringVar()
    pword = StringVar()

    lbl_name=ttk.Label(win,text="Username ",font=('arial',14,'bold'))
    lbl_name.place(x=0,y=50)
    txt_name=ttk.Entry(win,textvariable=uName) 
    txt_name.place(x=110,y=50)
    lbl_u=ttk.Label(win,text="Password",font=('arial',14,'bold'))
    lbl_u.place(x=0,y=80)
    txt_u=ttk.Entry(win,show="*",textvariable=pword)
    txt_u.place(x=110,y=80)
    btn_add2=Button(win,width=12,fg="red",bg="pink",font=('arial',14,'bold'),text="Login",command=login)
    btn_add2.place(x=240,y=50)
   
   
            


#=========================================================================================================
btn_add2=Button(win,width=12,fg="red",bg="pink",font=('arial',14,'bold'),text="sign in",command=si)
btn_add2.place(x=240,y=50)

btn_add1=Button(win,width=12,fg="red",bg="pink",font=('arial',14,'bold'),text="Regitration",command=register)
btn_add1.place(x=240,y=450)

