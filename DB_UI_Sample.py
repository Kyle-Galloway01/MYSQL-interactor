import mysql.connector 
from mysql.connector import errorcode

import tkinter as tk
from tkinter import font
from  tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb

# Begin: Connection to Database ================

try:
    connect = mysql.connector.connect(
        user = 'root',
        password = 'Ga11oway!',
        host = 'localhost',
        database = 'bookdb',
        port = '3306'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Invalid credentials')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database not found')
    else:
        print('Cannot connect to database:', err)
# End: Connection to Database =========================

# Begin: GUI Layout with table and buttons ===========
r = tk.Tk()
r.title("Authors Details")
r.geometry('800x700')

tree = ttk.Treeview(r)
tree['show'] = 'headings'

tree['columns']  = ('au_id', 'au_fname', 'au_lname', \
                    'phone', 'address', 'city', 'state', 'zip')

tree.column('au_id', width=50, minwidth=50, anchor=tk.CENTER)
tree.column('au_fname', width=100, minwidth=100, anchor=tk.W)
tree.column('au_lname', width=100, minwidth=100, anchor=tk.W)
tree.column('phone', width=100, minwidth=100, anchor=tk.CENTER)
tree.column('address', width=150, minwidth=150, anchor=tk.W)
tree.column('city', width=125, minwidth=125, anchor=tk.W)
tree.column('state', width=100, minwidth=100, anchor=tk.CENTER)
tree.column('zip', width=50, minwidth=50, anchor=tk.CENTER)

tree.heading('au_id', text='A_ID', anchor=tk.CENTER)
tree.heading('au_fname', text='First', anchor=tk.CENTER)
tree.heading('au_lname', text='Last', anchor=tk.CENTER)
tree.heading('phone', text='Phone', anchor=tk.CENTER)
tree.heading('address', text='Address', anchor=tk.CENTER)
tree.heading('city', text='City', anchor=tk.CENTER)
tree.heading('state', text='State', anchor=tk.CENTER)
tree.heading('zip', text='Zip', anchor=tk.CENTER)

hsb = ttk.Scrollbar(r, orient='horizontal')
hsb.configure(command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X, side=BOTTOM)

vsb = ttk.Scrollbar(r, orient='vertical')
vsb.configure(command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y, side=RIGHT)

# End: GUI Layout with table and buttons ===========

# Begin: Select initial data and populate GUI Grid ========

conn = connect.cursor()
conn.execute("select * from authors")


for row in conn:
    tree.insert('', 'end', text="", values=(row[0],row[1],row[2],row[3],\
                                            row[4],row[5],row[6],row[7]))
    

tree.pack()

# END: Select initial data and populate GUI Grid ========

# Begin: Variables defined by data types to help with GUI =====

au_id = tk.StringVar()
fName=tk.StringVar()
lName=tk.StringVar()
phone=tk.StringVar()
address=tk.StringVar()
city=tk.StringVar()
au_state=tk.StringVar()
au_zip=tk.StringVar()


# End: Variables defined by data types to help with GUI =====

# Begin: Add Author function ===============

def add_data(tree):

    f = Frame(r, width=400, height=400, background='grey')
    f.place(x=100, y=250)


    l1=Label(f, text='ID', width=8, font=('Times', 11, 'bold'))
    e1=Entry(f,textvariable=au_id, width=25)
    l1.place(x=50, y=30)
    e1.place(x=170, y=30)    
    
    l2=Label(f, text='First Name', width=8, font=('Times', 11, 'bold'))
    e2=Entry(f,textvariable=fName, width=25)
    l2.place(x=50, y=70)
    e2.place(x=170, y=70)

    l3=Label(f, text='Last Name', width=8, font=('Times', 11, 'bold'))
    e3=Entry(f,textvariable=lName, width=25)
    l3.place(x=50, y=110)
    e3.place(x=170, y=110)

    
    l4=Label(f, text='Phone', width=8, font=('Times', 11, 'bold'))
    e4=Entry(f,textvariable=phone, width=25)
    l4.place(x=50, y=150)
    e4.place(x=170, y=150)

    
    l5=Label(f, text='Address', width=8, font=('Times', 11, 'bold'))
    e5=Entry(f,textvariable=address, width=25)
    l5.place(x=50, y=190)
    e5.place(x=170, y=190)

    
    l6=Label(f, text='City', width=8, font=('Times', 11, 'bold'))
    e6=Entry(f,textvariable=city, width=25)
    l6.place(x=50, y=230)
    e6.place(x=170, y=230)


    l7=Label(f, text='State', width=8, font=('Times', 11, 'bold'))
    e7=Entry(f,textvariable=au_state, width=25)
    l7.place(x=50, y=270)
    e7.place(x=170, y=270)


    l8=Label(f, text='Zip', width=8, font=('Times', 11, 'bold'))
    e8=Entry(f,textvariable=au_zip, width=25)
    l8.place(x=50, y=310)
    e8.place(x=170, y=310)

    # What happens when submit button is pressed
    def insert_data():
        nonlocal e1,e2,e3,e4,e5,e6,e7,e8
        a_id = au_id.get()
        a_fname=fName.get()
        a_lname = lName.get()
        a_phone = phone.get()
        a_address = address.get()
        a_city = city.get()
        a_state = au_state.get()
        a_zip = au_zip.get()

        sql_insert = '''INSERT INTO authors(au_id, au_fname, au_lname, 
                    phone, address, city, state, zip) 
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
        
        insert_data = (a_id, a_fname, a_lname, a_phone, \
                          a_address, a_city, a_state, a_zip)
        
        conn.execute(sql_insert, insert_data)
        
        connect.commit()

        tree.insert('','end',text="",values=(a_id, a_fname, a_lname, \
                                             a_phone, a_address, a_city, a_state, a_zip))
        mb.showinfo("Success","Author Created")
        e1.delete(0,END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0,END)
        e8.delete(0,END)
        f.destroy()
    
    submitbutton = tk.Button(f, text="Insert", command=insert_data)
    submitbutton.configure(font=('Times', 11, 'bold'), bg='green', fg='white')
    submitbutton.place(x=100, y=360)
    cancelbutton = tk.Button(f, text="Close", command=f.destroy)
    cancelbutton.configure(font=('Times', 11, 'bold'), bg='red', fg='white')
    cancelbutton.place(x=240, y=360)

# End: Add Author function ============================

# Begin: Delete Author function =======================
def delete_data(tree):
    del_query = 'DELETE from authors where au_id = %s'

    selected_item = tree.selection()[0]
    uid=tree.item(selected_item)['values'][0]
    del_data=(uid,)
    
    conn.execute(del_query, del_data)
    connect.commit()
    tree.delete(selected_item)
    mb.showinfo("SUCCESS",'Author data deleted')

# End: Delete Author Function====================

# Begin: Update Author Function =======================
def select_data(tree):
    curItem = tree.focus()
    values = tree.item(curItem, 'values')
        
    f = Frame(r, width=400, height=400, background='grey')
    f.place(x=100, y=250)


    l1=Label(f, text='ID', width=8, font=('Times', 11, 'bold'))
    e1=Entry(f,textvariable=au_id, width=25)
    l1.place(x=50, y=30)
    e1.place(x=170, y=30)    
    
    l2=Label(f, text='First Name', width=8, font=('Times', 11, 'bold'))
    e2=Entry(f,textvariable=fName, width=25)
    l2.place(x=50, y=70)
    e2.place(x=170, y=70)

    l3=Label(f, text='Last Name', width=8, font=('Times', 11, 'bold'))
    e3=Entry(f,textvariable=lName, width=25)
    l3.place(x=50, y=110)
    e3.place(x=170, y=110)

    
    l4=Label(f, text='Phone', width=8, font=('Times', 11, 'bold'))
    e4=Entry(f,textvariable=phone, width=25)
    l4.place(x=50, y=150)
    e4.place(x=170, y=150)

    
    l5=Label(f, text='Address', width=8, font=('Times', 11, 'bold'))
    e5=Entry(f,textvariable=address, width=25)
    l5.place(x=50, y=190)
    e5.place(x=170, y=190)

    
    l6=Label(f, text='City', width=8, font=('Times', 11, 'bold'))
    e6=Entry(f,textvariable=city, width=25)
    l6.place(x=50, y=230)
    e6.place(x=170, y=230)


    l7=Label(f, text='State', width=8, font=('Times', 11, 'bold'))
    e7=Entry(f,textvariable=au_state, width=25)
    l7.place(x=50, y=270)
    e7.place(x=170, y=270)


    l8=Label(f, text='Zip', width=8, font=('Times', 11, 'bold'))
    e8=Entry(f,textvariable=au_zip, width=25)
    l8.place(x=50, y=310)
    e8.place(x=170, y=310)


    e1.insert(0,values[0])
    e2.insert(0,values[1])
    e3.insert(0,values[2])
    e4.insert(0,values[3])
    e5.insert(0,values[4])
    e6.insert(0,values[5])
    e7.insert(0,values[6])
    e8.insert(0,values[7])

    def update_data():
        nonlocal e1, e2, e3, e4, e5, e6, e7, e8, curItem, values
        a_id = au_id.get()
        a_fname=fName.get()
        a_lname = lName.get()
        a_phone = phone.get()
        a_address = address.get()
        a_city = city.get()
        a_state = au_state.get()
        a_zip = au_zip.get()
       
        update_sql = '''UPDATE authors SET au_id=%s, au_fname=%s, au_lname=%s, phone=%s, 
                    address=%s, city=%s, state=%s, zip=%s WHERE au_id=%s'''
        
        update_data = (a_id, a_fname, a_lname, a_phone, a_address, a_city, \
                          a_state, a_zip, values[0],)
        
        conn.execute(update_sql, update_data)
        connect.commit()

        tree.item(curItem,values=(a_id, a_fname, a_lname, a_phone, \
                                  a_address, a_city, a_state, a_zip))
        mb.showinfo('SUCCESS', 'Author data updated')

        e1.delete(0,END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0,END)
        e8.delete(0,END)
        f.destroy()

    savebutton = tk.Button(f, text="Update", command=update_data)
    savebutton.configure(font=('Times', 11, 'bold'), bg='green', fg='white')
    savebutton.place(x=100, y=360)
    cancelbutton = tk.Button(f, text="Close", command=f.destroy)
    cancelbutton.configure(font=('Times', 11, 'bold'), bg='red', fg='white')
    cancelbutton.place(x=200, y=360)

# End: Update Author Function =============================

insertbutton = tk.Button(r,text='Insert', command=lambda:add_data(tree))
insertbutton.configure(font=('calibri', 14, 'bold'), bg= 'green', fg='white')
insertbutton.place(x=200, y=260)

deletebutton = tk.Button(r,text='Delete', command=lambda:delete_data(tree))
deletebutton.configure(font=('calibri', 14, 'bold'), bg= 'red', fg='white')
deletebutton.place(x=300, y=260)

updatebutton = tk.Button(r,text='Update', command=lambda:select_data(tree))
updatebutton.configure(font=('calibri', 14, 'bold'), bg= 'blue', fg='white')
updatebutton.place(x=400, y=260)


r.mainloop()
