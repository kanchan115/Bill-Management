from tkinter import *
import mysql.connector

con = mysql.connector.connect(host = 'localhost',user = 'root', password = 'Krishn@2004')
cur = con.cursor()
try:
    cur.execute("use registration")
except:
    cur.execute("create database registration")
    cur.execute("use registration")    

try:
    cur.execute("describe person")
except:    
    cur.execute("create table bili(bill_id int primary key auto_increment, total_bil varchar(250))")
    
    
def submit():

    cur.execute(f"insert into bili(total_bil) values ('{submitbill.get()}')")
    con.commit()
    
def reset():
    # Clears all the entry fields
    dosa.delete(0, END)
    cookies.delete(0, END)
    tea.delete(0, END)
    coffee.delete(0, END)
    juice.delete(0, END)
    pizza.delete(0, END)
    sandwich.delete(0, END)
    total_bill.set("")

def total():
    # Get values from entries and handle non-integer inputs
    try:
        a1 = int(dosa_var.get())
    except ValueError:
        a1 = 0
    try:
        a2 = int(cookies_var.get())
    except ValueError:
        a2 = 0
    try:
        a3 = int(tea_var.get())
    except ValueError:
        a3 = 0
    try:
        a4 = int(coffee_var.get())
    except ValueError:
        a4 = 0
    try:
        a5 = int(juice_var.get())
    except ValueError:
        a5 = 0
    try:
        a6 = int(pizza_var.get())
    except ValueError:
        a6 = 0
    try:
        a7 = int(sandwich_var.get())
    except ValueError:
        a7 = 0

    # Calculate total cost
    total_cost = (60 * a1 + 30 * a2 + 15 * a3 + 20 * a4 + 100 * a5 + 170 * a6 + 90 * a7)
    total_bill.set(f"Rs. {total_cost:.2f}")
    

    # Insert the sale record into the database

root = Tk()
root.geometry("1200x500")
root.title("Bill Management")
root.resizable(False, False)

# Variable definitions
dosa_var = StringVar()
cookies_var = StringVar()
tea_var = StringVar()
coffee_var = StringVar()
juice_var = StringVar()
pizza_var = StringVar()
sandwich_var = StringVar()
total_bill = StringVar()
submitbill = StringVar()

# Menu frame
menu_frame = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
menu_frame.place(x=10, y=118)
Label(menu_frame, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=80, y=0)

Label(menu_frame, text="Dosa.........Rs.60/plate", font=("Lucida Calligraphy", 15, 'bold'), fg="black", bg="lightgreen").place(x=10, y=100)
Label(menu_frame, text="Cookies......Rs.30/plate", font=("Lucida Calligraphy", 15, 'bold'), fg="black", bg="lightgreen").place(x=10, y=130)
Label(menu_frame, text="Tea..........Rs.15/plate", font=("Lucida Calligraphy", 15, 'bold'), fg="black", bg="lightgreen").place(x=10, y=160)
Label(menu_frame, text="Coffee.......Rs.20/plate", font=("Lucida Calligraphy", 15, 'bold'), fg="black", bg="lightgreen").place(x=10, y=190)
Label(menu_frame, text="Juice........Rs.100/plate", font=("Lucida Calligraphy", 15, 'bold'), fg="black", bg="lightgreen").place(x=10, y=220)
Label(menu_frame, text="Pizza........Rs.170/plate", font=("Lucida Calligraphy", 15, 'bold'), fg="black", bg="lightgreen").place(x=10, y=250)
Label(menu_frame, text="Sandwich....Rs.90/plate", font=("Lucida Calligraphy", 15, 'bold'), fg="black", bg="lightgreen").place(x=10, y=280)

# Bill frame
bill_frame = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
bill_frame.place(x=880, y=118)
Label(bill_frame, text="Bill", font=("calibri", 20), bg="lightyellow").place(x=120, y=10)
entry_total = Entry(bill_frame, font=("aria", 20, 'bold'), textvariable=total_bill, bd=6, width=15, bg="lightgreen")
entry_total.place(x=20, y=50)

Label(bill_frame, text="Enter Bill", font=("calibri", 20), bg="lightyellow").place(x=110, y=100)
billamt = Entry(bill_frame, font=("aria", 20, 'bold'), textvariable=submitbill, bd=6, width=15, bg="lightgreen")
billamt.place(x=20, y=150)

Button(bill_frame, text="SUBMIT", command=submit, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=9).place(x=110,y=200)



# Entry work
entry_frame = Frame(root, bd=5, height=370, width=300, relief=RAISED)
entry_frame.pack()

Label(entry_frame, text="Dosa", font=("aria", 20, 'bold'), width=12, fg="blue4").grid(row=1, column=0)
dosa = Entry(entry_frame, font=("aria", 20, 'bold'), textvariable=dosa_var, bd=6, width=8, bg="lightpink")
dosa.grid(row=1, column=1)

Label(entry_frame, text="Cookies", font=("aria", 20, 'bold'), width=12, fg="blue4").grid(row=2, column=0)
cookies = Entry(entry_frame, font=("aria", 20, 'bold'), textvariable=cookies_var, bd=6, width=8, bg="lightpink")
cookies.grid(row=2, column=1)

Label(entry_frame, text="Tea", font=("aria", 20, 'bold'), width=12, fg="blue4").grid(row=3, column=0)
tea = Entry(entry_frame, font=("aria", 20, 'bold'), textvariable=tea_var, bd=6, width=8, bg="lightpink")
tea.grid(row=3, column=1)

Label(entry_frame, text="Coffee", font=("aria", 20, 'bold'), width=12, fg="blue4").grid(row=4, column=0)
coffee = Entry(entry_frame, font=("aria", 20, 'bold'), textvariable=coffee_var, bd=6, width=8, bg="lightpink")
coffee.grid(row=4, column=1)

Label(entry_frame, text="Juice", font=("aria", 20, 'bold'), width=12, fg="blue4").grid(row=5, column=0)
juice = Entry(entry_frame, font=("aria", 20, 'bold'), textvariable=juice_var, bd=6, width=8, bg="lightpink")
juice.grid(row=5, column=1)

Label(entry_frame, text="Pizza", font=("aria", 20, 'bold'), width=12, fg="blue4").grid(row=6, column=0)
pizza = Entry(entry_frame, font=("aria", 20, 'bold'), textvariable=pizza_var, bd=6, width=8, bg="lightpink")
pizza.grid(row=6, column=1)

Label(entry_frame, text="Sandwich", font=("aria", 20, 'bold'), width=12, fg="blue4").grid(row=7, column=0)
sandwich = Entry(entry_frame, font=("aria", 20, 'bold'), textvariable=sandwich_var, bd=6, width=8, bg="lightpink")
sandwich.grid(row=7, column=1)

# Buttons
Button(entry_frame, text="RESET", command=reset, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=9).grid(row=9, column=0)
Button(entry_frame, text="TOTAL", command=total, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=9).grid(row=9, column=1)


root.mainloop()
