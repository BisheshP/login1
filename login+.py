from tkinter import*
import os
import random
import datetime

# def delete2():
#     screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def login_sucess():
    # global screen3
    class main:
        def __init__(self,master):
            self.master = master
            self.master.title("Billing Software")
            self.master.geometry("1300x700+0+0")
            # self.master.config(bg="black")
            self.master.resizable(0,0)
            bg_color = "#001a60"
            title = Label(self.master, text="B$B Mart", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman",30,"bold"), pady=2)
            title.pack(fill=X)
            #================ Date & Time =============================
            self.dt = datetime.date.today()
            date = Label(title, text=self.dt, font="arial 20 bold", bg=bg_color, fg="white")
            date.place(x=1080, y=10)
            
            #====================================Variables========================================
            #==================== Stationary =================================
            self.g_pen = IntVar()
            self.eraser = IntVar()
            self.marker = IntVar()
            self.n_book = IntVar()
            self.g_box = IntVar()
            self.m_pencil = IntVar()
            #==================== Grocery =================================
            self.rice = IntVar()
            self.bread = IntVar()
            self.flour = IntVar()
            self.fish = IntVar()
            self.sugar = IntVar()
            self.cheese = IntVar()
            #==================== Drinks =================================
            self.fanta = IntVar()
            self.real = IntVar()
            self.limca = IntVar()
            self.tuborg = IntVar()
            self.wine = IntVar()
            self.redbull = IntVar()
            #==================== Total Product Price and Tax Variable =================================
            self.stationary_price = StringVar()
            self.grocery_price = StringVar()
            self.drink_price = StringVar()

            self.total_tax = StringVar()
            self.total_amt = StringVar()
            self.received_amt = IntVar()

            #==================== Customer =================================
            self.c_name = StringVar()
            self.c_phn = StringVar()
            self.bill_no = StringVar()
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill = StringVar()

            #================== Costumer Detail Frame ====================
            F1 = LabelFrame(self.master, text="Customer Details", font=("times new roman",15,"bold"), bd=12, relief=GROOVE, fg="gold", bg=bg_color)
            F1.place(x=0, y=75, relwidth=1)

            name_l = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman",18,"bold"))
            name_l.pack(fill=BOTH, expand=True, side=LEFT)
            name_en=Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN)
            name_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)
            
            phn_l = Label(F1, text="Mobile No.", bg=bg_color, fg="white", font=("times new roman",18,"bold"))
            phn_l.pack(fill=BOTH, expand=True, side=LEFT)
            phn_en = Entry(F1, width=15, textvariable=self.c_phn, font="arial 15", bd=7, relief=SUNKEN)
            phn_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)

            billno_l = Label(F1, text="Customer Bill No.", bg=bg_color, fg="white", font=("times new roman",18,"bold"))
            billno_l.pack(fill=BOTH, expand=True, side=LEFT)
            billno_en =Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN)
            billno_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)
            
            search_btn = Button(F1, text="Search", width=10, bd=7, font="arial 12 bold")
            search_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=12, pady=3)

            #================== Stationary Frame ===================
            F2 = LabelFrame(self.master, text="Stationary", bd=8, relief=GROOVE, font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
            F2.place(x=364, y=165, width=325, height=380)

            g_pen_l = Label(F2, text="Gel Pen", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            g_pen_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            g_pen_en = Entry(F2, textvariable=self.g_pen, width=10, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            g_pen_en.grid(row=0, column=1, padx=10, pady=10)

            eraser_l = Label(F2, text="Eraser", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            eraser_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            eraser_en = Entry(F2, width=10, textvariable=self.eraser, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            eraser_en.grid(row=1, column=1, padx=10, pady=10)

            marker_l = Label(F2, text="Marker", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            marker_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            marker_en = Entry(F2, width=10, textvariable=self.marker, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            marker_en.grid(row=2, column=1, padx=10, pady=10)

            n_book_l = Label(F2, text="Notebook", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            n_book_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            n_book_en = Entry(F2, width=10, textvariable=self.n_book, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            n_book_en.grid(row=3, column=1, padx=10, pady=10)

            g_box_l = Label(F2, text="Geometry Box", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            g_box_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
            g_box_en = Entry(F2, width=10, textvariable=self.g_box, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            g_box_en.grid(row=4, column=1, padx=10, pady=10)

            c_pencil_l = Label(F2, text="Color Pencils", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            c_pencil_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
            c_pencil_en = Entry(F2, width=10, textvariable=self.m_pencil, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            c_pencil_en.grid(row=5, column=1, padx=10, pady=10)
            


            #================== Grocery Frame =====================
            F3 = LabelFrame(self.master, text="Grocery", bd=8, relief=GROOVE, font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
            F3.place(x=694, y=165, width=325, height=380)

            rice_l = Label(F3, text="Rice", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            rice_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            rice_en = Entry(F3, width=10, textvariable=self.rice, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            rice_en.grid(row=0, column=1, padx=10, pady=10)

            bread_l = Label(F3, text="Brown Bread", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            bread_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            bread_en = Entry(F3, width=10, textvariable=self.bread, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            bread_en.grid(row=1, column=1, padx=10, pady=10)

            flour_l = Label(F3, text="Flour", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            flour_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            flour_en = Entry(F3, width=10, textvariable=self.flour, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            flour_en.grid(row=2, column=1, padx=10, pady=10)

            fish_l = Label(F3, text="Fish", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            fish_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            fish_en = Entry(F3, width=10, textvariable=self.fish, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            fish_en.grid(row=3, column=1, padx=10, pady=10)

            sugar_l = Label(F3, text="Sugar", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            sugar_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
            sugar_en = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            sugar_en.grid(row=4, column=1, padx=10, pady=10)

            cheese_l = Label(F3, text="Cheese", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            cheese_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
            cheese_en = Entry(F3, width=10, textvariable=self.cheese, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            cheese_en.grid(row=5, column=1, padx=10, pady=10)
            

            #================== Drinks Frame ======================
            F4 = LabelFrame(self.master, text="Drinks", bd=8, relief=GROOVE, font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
            F4.place(x=1024, y=165, width=275, height=380)

            fanta_l = Label(F4, text="Fanta", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            fanta_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            fanta_en = Entry(F4, width=10, textvariable=self.fanta, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            fanta_en.grid(row=0, column=1, padx=10, pady=10)

            real_l = Label(F4, text="Real", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            real_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            real_en = Entry(F4, width=10, textvariable=self.real, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            real_en.grid(row=1, column=1, padx=10, pady=10)

            limca_l = Label(F4, text="Limca", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            limca_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            limca_en = Entry(F4, width=10, textvariable=self.limca, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            limca_en.grid(row=2, column=1, padx=10, pady=10)

            tuborg_l = Label(F4, text="Tuborg", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            tuborg_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            tuborg_en = Entry(F4, width=10, textvariable=self.tuborg, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            tuborg_en.grid(row=3, column=1, padx=10, pady=10)

            wine_l = Label(F4, text="Wine", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            wine_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
            wine_en = Entry(F4, width=10, textvariable=self.wine, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            wine_en.grid(row=4, column=1, padx=10, pady=10)

            redbull_l = Label(F4, text="Redbull", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgreen")
            redbull_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
            redbull_en = Entry(F4, width=10,textvariable=self.redbull, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
            redbull_en.grid(row=5, column=1, padx=10, pady=10)

            #================== Receipt Area =========================
            F5 = Frame(self.master, bd=5, relief=GROOVE)
            F5.place(x=5, y=165, width=355, height=380)
            header = Label(F5, text="Receipt", font="arial 15 bold", bd=7, relief=GROOVE)
            header.pack(fill=X)
            scrol_y = Scrollbar(F5, orient=VERTICAL)
            self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
            scrol_y.pack(side=RIGHT, fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH, expand=True)

            #================== Button Frame ======================
            F6 = LabelFrame(self.master, text="Bill Menu", bd=8, relief=GROOVE, font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
            F6.place(x=0, y=548, relwidth=1, height=152)

            R1_l = Label(F6, text="Total Stationary Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=0, column=0, padx=10, pady=1, sticky="w")
            R1_en = Entry(F6, textvariable=self.stationary_price, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=3)

            R2_l = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=1, column=0, padx=10, pady=1, sticky="w")
            R2_en = Entry(F6, textvariable=self.grocery_price, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=3)

            R3_l = Label(F6, text="Total Drinks Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=2, column=0, padx=10, pady=1, sticky="w")
            R3_en = Entry(F6, textvariable=self.drink_price, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=3)
            
            R4_l = Label(F6, text="Total Tax", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=0, column=2, padx=10, pady=1, sticky="w")
            R4_en = Entry(F6, textvariable=self.total_tax, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

            R5_l = Label(F6, text="Total Amount", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=1, column=2, padx=10, pady=1, sticky="w")
            R5_en = Entry(F6, textvariable=self.total_amt, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

            R_l = Label(F6, text="Received Amount", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=2, column=2, padx=10, pady=1, sticky="w")
            R_en = Entry(F6, textvariable=self.received_amt, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

            btn_F = Frame(F6, bd=7, relief=GROOVE)
            btn_F.place(x=715, y=5, width=570, height=105)

            total_btn = Button(btn_F, command=self.total, text="Total", bg=bg_color, fg="white", pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=0, padx=4, pady=10)
            Gbill_btn = Button(btn_F, text="Generate Bill",command=self.receipt_area, bg=bg_color, fg="white", pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=1, padx=4, pady=5)
            Clear_btn = Button(btn_F, text="Clear", bg=bg_color, fg="white", pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=2, padx=4, pady=5)
            Exit_btn = Button(btn_F, text="Exit", bg=bg_color, fg="white", pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=3, padx=4, pady=5)
            self.welcome_receipt()

        def total(self):
            self.s_gp_p = self.g_pen.get()*30
            self.s_e_p = self.eraser.get()*50
            self.s_m_p = self.marker.get()*50
            self.s_nb_p = self.n_book.get()*100
            self.s_gb_p = self.g_box.get()*450
            self.s_mp_p = self.m_pencil.get()*150
            self.total_stationary_price = float(
                                            self.s_gp_p+
                                            self.s_e_p+
                                            self.s_m_p+
                                            self.s_nb_p+
                                            self.s_gb_p+
                                            self.s_mp_p
                                            )
            self.stationary_price.set("Rs. "+str(self.total_stationary_price))

            self.g_r_p = self.rice.get()*2650
            self.g_b_p = self.bread.get()*80
            self.g_fl_p = self.flour.get()*350
            self.g_fi_p = self.fish.get()*500
            self.g_s_p = self.sugar.get()*72
            self.g_c_p = self.cheese.get()*200
            self.total_grocery_price = float(
                                            self.g_r_p+
                                            self.g_b_p+
                                            self.g_fl_p+
                                            self.g_fi_p+
                                            self.g_s_p+
                                            self.g_c_p
                                            )
            self.grocery_price.set("Rs. "+str(self.total_grocery_price))

            self.d_f_p = self.fanta.get()*220
            self.d_r_p = self.real.get()*180
            self.d_l_p = self.limca.get()*150
            self.d_t_p = self.tuborg.get()*340
            self.d_w_p = self.wine.get()*2100
            self.d_rb_p = self.redbull.get()*110
            self.total_drink_price = float(
                                            self.d_f_p+
                                            self.d_r_p+
                                            self.d_l_p+
                                            self.d_t_p+
                                            self.d_w_p+
                                            self.d_rb_p
                                            )
            self.drink_price.set("Rs. "+str(self.total_drink_price))

            self.ttl_tax = (round(
                                ((self.total_stationary_price*0.05)+
                                (self.total_grocery_price*0.01)+
                                (self.total_drink_price*0.03)),2)
                            )
            self.total_tax.set("Rs. "+str(self.ttl_tax))

            self.ttl_amt = (round(
                                ((self.total_stationary_price)+
                                (self.total_grocery_price)+
                                (self.total_drink_price)+
                                (self.ttl_tax)),2)
                            )
            self.total_amt.set("Rs. "+str(self.ttl_amt))


        def welcome_receipt(self):
            self.datetime = datetime.datetime.today().replace(microsecond=0)
            self.txtarea.delete("1.0",END)
            self.txtarea.insert(END, "\t    B$B Mart Pvt.Ltd \n\t\tBansbari\n")
            self.txtarea.insert(END, f"\n Bill No.  : {self.bill_no.get()}")
            self.txtarea.insert(END, f"\n Customer  : {self.c_name.get()}")
            self.txtarea.insert(END, f"\n Phone No. : {self.c_phn.get()}")
            self.txtarea.insert(END, f"\n P.Time    : {self.datetime}")
            self.txtarea.insert(END, f"\n----------------------------------------")
            self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
            self.txtarea.insert(END, f"\n----------------------------------------")
        def receipt_area(self):
            self.received = self.received_amt.get()
            self.return_amt = (round(
                                (float(self.received) - 
                                self.ttl_amt),2)                    
                                )

            self.welcome_receipt()
            #--------- Stationary ------------
            if self.g_pen.get() !=0:
                self.txtarea.insert(END, f"\n Gel Pen\t\t{self.g_pen.get()}\t\t{self.s_gp_p}")   
            if self.eraser.get() !=0:
                self.txtarea.insert(END, f"\n Eraser\t\t{self.eraser.get()}\t\t{self.s_e_p}")   
            if self.marker.get() !=0:
                self.txtarea.insert(END, f"\n Marker\t\t{self.marker.get()}\t\t{self.s_m_p}")   
            if self.n_book.get() !=0:
                self.txtarea.insert(END, f"\n Notebook\t\t{self.n_book.get()}\t\t{self.s_nb_p}")   
            if self.g_box.get() !=0:
                self.txtarea.insert(END, f"\n Geometry Box\t\t{self.g_box.get()}\t\t{self.s_gb_p}")   
            if self.m_pencil.get() !=0:
                self.txtarea.insert(END, f"\n Magic Pencils\t\t{self.m_pencil.get()}\t\t{self.s_mp_p}")

            #--------- Grocery ------------
            if self.rice.get() !=0:
                self.txtarea.insert(END, f"\n Gel Pen\t\t{self.rice.get()}\t\t{self.g_r_p}")   
            if self.bread.get() !=0:
                self.txtarea.insert(END, f"\n Eraser\t\t{self.bread.get()}\t\t{self.g_b_p}")   
            if self.flour.get() !=0:
                self.txtarea.insert(END, f"\n Marker\t\t{self.flour.get()}\t\t{self.g_fl_p}")   
            if self.fish.get() !=0:
                self.txtarea.insert(END, f"\n Notebook\t\t{self.fish.get()}\t\t{self.g_fi_p}")   
            if self.sugar.get() !=0:
                self.txtarea.insert(END, f"\n Geometry Box\t\t{self.sugar.get()}\t\t{self.g_s_p}")   
            if self.cheese.get() !=0:
                self.txtarea.insert(END, f"\n Magic Pencils\t\t{self.cheese.get()}\t\t{self.g_c_p}")

            #--------- Drinks ------------
            if self.fanta.get() !=0:
                self.txtarea.insert(END, f"\n Gel Pen\t\t{self.fanta.get()}\t\t{self.d_f_p}")   
            if self.real.get() !=0:
                self.txtarea.insert(END, f"\n Eraser\t\t{self.real.get()}\t\t{self.d_r_p}")   
            if self.limca.get() !=0:
                self.txtarea.insert(END, f"\n Marker\t\t{self.limca.get()}\t\t{self.d_l_p}")   
            if self.tuborg.get() !=0:
                self.txtarea.insert(END, f"\n Notebook\t\t{self.tuborg.get()}\t\t{self.d_t_p}")   
            if self.wine.get() !=0:
                self.txtarea.insert(END, f"\n Geometry Box\t\t{self.wine.get()}\t\t{self.d_w_p}")   
            if self.redbull.get() !=0:
                self.txtarea.insert(END, f"\n Magic Pencils\t\t{self.redbull.get()}\t\t{self.d_rb_p}") 

            self.txtarea.insert(END, f"\n----------------------------------------")
            if self.stationary_price.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Stationary Price:\t\tRs. {self.total_stationary_price}")
            if self.grocery_price.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Price   :\t\tRs. {self.total_grocery_price}")
            if self.drink_price.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Drinks Price    :\t\tRs. {self.total_drink_price}")
            self.txtarea.insert(END, f"\n Total Tax       :\t\tRs. {self.ttl_tax}")
            self.txtarea.insert(END, f"\n----------------------------------------")
            #if !=0 then..... use garne
            self.txtarea.insert(END, f"\n Total Amount    :\t\tRs. {self.ttl_amt}")
            self.txtarea.insert(END, f"\n----------------------------------------")
            self.txtarea.insert(END, f"\n Received Amount :\t\tRs. {self.received}")
            self.txtarea.insert(END, f"\n Return Amount   :\t\tRs. {self.return_amt}")
            self.txtarea.insert(END, f"\n****************************************")
            self.txtarea.insert(END, "\n\t\tTHANK YOU!\n\t       VISIT AGAIN")
            self.txtarea.insert(END, f"\n****************************************")
    screen3 = Toplevel(screen)
    main(screen3)

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text = "Password Error").pack()
    Button(screen4, text = "OK", command = delete3)

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text = "Username Not Found").pack()
    Button(screen5, text = "OK", command = delete4)


def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1, text = "Registration Success", fg = "green", font = ("calibri",11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
            screen2.destroy()
        else:
            password_not_recognised()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes1.0", bg = "grey", width = 300, height = 2,font = ("Calibri,13")).pack()
    Label(text = "").pack()
    Button(text = "Login",height = 2, width = 30, command = login).pack()
    Label(text = "").pack()
    Button(text = "Register",height = 2, width = 30, command = register).pack()
    screen.mainloop()


main_screen()
