from datetime import datetime
import tkinter as tk
import mysql.connector
import tkinter.messagebox

#MySQL Server Connection
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="153Sahil*"
)

#Server Cursor
mycursor = mydb.cursor()

#Getting Into Database SEProject
mycursor.execute("use SEProject;")

def search(enter, password):
    mycursor.execute("select * from login where uname = '{}' or email = '{}' and pword = '{}';".format(enter, enter, password))
    arr = mycursor.fetchall()
    return arr

def submt():
    enter = UserID.get()

    pw = Password.get()

    chk = search(enter, pw)
    if chk == []:
        tk.messagebox.showinfo("Invalid Login", "Put in Correct Credentials")
    else:
        #Credentials Window
        windoc = tk.Toplevel()
        windoc.geometry('1920x1020+0+0')
        # windoc.configure(bg="#592E95")
        # windoc.configure(bg="#66E3B3")
        windoc.configure(bg="#89EAC4")
        
        mycursor.execute("select*from Employee where EmpID = '{}'".format(chk[0][0]))
        qr = mycursor.fetchall()
        qr = qr[0]
        windoc.title("{}".format(qr[0]))
        #975C8F

        lbg31 = tk.Label(windoc, image=bg3).place(x=100, y=130)
        lbg32 = tk.Label(windoc, image=bg3).place(x=1100, y=130)

        lid = tk.Label(windoc, bg="#89EAC4", text=qr[0], fg="#A65640", font=('Arial', 30)).place(x=150, y=30)
        lname = tk.Label(windoc, bg="#89EAC4", text=(qr[1] + "  " + qr[2]), fg="#A65640", font=('Georgia', 30)).place(x=500, y=30)
        
        pd = tk.Label(windoc, text="Personal Details:", bg="#592E95", fg="pink", font=('Arial', 30)).place(x=200, y=160)
        od = tk.Label(windoc, text="Organisational Details:", bg="#592E95", fg="skyblue", font=('Arial', 30)).place(x=1200, y=160)
        
        dob = qr[4].strftime("%d/%m/%y")
        p1 = tk.Label(windoc, text="Date Of Birth: " + dob, bg="#1B2068", fg="#FF69D0", font=('Arial', 20)).place(x=150, y=340)
        gender = "Male" if qr[3] == 'M' else "Female"
        p2 = tk.Label(windoc, text="Gender: " + gender, bg="#1B2068", fg="#FF69D0", font=('Arial', 20)).place(x=150, y=460)
        p3 = tk.Label(windoc, text="Email ID: " + qr[5], bg="#1B2068", fg="#FF69D0", font=('Arial', 20)).place(x=150, y=580)
        p4 = tk.Label(windoc, text="Phone Number: " + qr[6], bg="#1B2068", fg="#FF69D0", font=('Arial', 20)).place(x=150, y=700)
        p5 = tk.Label(windoc, text="Current Address: " + qr[7], bg="#1B2068", fg="#FF69D0", font=('Arial', 20)).place(x=150, y=820)

        o1 = tk.Label(windoc, text="Department: " + qr[8], bg="#550975", fg="#008EFF", font=('Arial', 20)).place(x=1150, y=280)
        o2 = tk.Label(windoc, text="Job Role: " + qr[9], bg="#550975", fg="#008EFF", font=('Arial', 20)).place(x=1150, y=380)
        djoined = qr[10].strftime("%d/%m/%y")
        o3 = tk.Label(windoc, text="Date OF Joining: " + djoined, bg="#550975", fg="#008EFF", font=('Arial', 20)).place(x=1150, y=480)
        o4 = tk.Label(windoc, text="Salary: " + str(qr[11]), bg="#550975", fg="#008EFF", font=('Arial', 20)).place(x=1150, y=580)
        empreg = "Yes" if qr[12] == 1 else "No"
        o5 = tk.Label(windoc, text="Registered for Login: " + empreg, bg="#550975", fg="#008EFF", font=('Arial', 20)).place(x=1150, y=680)
        o6 = tk.Label(windoc, text="Registration Key: " + qr[13], bg="#550975", fg="#008EFF", font=('Arial', 20)).place(x=1150, y=780)
        o7 = tk.Label(windoc, text="Laptop ID: " + qr[14], bg="#550975", fg="#008EFF", font=('Arial', 20)).place(x=1150, y=880)

        def change():
            #Changes Window
            changewin = tk.Toplevel()
            changewin.configure(bg='#4D329A')
            changewin.geometry('500x450+660+350')
            changewin.title("Change Your Credentials")

            ch1 = tk.Label(changewin, bg="#4D329A", fg='white', font=('Arial', 15), text="Enter the Field You want to Change:").place(x=50, y=50)
            che1 = tk.Entry(changewin, bg="#303030", fg='pink', font=('Arial', 15), width=25)
            che1.place(x=50, y=110)

            ch2 = tk.Label(changewin, bg="#4D329A", fg='white', font=('Arial', 15), text="Enter the Value You want to Have:").place(x=50, y=210)
            che2 = tk.Entry(changewin, bg="#303030", fg='pink', font=('Arial', 15), width=25)
            che2.place(x=50, y=270)

            def chg():
                t1 = che1.get()
                t2 = che2.get()
                mycursor.execute("insert into changes values('{}', '{}', '{}');".format(qr[0], t1, t2))
                mydb.commit()
                tk.messagebox.showinfo("Change Initialised", "Request has been sent to the System Admin")
                changewin.destroy()


            chsbm = tk.Button(changewin, bg="#313131", text="Submit", font=('Arial', 15), fg="pink", command=chg).place(x=200, y=350)

        changeB = tk.Button(windoc, bg="violet", text="Change Your Credentials", borderwidth=1, font=('Arial', 13), fg="#550975", command=change).place(x=1300, y=30)


#Login Window
window = tk.Tk()
window.geometry('1920x1020+0+0')
window.title("Login")

bg3 = tk.PhotoImage(file="BG3.png")
bg2 = tk.PhotoImage(file = "BG2.png")
bg1 = tk.PhotoImage(file = "BG1.png")
lbg1 = tk.Label(window, image=bg1).place(x=650, y=100)

Heading = tk.Label(window, bg="#960070", width=10, text="Login:", fg="pink", font=('Arial', 28)).place(x=840, y=150)

Label1 = tk.Label(window, bg="#860080", text="Username / EmailID:", fg="white", font=('Arial', 20)).place(x=700, y=280)
UserID = tk.Entry(window,bg="skyblue", fg="brown", font=('Arial', 17), width = 30)
UserID.place(x=700, y=370)

Label1 = tk.Label(window, bg="#660080", text="Password:", fg="white", font=('Arial', 20)).place(x=700, y=470)
Password = tk.Entry(window, bg="skyblue", fg="brown", font=('Arial', 17), width = 30, show="*")
Password.place(x=700, y=560)

Submit = tk.Button(window, bg="#DD6666", text="Submit", font=('Arial', 15), fg="#702070", command=submt).place(x=860, y=660)

RegLabel = tk.Label(window, bg="#505050", text="Don't have an Account? Register Here:", fg="white", font=('Arial', 13)).place(x=780, y=798)

def reg():
    #Registration Window
    windor = tk.Toplevel()
    windor.title("Register")
    windor.geometry('700x700+600+150')
    
    lbg2 = tk.Label(windor, image=bg2).place(x=0, y=0)

    lh = tk.Label(windor, text="Register Your Account:", bg="#960070", fg='pink', font=('Arial', 24), width=20).place(x=150, y=60)

    l0 = tk.Label(windor, text="Registration Key:", bg="#860080", fg="white", font=('Arial', 18)).place(x=50, y=200)
    t0 = tk.Entry(windor, bg="skyblue", fg="brown", font=('Arial', 16), width = 15)
    t0.place(x=260, y=202)

    lid = tk.Label(windor, text="Employee ID:", bg="#760080", fg="white", font=('Arial', 18)).place(x=50, y=300)
    tid = tk.Entry(windor, bg="skyblue", fg="brown", font=('Arial', 16), width = 15)
    tid.place(x=260, y=302)

    l1 = tk.Label(windor, text="Username:", bg="#660080", fg="white", font=('Arial', 18)).place(x=50, y=400)
    t1 = tk.Entry(windor, bg="skyblue", fg="brown", font=('Arial', 16), width = 30)
    t1.place(x=220, y=402)
    
    l2 = tk.Label(windor, text="Password:", bg="#560080", fg="white", font=('Arial', 18)).place(x=50, y=500)
    t2 = tk.Entry(windor, bg="skyblue", fg="brown", font=('Arial', 16), width = 30)
    t2.place(x=220, y=502)

    def ireg():
        regkey = t0.get()
        empid = tid.get()
        mycursor.execute("select email from Employee where EmpID = '{}' and regkey = '{}' and registered = false".format(empid, regkey))
        stremail = mycursor.fetchall()
        if stremail == []:
            tk.messagebox.showinfo("Error", "Put in Correct Credentials Or\nUse the Login Section if You have Already Registered")
            windor.destroy()
        else:
            un = t1.get()
            pw = t2.get()
            mycursor.execute("insert into login values('{}', '{}', '{}', '{}');".format(empid, un, stremail[0][0], pw))
            mycursor.execute("update employee set registered = true where EmpID = '{}'".format(empid))
            mydb.commit()
            tk.messagebox.showinfo("Success", "Your Account has been Registered\nNow Login using the Login Section")
            windor.destroy()

    RegisterB = tk.Button(windor, bg="#DD6666", text="Register", font=('Arial', 15), fg="#702070", command=ireg).place(x=310, y=600)

RegButton = tk.Button(bg="#313131", text="Register", font=('Arial', 13), fg="pink", command=reg).place(x=1090, y=795)

window.mainloop()

mycursor.close()
mydb.close()

# datetime.date(2002, 5, 3)  --> format to access date
