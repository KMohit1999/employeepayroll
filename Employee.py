from random import sample
from tkinter import *
from tkinter import Label,Frame,Entry,Text
from tkinter import messagebox,ttk
import pymysql #pip install pymysql
import time 
import os
import tempfile



class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title=("Employee Payroll Management System | developed by Mohit Kulkarni")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,width=1320)
        btn_emp=Button(self.root,text="All Employee",command=self.employee_frame,font=("times new roman",17),bg="grey",fg="white",anchor="w",padx=4).place(x=1000,y=10,height=30,width=140)
        #=========Frame 1===============

        #==== Variable==================
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar() # Aadhar Card =========
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience=StringVar()
        self.txt_address=StringVar()
        
        

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=800,height=620)
        title2=Label(Frame1,text="Employee details",font=("times now roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=50,relwidth=1 )
        self.txt_code=Entry(Frame1,font=("times new roman",20),textvariable=self.var_emp_code,bg="lightyellow",fg="black")
        self.txt_code.place(x=220,y=53,width=220) 
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",20),bg="grey",fg="black",anchor="w",padx=10).place(x=480,y=46,width=100)
       

        ### Row1
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=100,relwidth=1)
        txt_designation=Entry(Frame1,font=("times new roman",20),textvariable=self.var_designation,bg="lightyellow",fg="black").place(x=170,y=103,width=220) 
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=390,y=103,relwidth=1)
        txt_dob=Entry(Frame1,font=("times new roman",20),textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=520,y=103 ,width=150)
        
        ##Row2
        lbl_Name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=150,relwidth=1)
        txt_Name=Entry(Frame1,font=("times new roman",20),textvariable=self.var_name,bg="lightyellow",fg="black").place(x=170,y=155,width=220) 
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=400,y=153,relwidth=1)
        txt_doj=Entry(Frame1,font=("times new roman",20),textvariable=self.var_doj,bg="lightyellow",fg="black").place(x=520,y=153 ,width=150)

        ##Row3
        lbl_age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=200,relwidth=1)
        txt_age=Entry(Frame1,font=("times new roman",20),textvariable=self.var_age,bg="lightyellow",fg="black").place(x=170,y=205,width=200) 
        lbl_experience=Label(Frame1,text="Experience",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=383,y=203,relwidth=1)
        txt_experience=Entry(Frame1,font=("times new roman",20),textvariable=self.var_experience,bg="lightyellow",fg="black").place(x=520,y=203 ,width=150)    

        
        ##Row4
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=250,relwidth=1)
        txt_gender=Entry(Frame1,font=("times new roman",20),textvariable=self.var_gender,bg="lightyellow",fg="black").place(x=170,y=253,width=200) 
        lbl_proof=Label(Frame1,text="Proof Id",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=383,y=253,relwidth=1)
        txt_proof=Entry(Frame1,font=("times new roman",20),textvariable=self.var_proof_id,bg="lightyellow",fg="black").place(x=520,y=253 ,width=150)    

        ##Row5
        lbl_email=Label(Frame1,text="Email",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=300,relwidth=1)
        txt_email=Entry(Frame1,font=("times new roman",20),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=170,y=303,width=200) 
        lbl_contact=Label(Frame1,text="Contact No",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=380,y=303,relwidth=1)
        txt_contact=Entry(Frame1,font=("times new roman",20),textvariable=self.var_contact,bg="lightyellow",fg="black").place(x=520,y=303 ,width=150)    

        ##Row6
        lbl_hired=Label(Frame1,text="Hire Location",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=350,relwidth=1)
        txt_hired=Entry(Frame1,font=("times new roman",20),textvariable=self.var_hr_location,bg="lightyellow",fg="black").place(x=190,y=353,width=190) 
        lbl_status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black",anchor="w",padx=10).place(x=380,y=353,relwidth=1)
        txt_status=Entry(Frame1,font=("times new roman",20),textvariable=self.var_status,bg="lightyellow",fg="black").place(x=520,y=353,width=175)    

        ##Row7  
        lbl_address=Label(Frame1,text="Address",font=("times new roman",18),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=422,relwidth=1)
        txt_address=Entry(Frame1,font=("times new roman",20),textvariable=self.txt_address,bg="lightyellow",fg="black").place(x=190,y=425,width=450,height=140) 
        
       # self.txt_address=Text(Frame1,font=("times new roman",20),bg="lightyellow",fg="black")
       # self.txt_address.place(x=190,y=425,width=450,height=140) 

        #============Variable=============
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
        self.var_salary_receipt=StringVar()


        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)

        title3=Label(Frame2,text="Employee Salary Details",font=("times now roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_month=Label(Frame2,text="Month",font=("times new roman",15),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=60,relwidth=1 )
        txt_month=Entry(Frame2,font=("times new roman",15),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=80,y=60,width=90) 
       
        lbl_year=Label(Frame2,text="Year",font=("times new roman",15),bg="white",fg="black",anchor="w",padx=10).place(x=170,y=60,relwidth=1 )
        txt_year=Entry(Frame2,font=("times new roman",15),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=225,y=60,width=70) 
        
        lbl_salary=Label(Frame2,text="Salary",font=("times new roman",15),bg="white",fg="black",anchor="w",padx=10).place(x=300,y=60,relwidth=1 )
        txt_salary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_salary,bg="lightyellow",fg="black").place(x=380,y=60,width=90) 
        

        ### Row1
        lbl_days=Label(Frame2,text="Total Days",font=("times new roman",15),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=103,relwidth=1)
        txt_days=Entry(Frame2,font=("times new roman",15),textvariable=self.var_t_days,bg="lightyellow",fg="black").place(x=120,y=103,width=120) 
        lbl_absent=Label(Frame2,text="Absents:",font=("times new roman",15),bg="white",fg="black",anchor="w",padx=10).place(x=250,y=103,relwidth=1)
        txt_absent=Entry(Frame2,font=("times new roman",15),textvariable=self.var_absent,bg="lightyellow",fg="black").place(x=340,y=103 ,width=120)
        
        ##Row2
        lbl_medical=Label(Frame2,text="Medical",font=("times new roman",15),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=150,relwidth=1)
        txt_medical=Entry(Frame2,font=("times new roman",15),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=120,y=155,width=120) 
        lbl_pf=Label(Frame2,text="PF",font=("times new roman",15),bg="white",fg="black",anchor="w",padx=10).place(x=260,y=153,relwidth=1)
        txt_pf=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black").place(x=340,y=153 ,width=120)

        ##Row3  
        lbl_convence=Label(Frame2,text="Convence",font=("times new roman",15),bg="white",fg="black",anchor="w",padx=10).place(x=10,y=200,relwidth=1)
        txt_convence=Entry(Frame2,font=("times new roman",15),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=120,y=205,width=110) 
        lbl_netsalary=Label(Frame2,text="Net Salary",font=("times new roman",13),bg="white",fg="black",anchor="w",padx=10).place(x=237,y=203,relwidth=1)
        txt_netsalary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_net_salary,bg="lightyellow",fg="black").place(x=327,y=203,width=120)

        ##Row4
        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",17),bg="orange",fg="black",anchor="w",padx=4).place(x=70,y=243,height=20)
        btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman",17),bg="green",fg="white",anchor="w",padx=4).place(x=210,y=243,height=20)
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",17),bg="grey",fg="black",anchor="w",padx=4).place(x=310,y=243,height=20)
       
       
        btn_update=Button(Frame2,text="Update",command=self.update,font=("times new roman",17),bg="blue",fg="white",anchor="w",padx=4).place(x=70,y=268,height=40,width=120)
        btn_delete=Button(Frame2,text="Delete",command=self.delete,font=("times new roman",17),bg="red",fg="white",anchor="w",padx=4).place(x=210,y=268,height=40,width=120)
        #=== Frame3
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)

        #=== Calculator
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
            print(num)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
         
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''
           
        Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE).place(x=2,y=2,width=243,height=300)

        txt_Result=Entry(Frame3,bg='lightyellow',textvariable=self.var_txt,font=("times new roman",15)).place(x=0,y=0,height=40,width=247)

        # ==== Row1===========
        btn_7=Button(Frame3,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=42,width=60,height=60)  
        btn_7=Button(Frame3,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=61,y=42,width=60,height=60)
        btn_7=Button(Frame3,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=122,y=42,width=60,height=60)   
        btn_7=Button(Frame3,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=183,y=42,width=60,height=60)
        #==Row2======
        btn_7=Button(Frame3,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=103,width=60,height=60)  
        btn_7=Button(Frame3,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=61,y=103,width=60,height=60)
        btn_7=Button(Frame3,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=122,y=103,width=60,height=60)   
        btn_7=Button(Frame3,text='*',command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=183,y=103,width=60,height=60)
        
        #==Row3======
        btn_7=Button(Frame3,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=155,width=60,height=60)  
        btn_7=Button(Frame3,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=61,y=155,width=60,height=60)
        btn_7=Button(Frame3,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=122,y=155,width=60,height=60)   
        btn_7=Button(Frame3,text='-',command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=183,y=155,width=60,height=60)
        
        #==Row4======
        btn_7=Button(Frame3,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=205,width=60,height=60)  
        btn_7=Button(Frame3,text='C',command=clear_cal(),font=("times new roman",15,"bold")).place(x=61,y=205,width=60,height=60)
        btn_7=Button(Frame3,text='+',command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=122,y=205,width=60,height=60)   
        btn_7=Button(Frame3,text='=',command=result,font=("times new roman",15,"bold")).place(x=183,y=205,width=60,height=60)
        
        #=========== Salary Frame=======
        sal_Frame=Frame(Frame3,bg="white",relief=RIDGE)
        sal_Frame.place(x=250,y=2,width=320,height=300)

        title_sal=Label(sal_Frame,text="Salary Receipt",font=("times now roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2=Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,width=250,height=200)
        
        new_sample =''' \t Company Name , XYZ \n\tAddress: Xyz,Floor4
        ---------------------------------------------------
        Employee ID\t\t: {self.var_emp_code.get()}
        Salary of \t\t:    {self.var_month.get()}-{self.var_year.get()}
        Generated on \t\t: {str(time.strftime("%d-%M-%Y"))}
        ---------------------------------------------------
        Total Days \t\t:  {self.var_t_days.get()}
        Total Presents \t\t: {str(self.var_t_days.get()-int(self.var_absent.get()))}
        Total Absents \t\t: {self.var_absents.get()}
        Convence \t\t: Rs. {self.var_convence.get()}
        Medical \t\t: Rs.{self.var_medical.get()}
        PF \t\t: Rs.{self.var_pf.get()}
        Gross Salary \t\t: Rs.{self.var_salary.get()}
        Net Salary \t\t: Rs.{self.var_net_salary.get()}
        ----------------------------------------------------
        This is computer generated slip,must
        required any signature 
        '''
   #     self.var_salary_receipt.delete('1.0',END) 
    #    self.var_salary_receipt.insert(END,new_sample)

        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",13),bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1,)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,sample)

        self.btn_print=Button(sal_Frame,text="Print",state=DISABLED,font=("times new roman",17),bg="lightblue",fg="black",anchor="w",padx=4)
        self.btn_print.place(x=164,y=230,height=30,width=90)

     #   self.check_connection()

    def clear(self):
        self.btn_save.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.btn_update.config(state=NORMAL)
        self.btn_delete.config(state=NORMAL)
        self.txt_code.config(state='readonly')

        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')    
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.set('')
            
        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
    
                    


    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error ","Employee Id must be required")
        else:
             
            try:  
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                # print(rows)
                if row==None:
                    messagebox.showerror("Error","Invalid employee id, please try with another employee id ",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op>1:
                        cur.execute("delete * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee record deleted successfully ",parent=self.root)
     

                        
            except Exception as ex:
                messagebox.showerror("Error ",f"Error due to:{str(ex)} ")                   
        

    def search(self):
        try:
                    
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                # print(rows)
                if row==None:
                    messagebox.showerror("Error","Invalid employee id, please try with another employee id ",parent=self.root)
                else :
                #    print(row)
                    self.var_emp_code.set(row[0])
                    self.var_designation.set(row[1])
                    self.var_name.set(row[2])
                    self.var_age.set(row[3])
                    self.var_gender.set(row[4]) 
                    self.var_email.set(row[5])
                    self.var_hr_location.set(row[6])
                    self.var_doj.set(row[7])
                    self.var_dob.set(row[8])
                    self.var_experience.set(row[9])
                    self.var_proof_id.set(row[10])
                    self.var_contact.set(row[11])
                    self.var_status.set(row[12])
                    self.txt_address.set(row[13])


                    self.var_month.set(row[14])
                    self.var_year.set(row[15])
                    self.var_salary.set(row[16])
                    self.var_t_days.set(row[17])
                    self.var_absent.set(row[18])
                    self.var_medical.set(row[19])
                    self.var_pf.set(row[20])
                    self.var_convence.set(row[21])
                    self.var_net_salary.set(row[22])
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get(row[23])),'r')
                    self.txt_salary_receipt.delete('1.0',END)
                    for i in file_:
                        self.txt_salary_receipt.insert(END,i)
                    file_.close()
                    self.btn_save.config(state=DISABLED)
                    self.btn_update.config(state=NORMAL)
                    self.btn_delete.config(state=NORMAL)
                    self.txt_code.config(state='readonly')
                    self.btn_print.config(state=NORMAL)
                                


        except Exception as ex:
                messagebox.showerror("Error ",f"Error due to:{str(ex)} ")       


    def add(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='' :
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                    
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                # print(rows)
                if row!=None:
                    messagebox.showerror("Error","This employee Id has already available in our record,try again with another ID",parent=self.root)
                else :
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
        
                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(), 
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),


                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_salary_receipt.get(),
                        "receipt"

                    )                                              
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.var_salary_receipt.get('1.0',END))
                    file_.close()

                    messagebox.showinfo("Success","Record Added Successfully")
                    self.btn_print.config(state=NORMAL)

            except Exception as ex:
                messagebox.showerror("Error ",f"Error due to:{str(ex)} ")    

    def update(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='' :
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                    
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                # print(rows)
                if row==None:
                    messagebox.showerror("Error","This employee Id is invalid, try again with Valid employee  ID",parent=self.root)
                else :
                    cur.execute("UPDATE `emp_salary` SET`Designation`='%s',`name`='%s',`age`='%s',`gender`='%s',`email`='%s',`hr_location`='%s',`doj`='%s',`dob`='%s',`experience`='%s',`proof_id`='%s',`contact`='%s',`status`='%s',`address`='%s',`month`='%s',`year`='%s',`basic_salary`='%s',`t_days`='%s',`absent_days`='%s',`medical`='%s',`pf`='%s',`convence`='%s',`net_salary`='%s',`salary_receipt`='%s' WHERE  `e_id`='%s'",
                    (
        
                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(), 
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get(),


                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_salary_receipt.get(),
                        "receipt"

                    )                                              
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.var_salary_receipt.get('1.0',END))
                    file_.close()

                    messagebox.showinfo("Success","Record Updated Successfully")
                        
            except Exception as ex:
                messagebox.showerror("Error ",f"Error due to:{str(ex)} ")    


    def calculate(self):
        if  self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' :
            messagebox.showerror('Error','All fields are required')
        else :

            per_day=int(self.var_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absent.get())
            sal_=per_day*work_day
            debuct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal_ - debuct + addition
            self.var_net_salary.set(str(round(net_sal,2)))

            #===============Update the receipt====
            sample =''' \t Company Name , XYZ \n\tAddress: Xyz,Floor4
                        ---------------------------------------------------
                        Employee ID\t\t:  {self.var_emp_code.get()}
                        Salary of \t\t: Mon-YYYY
                        Generated on \t\t: DD-MM-YYYY
                        ---------------------------------------------------
                        Total Days \t\t:DD
                        Total Presents \t\t: DD
                        Total Absents \t\t: DD
                        Convence \t\t: Rs.----
                        Medical \t\t: Rs.----
                        PF \t\t: Rs.----
                        Gross Salary \t\t: Rs.-------
                        Net Salary \t\t: Rs.-------
                        ----------------------------------------------------
                        This is computer generated slip,must
                        required any signature 

                        '''

    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()    
        except Exception as ex:
            messagebox.showerror("Error ",f"Error due to:{str(ex)} ")  

    def employee_frame(self):
        self.root2=Tk()
        self.root2.title("Employee Payroll Management System | developed by Mohit Kulkarni")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white") 
        title=Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2,orient=VERTICAL)

        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'Designation','name','age','gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 't_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set) # type: ignore
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='HR LOC.')
        self.employee_tree.heading('doj',text='D.O.J')
        self.employee_tree.heading('dob',text='D.O.B')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('t_days',text='Days')
        self.employee_tree.heading('absent_days',text='Absents')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('salary_receipt',text='Salary Receipt')

        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('absent_days',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=100)
        scrollx.config(command=self.employee_tree.xview) # type: ignore
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1,)
        self.show()


        self.root2.mainloop()

    def print(self):

        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print')
    



root=Tk()
obj=EmployeeSystem(root)
root.mainloop()