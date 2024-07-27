from tkinter import *
import qrcode
from PIL import Image, ImageTk
class Qr_Generator:
    def __init__(self,  root):
        self.root = root
        self.root.geometry("900x600+200+50")
        self.root.title("QR Generator | Insane Person Identifier")
        self.root.resizable(False,False)

        title = Label(self.root,text="  QR Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        #***Insane Person Details Window***

        #***Variables***
        self.var_ins_code = StringVar()
        self.var_ins_name = StringVar()
        self.var_ins_age = StringVar()
        self.var_ins_ill = StringVar()
        self.var_ins_address = StringVar()
        self.var_ins_contact = StringVar()
        self.var_ins_sos = StringVar()
        ins_Frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        ins_Frame.place(x=50, y=100, width=500, height=440)

        ins_title=Label(ins_Frame,text="Shipment Details",font=("goudy old style", 20), bg='#053246', fg='white').place(x=0,y=0,relwidth=1)

        lbl_ins_code = Label(ins_Frame, text="Consignment ID", font=("times new roman",15,'bold'), bg='white').place(x=15,y=60)
        lbl_ins_name = Label(ins_Frame, text="Shipper Details", font=("times new roman", 15, 'bold'), bg='white').place(x=15,y=100)
        lbl_ins_Age = Label(ins_Frame, text="Means of Transport", font=("times new roman", 15, 'bold'), bg='white').place(x=15,y=140)
        lbl_ins_ill = Label(ins_Frame, text="Port / Place of Departure", font=("times new roman", 15, 'bold'), bg='white').place(x=15,y=180)
        lbl_ins_Address = Label(ins_Frame, text="Cargo Information", font=("times new roman", 15, 'bold'), bg='white').place(x=15,y=220)
        lbl_ins_contact = Label(ins_Frame, text="Gross Mass (Kg / Tonnes)", font=("times new roman", 15, 'bold'), bg='white').place(x=15,y=260)
        lbl_ins_SOS = Label(ins_Frame, text="Emergency Contact", font=("times new roman", 15, 'bold'), bg='white').place(x=15,y=300)

        txt_ins_code = Entry(ins_Frame, font=("times new roman", 15), textvariable=self.var_ins_code, bg='lightyellow').place(x=250, y=60)
        txt_ins_name = Entry(ins_Frame, font=("times new roman", 15), textvariable=self.var_ins_name, bg='lightyellow').place(x=250, y=100)
        txt_ins_Age = Entry(ins_Frame, font=("times new roman", 15), textvariable=self.var_ins_age, bg='lightyellow').place(x=250, y=140)
        txt_ins_ill = Entry(ins_Frame, font=("times new roman", 15), textvariable=self.var_ins_ill, bg='lightyellow').place(x=250, y=180)
        txt_ins_Address = Entry(ins_Frame, font=("times new roman", 15), textvariable=self.var_ins_address, bg='lightyellow').place(x=250, y=220)
        txt_ins_contact = Entry(ins_Frame, font=("times new roman", 15), textvariable=self.var_ins_contact, bg='lightyellow').place(x=250, y=260)
        txt_ins_SOS = Entry(ins_Frame, font=("times new roman", 15), textvariable=self.var_ins_sos, bg='lightyellow').place(x=250, y=300)

        btn_generate = Button(ins_Frame, text="QR Generate", command=self.generate, font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=350, width=170, height = 30)
        btn_clear = Button(ins_Frame, text="Clear", command=self.clear, font=("times new roman", 18, 'bold'), bg='#607d8b',fg='white').place(x=340, y=350, width=110, height=30)

        self.msg = ''
        self.lbl_msg = Label(ins_Frame, text=self.msg, font=("times new roman", 20, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0,y=390,relwidth=1)
        # ***Insane Person QR Code Window***
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=440)

        ins_title = Label(qr_Frame, text="Consignment Code", font=("goudy old style", 20), bg='#053246', fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code=Label(qr_Frame,text='No QR \nAvailable', font=('times new roman', 15), bg='#3f51b5', fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_ins_code.set('')
        self.var_ins_name.set('')
        self.var_ins_age.set('')
        self.var_ins_ill.set('')
        self.var_ins_address.set('')
        self.var_ins_contact.set('')
        self.var_ins_sos.set('')
        self.msg = ""
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        if self.var_ins_code.get()=='' or self.var_ins_name.get()=='' or self.var_ins_age.get()=='' or self.var_ins_ill.get()=='' or self.var_ins_address.get()=='' or self.var_ins_contact.get()=='' or self.var_ins_sos.get()=='':
            self.msg="All Fields Are Required...!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Patient ID: {self.var_ins_code.get()}\nPatinet Name: {self.var_ins_name.get()}\nAge: {self.var_ins_age.get()}\nIllness: {self.var_ins_ill.get()}\nAddress: {self.var_ins_address.get()}\nParent / Guardian: {self.var_ins_contact.get()}\nEmergency Contact: {self.var_ins_sos.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code.save("Codes/Consignment ID_"+str(self.var_ins_code.get())+'.png')

            #***QR Code Image Update***
            self.im = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)

            #***Updating Notification***
            self.msg = "QR Generated Successfully...!"
            self.lbl_msg.config(text=self.msg, fg='green')


root = Tk()
obj = Qr_Generator(root)
root.mainloop()
