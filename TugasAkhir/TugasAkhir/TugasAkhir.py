#import modules
 
from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox 


class Setget:
    def __init__(self, makan2, des1):
        self.makan2 = makan2
        self.des1 = des1

    def makan2_set(self):
        if self.makan2 == 1:
            self.des1="Makan"
        if self.makan2 == 2:
            self.des1="BAB"
        if self.makan2 == 3:
            self.des1="BAK"
        if self.makan2 == 0:
            self.des1=("Error","BELUM MEMILIH AKTIVITAS")

    def makan2_get(self):
            return self.des1




# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Pendaftaran Hewan")
    register_screen.geometry("300x250")
 
    global namahewan
    global spesies
    global namahewan_entry
    global spesies_entry
    namahewan = StringVar()
    spesies = StringVar()
 
    Label(register_screen, text="Silahkan Masukan Nama hewan dan Spesies").pack()
    Label(register_screen, text="").pack()
    namahewan_lable = Label(register_screen, text="Nama Hewan")
    namahewan_lable.pack()
    namahewan_entry = Entry(register_screen, textvariable=namahewan)
    namahewan_entry.pack()
    spesies_lable = Label(register_screen, text="Spesies")
    spesies_lable.pack()
    spesies_entry = Entry(register_screen, textvariable=spesies)
    spesies_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Daftarkan", width=10, height=1, command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Silahkan Login").pack()
    Label(login_screen, text="").pack()
 
    global namahewan_verify
    global spesies_verify
 
    namahewan_verify = StringVar()
    spesies_verify = StringVar()
 
    global namahewan_login_entry
    global spesies_login_entry
 
    Label(login_screen, text="Nama Hewan").pack()
    namahewan_login_entry = Entry(login_screen, textvariable=namahewan_verify)
    namahewan_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Spesies").pack()
    spesies_login_entry = Entry(login_screen, textvariable=spesies_verify)
    spesies_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Tambahkan Aktivitas", width=17, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    namahewan_info = namahewan.get()
    spesies_info = spesies.get()
 
    file = open(namahewan_info, "w")
    file.write(namahewan_info + "\n")
    file.write(spesies_info)
    file.close()
 
    namahewan_entry.delete(0, END)
    spesies_entry.delete(0, END)
 
    Label(register_screen, text="Pendaftaran Hewan Berhasil", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    namahewan1 = namahewan_verify.get()
    spesies1 = spesies_verify.get()
    namahewan_login_entry.delete(0, END)
    spesies_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if namahewan1 in list_of_files:
        file1 = open(namahewan1, "r")
        verify = file1.read().splitlines()
        if spesies1 in verify:
            login_sucess()
 
        else:
            spesies_not_recognised()
    else:
        namahewan_not_found()
 
# Hewan terdaftar
 
def login_sucess():
    global hewan_terdaftar
    hewan_terdaftar = Toplevel(login_screen)
    hewan_terdaftar.title("spesies")
    hewan_terdaftar.geometry("150x100")
    Label(hewan_terdaftar, text="Hewan Terdaftar").pack()
    Button(hewan_terdaftar, text="OK", command=ok).pack() 

# Spesies hewan tidak sesuai

def spesies_not_recognised():
    global spesies_not_recog_screen
    spesies_not_recog_screen = Toplevel(login_screen)
    spesies_not_recog_screen.title("Spesies Tidak Sesuai")
    spesies_not_recog_screen.geometry("150x100")
    Label(spesies_not_recog_screen, text="Spesies Tidak Sesuai").pack()
    Button(spesies_not_recog_screen, text="OK", command=delete_spesies_not_recognised).pack()

# Hewan belum terdaftar
 
def namahewan_not_found():
    global namahewan_not_found_screen
    namahewan_not_found_screen = Toplevel(login_screen)
    namahewan_not_found_screen.title("Hewan Belum Terdaftar")
    namahewan_not_found_screen.geometry("150x100")
    Label(namahewan_not_found_screen, text="Hewan Belum Terdaftar").pack()
    Button(namahewan_not_found_screen, text="OK", command=delete_namahewan_not_found_screen).pack()

def ok():
    global aktivitas
    global radio_aktivitas
    aktivitas = Toplevel(hewan_terdaftar)
    aktivitas.geometry("250x150")
    aktivitas.title("Pencatatan aktivitas hewan")
    Label(aktivitas, text="SILAHKAN PILIH AKTIVITAS HEWAN ANDA").pack()
    radio_aktivitas = IntVar()
    R1 = Radiobutton(aktivitas, text="MAKAN", variable=radio_aktivitas, value=1).place(x=90, y=30) 
    R2 = Radiobutton(aktivitas, text="BAB", variable=radio_aktivitas, value=2).place(x=90, y=50) 
    R3 = Radiobutton(aktivitas, text="BAK", variable=radio_aktivitas, value=3).place(x=90, y=70) 
    btn2 = Button(aktivitas, command = submit, text="SUBMIT").place(x=100,y=100)

def submit():
    global kondisi_aktivitas
    global stringjenis
    global stringjumlah
    global radio

    radio_aktivitas_radio_aktivitas = radio_aktivitas.get()

    if radio_aktivitas.get() == 0:
        messagebox.showerror("Error","BELUM MEMILIH AKTIVITAS")
        return

    if radio_aktivitas.get() == 1:
        kondisi_aktivitas = Toplevel(aktivitas)
        kondisi_aktivitas.title("Kondisi Pakan")
        kondisi_aktivitas.geometry("300x200")
        Label(kondisi_aktivitas, text="SILAHKAN MASUKAN JENIS MAKANAN").pack()
        lbjenis = Label(kondisi_aktivitas, text = "Jenis Makanan\t:").place(x = 25,y = 30)    
        lbkondisi = Label(kondisi_aktivitas, text = "Kondisi Makanan\t:").place(x = 25, y=60)
        lbjumlah = Label(kondisi_aktivitas, text = "Jumlah Makanan\t:").place(x = 25, y=130)
        stringjenis = StringVar()
        stringjumlah = StringVar()
        ijenis = Entry(kondisi_aktivitas, width = 20, textvariable=stringjenis).place(x = 130, y = 30) 
        ijumlah = Entry(kondisi_aktivitas, width = 20, textvariable=stringjumlah).place(x = 130, y = 130) 
        radio = IntVar()
        R1 = Radiobutton(kondisi_aktivitas, text="Fresh", variable=radio, value=1).place(x=130, y=60)  
        R2 = Radiobutton(kondisi_aktivitas, text="Olahan", variable=radio, value=2).place(x=130, y=80)
        btn1 = Button(kondisi_aktivitas, command = catatanmakan, text="SUBMIT").place(x=130,y=170)

    if radio_aktivitas.get() == 2:
        kondisi_aktivitas = Toplevel(aktivitas)
        kondisi_aktivitas.title("Jasa Open Trip - Data Diri")
        kondisi_aktivitas.geometry("300x200")
        Label(kondisi_aktivitas, text="KONDISI KOTORAN").pack()
        lbjk = Label(kondisi_aktivitas, text = "Kondisi\t:").place(x = 30, y=60)
        stringjenis = StringVar()
        stringjumlah = StringVar()
        radio = IntVar()
        R1 = Radiobutton(kondisi_aktivitas, text="Normal", variable=radio, value=1).place(x=105, y=60)  
        R2 = Radiobutton(kondisi_aktivitas, text="Tidak Nomal", variable=radio, value=2).place(x=105, y=80)
        btn1 = Button(kondisi_aktivitas, command = catatanbab, text="SUBMIT").place(x=120,y=170)

    if radio_aktivitas.get() == 3:
        kondisi_aktivitas = Toplevel(aktivitas)
        kondisi_aktivitas.title("Jasa Open Trip - Data Diri")
        kondisi_aktivitas.geometry("300x200")
        Label(kondisi_aktivitas, text="KONDISI KOTORAN").pack()
        lbjk = Label(kondisi_aktivitas, text = "Kondisi\t:").place(x = 30, y=60)
        stringjenis = StringVar()
        stringjumlah = StringVar()
        radio = IntVar()
        R1 = Radiobutton(kondisi_aktivitas, text="Normal", variable=radio, value=1).place(x=105, y=60)  
        R2 = Radiobutton(kondisi_aktivitas, text="Tidak Nomal", variable=radio, value=2).place(x=105, y=80)
        btn1 = Button(kondisi_aktivitas, command = catatanbak, text="SUBMIT").place(x=120,y=170)

def catatanmakan():
    global strukanda
    strukanda = Toplevel(kondisi_aktivitas)
    strukanda.geometry("200x200")
    strukanda.title("CATATAN AKTIVITAS")
    Label(strukanda, text="CATATAN AKTIVITAS").pack()
 
    
    struk_stringjenis = stringjenis.get()
    struk_stringjumlah = stringjumlah.get()
    radio_radio      = radio.get()
    r_destinasi      = radio_aktivitas.get()
    

    if len(struk_stringjenis) == 0:
        messagebox.showerror("Error","BELUM MENGISI JENIS PAKAN")
        return
    if radio_radio == 0:
        messagebox.showerror("Error","BELUM MEMILIH KONDISI PAKAN")
        return
    if radio.get() == 1:
         kondisi ="Fresh"
    if radio.get() == 2:
         kondisi ="Olahan"
    if radio_aktivitas.get() == 0:
        messagebox.showerror("Error","BELUM MEMILIH AKTIVITAS")
        return
    
    keluar = Setget(radio_aktivitas.get(), "")
    keluar.makan2_set()

    Label(strukanda, text="AKTIVITAS").place(x=30,y=50)
    Label(strukanda, text=keluar.makan2_get()).place(x=30,y=70)
    Label(strukanda, text="KETERANGAN").place(x=30,y=100)
    Label(strukanda, text="Jenis Makanan      :  " + struk_stringjenis).place(x=30,y=120)
    Label(strukanda, text="Kondisi Makanan    :  " + kondisi).place(x=30,y=140)
    Label(strukanda, text="Jumlah Makanan       :  " + struk_stringjumlah).place(x=30,y=160)



def catatanbab():
    global strukanda
    strukanda = Toplevel(kondisi_aktivitas)
    strukanda.geometry("200x200")
    strukanda.title("CATATAN AKTIVITAS")
    Label(strukanda, text="CATATAN AKTIVITAS").pack()
    
    radio_radio      = radio.get()
    r_destinasi      = radio_aktivitas.get()

    if radio_radio == 0:
        messagebox.showerror("Error","BELUM MEMILIH KONDISI KOTORAN")
        return
    if radio.get() == 1:
         kondisi ="Normal"
    if radio.get() == 2:
         kondisi ="Tidak Normal"
    if radio_aktivitas.get() == 0:
        messagebox.showerror("Error","BELUM MEMILIH AKTIVITAS")
        return
    
    keluar = Setget(radio_aktivitas.get(), "")
    keluar.makan2_set()
 
    Label(strukanda, text="AKTIVITAS").place(x=30,y=50)
    Label(strukanda, text=keluar.makan2_get()).place(x=30,y=70)
    Label(strukanda, text="KETERANGAN").place(x=30,y=100)
    Label(strukanda, text="Kondisi Kotoran   :  " + kondisi).place(x=30,y=140)



def catatanbak():
    global strukanda
    strukanda = Toplevel(kondisi_aktivitas)
    strukanda.geometry("200x200")
    strukanda.title("CATATAN AKTIVITAS")
    Label(strukanda, text="CATATAN AKTIVITAS").pack()

    radio_radio      = radio.get()
    r_destinasi      = radio_aktivitas.get()

    if radio_radio == 0:
        messagebox.showerror("Error","BELUM MEMILIH KONDISI KOTORAN")
        return
    if radio.get() == 1:
         kondisi ="Normal"
    if radio.get() == 2:
         kondisi ="Tidak Normal"
    if radio_aktivitas.get() == 0:
        messagebox.showerror("Error","BELUM MEMILIH AKTIVITAS")
        return
    
    keluar = Setget(radio_aktivitas.get(), "")
    keluar.makan2_set()

 
    Label(strukanda, text="AKTIVITAS").place(x=30,y=50)
    Label(strukanda, text=keluar.makan2_get()).place(x=30,y=70)
    Label(strukanda, text="KETERANGAN").place(x=30,y=100)
    Label(strukanda, text="Kondisi Kotoran   :  " + kondisi).place(x=30,y=140)

# Deleting popups

def del_login_screen():
    login_screen.destroy()
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_spesies_not_recognised():
    spesies_not_recog_screen.destroy()
 
 
def delete_namahewan_not_found_screen():
    namahewan_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Aplikasi Pencatatan Perawatan Hewan")
    Label(text="Menu Utama", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Tambahkan Kegiatan", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Daftarkan Hewan", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()

