from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import *
import time

root = Tk()
root.title("currency converter")
root.geometry('1000x500+0+0')

bg_pic = Canvas(root, bg='blue', height=50, width=50)
#filename = PhotoImage(file=r"C:\Users\admin\Desktop\Converter\1234.png")      << Give the location of the picture in png format >>
#background_label = Label(root, image=filename)                                 << Uncomment the required lines of code to run them >>
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#bg_pic.pack()

heading = Label(root, text="The Currency Converter", font=('arial', 20, 'bold'), fg='blue', relief="raise").pack()

left_mainframe = Frame(root, width=660, height=400, bd=8, relief="raise")
left_mainframe.pack(side=LEFT)
right_mainframe = Frame(root, width=200, height=400, bd=8, relief="raise")
right_mainframe.pack(side=RIGHT)

date_of_order = StringVar()
from_currency = StringVar()
to_currency = StringVar()
convert = DoubleVar()
currency = DoubleVar()

fc = from_currency.get()


def conversion(fc):
    switcher = {
        "India (Rupees)": inr_conversion(),
        "USA (US Dollars)": usd_conversion(),
        "Canada (Canadian Dollars)": cad_conversion(),
        "Europe (Euro)": euro_conversion(),
        "Nigeria (Naira)": naira_conversion(),
        "Dubai (Dirham)": dirham_conversion(),
        "Korea (won)": won_conversion(),
        "Japan (Yen)": yen_conversion(),
        "Australia (Australian Dollars)": aud_conversion()
    }
    print(switcher.get(fc, "From Currency"))


def conversion2():
    conversion(fc)


def inr_conversion():
    if from_currency.get() == "India (Rupees)":
        if to_currency.get() == "USA (US Dollars)":
            convert1 = float(convert.get() * 0.014)
            convert2 = "$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian Dollars)":
            convert1 = float(convert.get() * 0.017)
            convert2 = "C$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            convert1 = float(convert.get() * 0.011)
            convert2 = "€", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            convert1 = float(convert.get() * 5.42)
            convert2 = "₦", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            convert1 = float(convert.get() * 0.050)
            convert2 = "D", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            convert1 = float(convert.get() * 15.09)
            convert2 = "₩", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            convert1 = float(convert.get() * 1.42)
            convert2 = "¥", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            convert1 = float(convert.get() * 0.018)
            convert2 = "A$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "India (Rupees)":
            error_popup()


def usd_conversion():
    if from_currency.get() == 'USA (US Dollars)':
        if to_currency.get() == "India (Rupees)":
            convert1 = float(convert.get() * 73.16)
            convert2 = "₹", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian Dollars)":
            convert1 = float(convert.get() * 1.27)
            convert2 = "C$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            convert1 = float(convert.get() * 0.83)
            convert2 = "€", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            convert1 = float(convert.get() * 396.19)
            convert2 = "₦", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            convert1 = float(convert.get() * 3.67)
            convert2 = "D", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            convert1 = float(convert.get() * 1104.26)
            convert2 = "₩", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            convert1 = float(convert.get() * 103.84)
            convert2 = "¥", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            convert1 = float(convert.get() * 1.30)
            convert2 = "A$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "USA (US Dollars)":
            error_popup()


def cad_conversion():
    if from_currency.get() == 'Canada (Canadian Dollars)':
        if to_currency.get() == "USA (US Dollars)":
            convert1 = float(convert.get() * 0.79)
            convert2 = "$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "India (Rupees)":
            convert1 = float(convert.get() * 57.60)
            convert2 = "₹", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            convert1 = float(convert.get() * 0.65)
            convert2 = "€", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            convert1 = float(convert.get() * 311.93)
            convert2 = "₦", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            convert1 = float(convert.get() * 2.89)
            convert2 = "D", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            convert1 = float(convert.get() * 869.21)
            convert2 = "₩", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            convert1 = float(convert.get() * 81.79)
            convert2 = "¥", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            convert1 = float(convert.get() * 1.02)
            convert2 = "A$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian Dollars)":
            error_popup()


def euro_conversion():
    if from_currency.get() == 'Europe (Euro)':
        if to_currency.get() == "USA (US Dollars)":
            convert1 = float(convert.get() * 1.21)
            convert2 = "$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian Dollars)":
            convert1 = float(convert.get() * 1.54)
            convert2 = "C$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "India (Rupees)":
            convert1 = float(convert.get() * 88.38)
            convert2 = "₹", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            convert1 = float(convert.get() * 478.58)
            convert2 = "₦", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            convert1 = float(convert.get() * 4.44)
            convert2 = "D", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            convert1 = float(convert.get() * 1333.89)
            convert2 = "₩", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            convert1 = float(convert.get() * 125.49)
            convert2 = "¥", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            convert1 = float(convert.get() * 1.57)
            convert2 = "A$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            error_popup()


def naira_conversion():
    if from_currency.get() == 'Nigeria (Naira)':
        if to_currency.get() == "USA (US Dollars)":
            convert1 = float(convert.get() * 0.0025)
            convert2 = "$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian Dollars)":
            convert1 = float(convert.get() * 0.0032)
            convert2 = "C$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            convert1 = float(convert.get() * 0.0021)
            convert2 = "€", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "India (Rupees)":
            convert1 = float(convert.get() * 0.18)
            convert2 = "₹", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            convert1 = float(convert.get() * 0.0093)
            convert2 = "D", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            convert1 = float(convert.get() * 2.79)
            convert2 = "₩", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            convert1 = float(convert.get() * 0.26)
            convert2 = "¥", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            convert1 = float(convert.get() * 0.0033)
            convert2 = "A$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            error_popup()


def won_conversion():
    if from_currency.get() == 'Korea (won)':
        if to_currency.get() == "USA (US Dollars)":
            convert1 = float(convert.get() * 0.00091)
            convert2 = "$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian dollar)":
            convert1 = float(convert.get() * 0.0012)
            convert2 = "C$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            convert1 = float(convert.get() * 0.00075)
            convert2 = "€", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            convert1 = float(convert.get() * 0.36)
            convert2 = "₦", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            convert1 = float(convert.get() * 0.0033)
            convert2 = "D", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "India (Rupees)":
            convert1 = float(convert.get() * 0.066)
            convert2 = "₹", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            convert1 = float(convert.get() * 0.094)
            convert2 = "¥", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            convert1 = float(convert.get() * 0.0012)
            convert2 = "A$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            error_popup()


def yen_conversion():
    if from_currency.get() == 'Japan (Yen)':
        if to_currency.get() == "USA (US Dollars)":
            convert1 = float(convert.get() * 0.0096)
            convert2 = "$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian Dollars)":
            convert1 = float(convert.get() * 0.012)
            convert2 = "C$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            convert1 = float(convert.get() * 0.0080)
            convert2 = "€", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            convert1 = float(convert.get() * 3.81)
            convert2 = "₦", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            convert1 = float(convert.get() * 0.035)
            convert2 = "D", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            convert1 = float(convert.get() * 10.63)
            convert2 = "₩", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "India (Rupees)":
            convert1 = float(convert.get() * 0.70)
            convert2 = "₹", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            convert1 = float(convert.get() * 0.012)
            convert2 = "A$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            error_popup()


def aud_conversion():
    if from_currency.get() == 'Australia (Australian Dollars)':
        if to_currency.get() == "USA (US Dollars)":
            convert1 = float(convert.get() * 0.77)
            convert2 = "$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian Dollars)":
            convert1 = float(convert.get() * 0.98)
            convert2 = "C$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            convert1 = float(convert.get() * 0.64)
            convert2 = "€", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            convert1 = float(convert.get() * 304.56)
            convert2 = "₦", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            convert1 = float(convert.get() * 2.82)
            convert2 = "D", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            convert1 = float(convert.get() * 850.62)
            convert2 = "₩", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            convert1 = float(convert.get() * 80.02)
            convert2 = "¥", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "India (Rupees)":
            convert1 = float(convert.get() * 56.24)
            convert2 = "₹", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            error_popup()


def dirham_conversion():
    if from_currency.get() == 'Dubai (Dirham)':
        if to_currency.get() == "USA (US Dollars)":
            convert1 = float(convert.get() * 0.27)
            convert2 = "$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Canada (Canadian Dollars)":
            convert1 = float(convert.get() * 0.35)
            convert2 = "C$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Europe (Euro)":
            convert1 = float(convert.get() * 0.23)
            convert2 = "€", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Nigeria (Naira)":
            convert1 = float(convert.get() * 107.87)
            convert2 = "₦", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "India (Rupees)":
            convert1 = float(convert.get() * 19.92)
            convert2 = "₹", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Korea (won)":
            convert1 = float(convert.get() * 300.64)
            convert2 = "₩", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Japan (Yen)":
            convert1 = float(convert.get() * 28.27)
            convert2 = "¥", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Australia (Australian Dollars)":
            convert1 = float(convert.get() * 0.35)
            convert2 = "A$", str('%.2f' % convert1)
            currency.set(convert2)
        elif to_currency.get() == "Dubai (Dirham)":
            error_popup()


def error_popup():
    error = tk.messagebox.showerror("ERROR!", "Please select some other country")
    return error


def prgm_exit():
    p_exit = tk.messagebox.askyesno("Exit System", "Do you want to quit?")
    if p_exit > 0:
        root.destroy()
        return


def reset():
    to_currency.set("To currency")
    from_currency.set("From Currency")
    convert.set("0.0")
    currency.set("0.0")


date_of_order.set(time.strftime("%B %d, %Y"))

ent_currency = Entry(left_mainframe, font=('cambria', 20, 'bold'), textvariable=convert, bd=2, width=20,
                     justify='center')
ent_currency.grid(row=0, column=1)

box1 = ttk.Combobox(left_mainframe, textvariable=from_currency, state='readonly', font=('cambria', 20, 'bold'),
                    width=20)
box1['values'] = ('From Currency', 'India (Rupees)', 'USA (US Dollars)', 'Canada (Canadian Dollars)', 'Europe (Euro)',
                  'Nigeria (Naira)', 'Dubai (Dirham)', 'Korea (won)', 'Japan (Yen)', 'Australia (Australian Dollars)')
box1.current(0)
box1.grid(row=0, column=2)

box2 = ttk.Combobox(left_mainframe, textvariable=to_currency, state='readonly', font=('cambria', 20, 'bold'),
                    width=20)
box2['values'] = ('To Currency', 'India (Rupees)', 'USA (US Dollars)', 'Canada (Canadian Dollars)', 'Europe (Euro)',
                  'Nigeria (Naira)', 'Dubai (Dirham)', 'Korea (won)', 'Japan (Yen)', 'Australia (Australian Dollars)')
box2.current(0)
box2.grid(row=4, column=2)

label_currency = Label(left_mainframe, font=('cambria', 20, 'bold'), textvariable=currency, bd=2, width=20,
                       bg='white', pady=2, padx=2, relief='sunken')
label_currency.grid(row=4, column=1)

label_date = Label(right_mainframe, font=('cambria', 20, 'bold'), textvariable=date_of_order, padx=2, pady=2, bd=2,
                   fg="black", width=15, justify='center')
label_date.grid(row=0, column=0, sticky=W)

button_convert = Button(right_mainframe, text='Convert', bd=2, fg="black", font=('cambria', 20, 'bold'), width=10,
                        height=1, command=conversion2).grid(row=1, column=0)
button_reset = Button(right_mainframe, text='Reset', bd=2, fg="black", font=('cambria', 20, 'bold'), width=10, height=1,
                      command=reset).grid(row=2, column=0)
button_exit = Button(right_mainframe, text='Exit', bd=2, fg="black", font=('cambria', 20, 'bold'), width=10, height=1,
                     command=prgm_exit).grid(row=3, column=0)

root.mainloop()
