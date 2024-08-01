import mysql.connector  as SM
conn=SM.connect(host="localhost",
                user="root",
                passwd="tiger")

cursor=conn.cursor()
cursor.execute("create database if not exists stk")
cursor.execute("use stk")
cursor.execute("create table if not exists user_table(username varchar(35) primary key,passwrd varchar(10) not null)")
print("\n\n\n\n\n")
print("*"*150)
print("\n\n")
print("\t\t\t\t\t\t\t\t\t\t\t WELCOME TO STOCK MANAGMENT SYSTEM \t\t\t")
print("\n\n")
print("*"*150)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("PRESS ENTER TO START....")
print("\n\n\n")
import datetime as dt
print("\n\n\n\n")
print("Time : ",dt.datetime.now())
print("\n\n\n\n\n\n\n")
print("\t\t\t\t\t\t\t\t\t\t\t 1.CREATE YOUR LOGIN ID ")
print("\n")
print("\t\t\t\t\t\t\t\t\t\t 2.LOGIN  WITH THE EXISTING ID")
print("\n\n\n\n\n\n\n")
CH=int(input("ENTER (1) FOR CREATING A NEW ID AND ENTER (2) FOR LOGGING IN WITH EXISTING ID : "))

if CH==1:
    print("\n\n")
    name=input("ENTER A USERNAME : ")
    passwd=int(input("ENTER A 4 DIGIT PASSWORD : "))
    A="INSERT INTO user_table(passwrd,username) values ('"+str(passwd)+"','"+name+"')"
    cursor.execute(A)
    conn.commit()
    print("\n")
    print("LOGIN ID CREATED.... CONGRATULATIONS!!!")
    move=input("PRESS ENTER TO MOVE IN....")

if CH==2:
    print("\n")
    name=input("ENTER YOUR USER NAME : ")
    print("\n")
    passwd=int(input("ENTER YOUR 4 DIGIT PASSWORD : "))
    B="select *from user_table where passwrd='"+str (passwd)+"' and username='"+name+"'"
    cursor.execute(B)
    if cursor.fetchone() is None:
        print()
        print("INVALID USERNAME OR PASWWORD!!!")
    else:
        print("SIGNED IN SUCCESSFULLY...")
        
        

#   MAIN PART 

import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="tiger",
                             database="stk")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists stk")
import os
import mysql.connector
import datetime
now=datetime.datetime.now()

def prod_mnagnt():
    while True:
        print("\t\t\t\t\t\t 1. Add a New Product")
        print("\t\t\t\t\t\t 2. List a Product")
        print("\t\t\t\t\t\t 3. Update a Product")
        print("\t\t\t\t\t\t 4. Delete a Product")
        print("\t\t\t\t\t\t 5. Back (# To Main Menu)") 
        print("\n")
        pr=int(input("Enter Your Choice : "))
        if pr==1:
            add_product()
        if pr==2:
            search_product()
        if pr==3:
            update_product()
        if pr==4:
            delete_product()
        if pr==5:
            break
       


def purchase_mnagnt():
    while True: 
        print("\t\t\t\t\t\t 1. Add Order")
        print("\t\t\t\t\t\t 2. List Order")
        print("\t\t\t\t\t\t 3. Back (Main Menu)") 
        pu=int (input("Enter Your Choice : "))
        if pu==1:
            add_order()
           
        if pu==2:
            list_order()
            
           
        if pu== 3: 
            break
            
def sales_mnagnt():
    while True:
        print("\n\n")
        print("\t\t\t\t\t\t 1. Sale Items") 
        print("\t\t\t\t\t\t 2. List Sales")
        print("\t\t\t\t\t\t 3. Back (Main Menu)") 
        print("\n")
        sl=int (input("Enter Your Choice : "))
        if sl== 1: 
            sale_product()
            
        if sl== 2: 
            list_sale()
            
        if sl== 3:
            break

def user_mnagnt():
    while True: 
        print("\n")
        print("\t\t\t\t\t\t 1. Add user")
        print("\t\t\t\t\t\t 2. List user")
        print("\t\t\t\t\t\t 3. Back (Main Menu)") 
        print("\n")
        ur=int (input("Enter Your Choice : "))
        if ur==1:
            add_user()
        if ur==2:
            list_user()
        if ur==3:
            break
        
def create_database():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    print(" Creating  product table ")
    SM="CREATE TABLE if not exists product (\
        pcode int(5) PRIMARY KEY,\
        pname char(40) NOT NULL,\
        pprice float(10,2),\
        pqty int(5),\
        pcat char(40));"
    mycursor.execute(SM)
    print("PRODUCT TABLE PRODUCT ..")
    
    print(" \n Creating order table")
    SM="CREATE TABLE if  not exists orders(\
        orderid int(5) primary key,\
        orderdate DATE,\
        pcode char(40) not null,\
        pprice float(10,2) ,\
        pqty int(5),\
        supplier char(60),\
        pcat char(40));"
    mycursor.execute(SM)
    print("ORDER TABLE CREATED ..")
    
    print(" \n creating sales table")
    SM="CREATE TABLE if not exists sales(\
        salesid int(5) PRIMARY KEY,\
        salesdate DATE,\
        pcode char(40) references product(pcode),\
        pprice float(10,2),\
        pqty int(5),\
        Total double(8,2)\
        );"
    mycursor.execute(SM)
    print("SALES TABLE CREATED ..")
    
    
    print("\n creating user table")
    SM="CREATE TABLE if not exists user(\
        uid char(35) PRIMARY KEY,\
        uname char(40) NOT NULL,\
        upwd char(20));"
    mycursor.execute(SM)
    print("USER TABLE CREATED ..")
    print("\n")
    

def list_database():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    SM="show tables"
    mycursor.execute(SM)
    for i in mycursor:
        print(i)
        
def add_order():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    now=datetime.datetime.now()
    SM="INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat) values(%s,%s,%s,%s,%s,%s,%s)"
    code=int(input("Enter the product code : "))
    oid=now.year+now.month+now.minute+now.hour+now.second
    qty=int(input("Enter product quantity : "))
    price=float(input("Enter the product price : "))
    cat=input("Enter the product category : ")
    supplier=input("Enter the supplier details : ")
    val=(oid,now,code,price,qty,cat,supplier)
    mycursor.execute(SM,val)
    mydb.commit()
    print("\n")
    move=input("PRESS ENTER TO CONTINUE...")
    print("\n")

  
    
def list_order(): 
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    SM="SELECT *from orders"
    mycursor.execute(SM)
    print("\n")
    print("\t\t\t\t\t\t\t\t ORDER DETAILS")
    print("-"*120)
    print("orderid \t Date \t\t Product code \t price \t Quantity \t Category \t\t Supplier  ")    
    print("-"*120)
    for i in mycursor:
        print(i[0],"\t\t",i[1],"\t",i[2],"\t\t\t",i[3],"\t\t",i[4],"\t",i[5],"\t",i[6])
    print("\n")
    move=input("PRESS ENTER TO CONTINUE ....")
        
def db_mnagnt():
    while True:
        print("\n")
        print("\t\t\t\t\t\t 1.Database creation")
        print("\t\t\t\t\t\t 2.List database")
        print("\t\t\t\t\t\t 3.Back(main menu)")
        pr=int(input("Enter your choice : "))
        print("\n\n")
        if pr==1:
            create_database()
        if pr==2:
            list_database()
        if pr==3:
            break
        
def add_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    SM="INSERT INTO product(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
    code=int(input("\t\t Enter the product code : "))   
    sr="SELECT count(*) FROM product WHERE pcode=%s;"
    val=(code,)
    mycursor.execute(sr,val)
    for m in mycursor:
        ct=m[0]
    if ct==0:
        name=input("\t\t Enter the product name : ")
        qty=int(input("\t\t Enter the product quantity : "))
        price=float(input("\t\t Enter the product unit price : "))
        cat=input("\t\t Enter the product category : ")
        val=(code,name,price,qty,cat)
        mycursor.execute(SM,val)
        mydb.commit()
        print("\n")
        move=input("PRESS ENTER TO CONTINUE ....")
        print("\n\n")
    else:
        print("\t\t Product already exists ")
        
    
def update_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    code=int(input("Enter the prooduct code : "))
    qty=int(input("Enter the quantity : "))
    SM="UPDATE product SET pqty=%s WHERE pcode=%s;"        
    val=(qty,code)
    mycursor.execute(SM,val)
    mydb.commit()
    print("\n")
    print("\t\t Product details is updated")
    print('\n')
    move=input("PRESS ENTER TO CONTINUE ....")

def delete_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    code=int(input("Enter the  product code : "))
    SM="DElETE FROM product WHERE pcode=%s;"
    val=(code,)
    mycursor.execute(SM,val)
    mydb.commit()
    print(mycursor.rowcount,"record(s) deleted")
    print("\n")
    move=input("PRESS ENTER TO CONTINUE ....")
    print("\n")
    
def search_product():
    print("\t\t\t\t\t\t 1.List all product")
    print("\t\t\t\t\t\t 2.list product wise")
    print("\t\t\t\t\t\t 3.List product category wise")
    print("\t\t\t\t\t\t 4.Back (main menu)")
    sl=int(input("Enter your choice : "))
    if sl==1:
        list_product()
    if sl==2:
        code=int(input("Enter the product code : "))
        list_prcode(code)
    if sl==3:
        cat=input("Enter category : ")
        list_prcat(cat)
    

def list_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    SM="SELECT *from product"
    mycursor.execute(SM)
    print("\n")
    print("\t\t\t\t\t\t\t\t PRODUCT DETAILS")
    print("-"*120)
    print("\t\t code \t name \t price \t quantity \t category ")
    print("-"*120)
    for i in mycursor:
        print("\t\t",i[0],"\t\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4])
    print("-"*120)
    move=input("PRESS ENTER TO CONTINUE .....")
    print("\n")
    
def list_prcode(code):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    SM="SELECT *from product WHERE pcode=%s"
    val=(code,)
    mycursor.execute(SM,val)
    print("\n")
    print("\t\t\t\t\t\t\t\t PRODUCT DETAILS")
    print("-"*120)
    print("\t\t code \t name \t price \t quantity \t category")
    print("-"*120)
    for i in mycursor:
        print("\t\t",i[0],"\t\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4])
    print("-"*120)
    print("\n")
    move=input("PRESS ENTER TO MOVE IN ....") 
    
def sale_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    pcode=int(input("Enter the product code : "))
    SM="SELECT count(*) from product WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(SM,val)
    for m in mycursor:
        ct=m[0]
    
    if ct!=0:
        while True:
            SM="SELECT *from product WHERE pcode=%s;"
            val=(pcode,)
            mycursor.execute(SM,val)
            for m in mycursor:
                print(m)
                price=int(m[2])
                pqty=int(m[3])
            qty=int(input("Enter the number of quantity : "))
            if qty<=pqty:
                total=qty*price;
                print("Collect Rs.",total)
                print("\n\n\n\n")
                move=input("PRESS ENTER TO CONTINUE .....")
                SM="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
                val=(int(ct)+100,datetime.datetime.now(),pcode,price,qty,total)
                mycursor.execute(SM,val)
                SM="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
                val=(qty,pcode)
                mycursor.execute(SM,val)
                mydb.commit()  
                ct+=1
                choice=input("Do you want to add more rows ? y/n")
                if choice=="n" or choice=="N":
                    break
        else:
            print("Quantity not available")
    
    else:
        print("Product not available")
        

def list_sale():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    SM="SELECT *FROM sales"
    mycursor.execute(SM)
    print("\n")
    print("\t\t\t\t\t\t\t\t SALES DETAILS")
    print("-"*120)
    print("Salesid  Date \t\t\t Product Code \t Price     Quantity  \t  Total")
    print("-"*120)
    for m in mycursor:
        print(m[0],"\t",m[1],"\t\t",m[2],"\t\t\t",m[3],"\t\t",m[4],"\t\t\t ",m[5])
    print("-"*120) 
    print("\n")
    move=input("PRESS ENTER TO MOVE IN ....")
    
def list_prcat(cat):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    print(cat)
    SM="SELECT *from product WHERE pcat=%s"
    val=(cat,)
    mycursor.execute(SM,val)
    clrscr()
    print("\n")
    print("\t\t\t\t\t\t\t\t PRODUCT DETAILS ")
    print("-"*120)
    print("\t\t code \t name \t price \t quantity \t category ")
    print("-"*120)
    for i in mycursor:
        print("\t\t",i[0],"\t\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4])
    print("-"*120)
    print("\n")
    move=input("PRESS ENTER TO CONTINUE .....")
    print("\n")   

def add_user():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()
    uid=input("Enter the email id : ")
    name=input('Enter the name : ')
    paswd=input("Enter the Password : ")
    SM="INSERT INTO user values(%s,%s,%s);"
    val=(uid,name,paswd)
    mycursor.execute(SM,val)
    mydb.commit()
    print("\n")
    print(mycursor.rowcount,"user created...")
    print("\n")
    

def list_user():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="stk")
    mycursor=mydb.cursor()    
    SM="SELECT uid,uname from user"
    mycursor.execute(SM)
    clrscr()
    print("\t\t\t\t USER DETAILS")
    print("\t\t","-"*22)
    print("\t\t UID \t  name")
    print("\t\t","-"*22)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1])
    print("\t\t","-"*22)
    print("\n")
    move=input("PRESS ENTER TO CONTINUE ....")
        
def clrscr():
    print("\n"*4)
    

while True:
    clrscr()
    print("\t\t\t\t\t\t STOCK MANAGEMENT")
    print("\t\t\t\t\t\t ****************\n")
    print("\t\t\t\t 1. PRODUCT MANAGEMENT")
    print("\t\t\t\t 2. PURCHASE MANAGEMENT")
    print("\t\t\t\t 3. SALES MANAGEMENT")
    print("\t\t\t\t 4. USER MANAGEMENT")
    print("\t\t\t\t 5. DATABASE SETUP")
    print("\t\t\t\t 6. EXIT ")
    print("\n\n")
    o=int(input("Enter your choice : "))
    if o==1:
        prod_mnagnt()
    if o==2:
        os.system('cls')
        purchase_mnagnt()
    if o==3:
        sales_mnagnt()
    if o==4:
        user_mnagnt()
    if o==5:
        db_mnagnt()
    elif o==6:
        print("\n\n")
        print("*"*145)
        print("THANK YOU".center(130))
        print("\n")
        print("STOCK MANAGEMENT SYSTEM".center(130))
        print("DONE BY:".center(140))
        print("\n")
        print("Rounak Vats".center(130))
        print("Adithya Shaktimani".center(130))
        print("\n")
        print("*"*145)
        ot=input("PRESS ENTER TO MOVE OUT ...")
        break
else:
    print("Wrong Choice entered")
    move=input("PRESS ENTER TO CONTINUE ....")
    
    
        
