from tkinter import *
from tkinter import simpledialog
import mysql.connector
import tkinter.messagebox as tmsg
import datetime

mydb = mysql.connector.connect(host='localhost', user='root', database='gaming_center')
mycursor = mydb.cursor(buffered=True)

xg = Tk()

xg.geometry("1366x768")
xg.minsize(1366, 768)
xg.maxsize(1366, 768)
xg.title("GAMING")
xg.wm_iconbitmap('TKLogo.ico')
img = PhotoImage(file='bg1.png')
background_label = Label(image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# TOP TITLE BOX

l1 = Label(xg, text="WELCOME TO BLAZE GAMING", font="calibri 20 bold", fg="WHITE", bg="BLACK")
l1.place(x=500, y=5)
# RIGHT TITLE BOX

l2 = Label(xg, text="CURRENT USERS", font="calibri 16 bold", fg="WHITE", bg="BLACK")
l2.place(x=1180, y=30)

# BUTTONS FOR LOGIN LOGOUT
photo = PhotoImage(file="Computer1.png")

def updateuser(USER_INP, number, pdate):
    sql = 'INSERT into xtreme_gaming (Login_ID, Pc_No, Date_Time_In) VALUES ( %s, %s, %s) '
    val = (USER_INP, number, pdate)
    mycursor.execute(sql, val)
    mydb.commit()
    sql = 'UPDATE pc_available SET login_ID = %s WHERE pc_no = %s'
    val = (USER_INP, number)
    mycursor.execute(sql, val)
    mydb.commit()


def updateuser1(number, pdate, p):
    sql = 'UPDATE xtreme_gaming SET Date_Time_Out = %s WHERE Pc_No = %s'
    val = (pdate, number)
    mycursor.execute(sql, val)
    mydb.commit()
    sql = 'UPDATE xtreme_gaming SET Game_Bill = %s WHERE Pc_No = %s'
    val = (p, number)
    mycursor.execute(sql, val)
    mydb.commit()
    sql = 'UPDATE pc_available SET login_ID = %s WHERE Pc_No = %s'
    val = ('EMPTY', number)
    mycursor.execute(sql, val)
    mydb.commit()


def btncommand(number):
    funct_dict = {1: b1, 2: b2, 3: b3,
                  4: b4, 5: b5, 6: b6,
                  7: b7, 8: b8, 9: b9,
                  10: b10}
    if funct_dict.get(number)['bg'] == 'RED':
        USER_INP = simpledialog.askstring(title="USER ID", prompt="ENTER LOGIN ID:", parent=xg)
        if USER_INP is not None:
            funct_dict.get(number)['bg'] = 'GREEN'
            if number == 1:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv1.set(USER_INP)
            elif number == 2:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv2.set(USER_INP)
            elif number == 3:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv3.set(USER_INP)
            elif number == 4:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv4.set(USER_INP)
            elif number == 5:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv5.set(USER_INP)
            elif number == 6:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv6.set(USER_INP)
            elif number == 7:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv7.set(USER_INP)
            elif number == 8:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv8.set(USER_INP)
            elif number == 9:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv9.set(USER_INP)
            elif number == 10:
                pdate = datetime.datetime.now()
                updateuser(USER_INP, number, pdate)
                sv10.set(USER_INP)
        else:
            funct_dict.get(number)['bg'] = 'RED'
            
    elif funct_dict.get(number)['bg'] == 'GREEN':
        funct_dict.get(number)['bg'] = 'RED'
        if number == 1:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv2.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 2:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv2.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 3:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv3.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 4:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv4.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 5:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv5.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 6:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv6.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 7:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv7.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 8:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv8.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 9:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv9.set("EMPTY")
            updateuser1(number, pdate, p)

        elif number == 10:
            p = 0
            query = ("SELECT * FROM xtreme_gaming WHERE Pc_No='%s'" % number)
            mycursor.execute(query)
            records = mycursor.fetchone()
            pdate = datetime.datetime.now()
            inhr = records[3].minute
            outhr = pdate.minute
            h = outhr - inhr
            if h == 240:
                p = 140
            else:
                p = p + 1.3 * h
            tmsg.showinfo("COST", "GRAND TOTAL: %s" % p)
            sv10.set("EMPTY")
            updateuser1(number, pdate, p)


b1 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(1))
b1.place(x=50, y=70)
b2 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(2))
b2.place(x=270, y=70)
b3 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(3))
b3.place(x=490, y=70)
b4 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(4))
b4.place(x=710, y=70)
b5 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(5))
b5.place(x=930, y=70)
b6 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(6))
b6.place(x=50, y=350)
b7 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(7))
b7.place(x=270, y=350)
b8 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(8))
b8.place(x=490, y=350)
b9 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(9))
b9.place(x=710, y=350)
b10 = Button(xg, image=photo, bg='RED', command=lambda: btncommand(10))
b10.place(x=930, y=350)

# Text for PcNo.
p1 = Label(xg, text="PC NO.1", fg="WHITE", bg="BLACK")
p1.place(x=124, y=215)
p2 = Label(xg, text="PC NO.2", fg="WHITE", bg="BLACK")
p2.place(x=345, y=215)
p3 = Label(xg, text="PC NO.3", fg="WHITE", bg="BLACK")
p3.place(x=565, y=215)
p4 = Label(xg, text="PC NO.4", fg="WHITE", bg="BLACK")
p4.place(x=788, y=215)
p5 = Label(xg, text="PC NO.5", fg="WHITE", bg="BLACK")
p5.place(x=1010, y=215)
p6 = Label(xg, text="PC NO.6", fg="WHITE", bg="BLACK")
p6.place(x=124, y=495)
p7 = Label(xg, text="PC NO.7", fg="WHITE", bg="BLACK")
p7.place(x=345, y=495)
p8 = Label(xg, text="PC NO.8", fg="WHITE", bg="BLACK")
p8.place(x=565, y=495)
p9 = Label(xg, text="PC NO.9", fg="WHITE", bg="BLACK")
p9.place(x=788, y=495)
p10 = Label(xg, text="PC NO.10", fg="WHITE", bg="BLACK")
p10.place(x=1010, y=495)

# STATUS Bar for Current User
sv1 = StringVar()
sv1.set("EMPTY")
sbar1 = Label(xg, textvariable=sv1, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar1.place(x=1200, y=70, relwidth=0.12, relheight=0.035)

sv2 = StringVar()
sv2.set("EMPTY")
sbar2 = Label(xg, textvariable=sv2, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar2.place(x=1200, y=100, relwidth=0.12, relheight=0.035)

sv3 = StringVar()
sv3.set("EMPTY")
sbar3 = Label(xg, textvariable=sv3, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar3.place(x=1200, y=130, relwidth=0.12, relheight=0.035)

sv4 = StringVar()
sv4.set("EMPTY")
sbar4 = Label(xg, textvariable=sv4, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar4.place(x=1200, y=160, relwidth=0.12, relheight=0.035)

sv5 = StringVar()
sv5.set("EMPTY")
sbar5 = Label(xg, textvariable=sv5, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar5.place(x=1200, y=190, relwidth=0.12, relheight=0.035)

sv6 = StringVar()
sv6.set("EMPTY")
sbar6 = Label(xg, textvariable=sv6, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar6.place(x=1200, y=220, relwidth=0.12, relheight=0.035)

sv7 = StringVar()
sv7.set("EMPTY")
sbar7 = Label(xg, textvariable=sv7, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar7.place(x=1200, y=250, relwidth=0.12, relheight=0.035)

sv8 = StringVar()
sv8.set("EMPTY")
sbar8 = Label(xg, textvariable=sv8, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar8.place(x=1200, y=280, relwidth=0.12, relheight=0.035)

sv9 = StringVar()
sv9.set("EMPTY")
sbar9 = Label(xg, textvariable=sv9, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar9.place(x=1200, y=310, relwidth=0.12, relheight=0.035)

sv10 = StringVar()
sv10.set("EMPTY")
sbar10 = Label(xg, textvariable=sv10, relief=SUNKEN, anchor="w", fg="WHITE", bg="BLACK")
sbar10.place(x=1200, y=340, relwidth=0.12, relheight=0.035)

xg.mainloop()
