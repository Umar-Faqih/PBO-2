import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("700x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE PINJAM:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL PINJAM:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL KEMBALI:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE BUKU:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE ANGGOTA:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE PETUGAS:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_pinjam = Entry(mainFrame, width=50) 
        self.txtKode_pinjam.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_pinjam.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtTgl_pinjam = Entry(mainFrame, width=50) 
        self.txtTgl_pinjam.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtTgl_kembali = Entry(mainFrame, width=50) 
        self.txtTgl_kembali.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_buku = Entry(mainFrame, width=50) 
        self.txtKode_buku.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_anggota = Entry(mainFrame, width=50) 
        self.txtKode_anggota.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_petugas = Entry(mainFrame, width=50) 
        self.txtKode_petugas.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_peminjaman','kode_pinjam','tgl_pinjam','tgl_kembali','kode_buku','kode_anggota','kode_petugas')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_peminjaman', text='ID')
        self.tree.column('id_peminjaman', width="30")
        self.tree.heading('kode_pinjam', text='KODE')
        self.tree.column('kode_pinjam', width="80")
        self.tree.heading('tgl_pinjam', text='TGL PINJAM')
        self.tree.column('tgl_pinjam', width="100")
        self.tree.heading('tgl_kembali', text='TGL KEMBALI')
        self.tree.column('tgl_kembali', width="100")
        self.tree.heading('kode_buku', text='K BUKU')
        self.tree.column('kode_buku', width="80")
        self.tree.heading('kode_anggota', text='K ANGGOTA')
        self.tree.column('kode_anggota', width="80")
        self.tree.heading('kode_petugas', text='K PETUGAS')
        self.tree.column('kode_petugas', width="80")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_pinjam.delete(0,END)
        self.txtKode_pinjam.insert(END,"")
        self.txtTgl_pinjam.delete(0,END)
        self.txtTgl_pinjam.insert(END,"")
        self.txtTgl_kembali.delete(0,END)
        self.txtTgl_kembali.insert(END,"")
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,"")
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.txtKode_petugas.delete(0,END)
        self.txtKode_petugas.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_peminjaman"],d["kode_pinjam"],d["tgl_pinjam"],d["tgl_kembali"],d["kode_buku"],d["kode_anggota"],d["kode_petugas"]))
    def onCari(self, event=None):
        kode_pinjam = self.txtKode_pinjam.get()
        obj = Peminjaman()
        a = obj.get_by_kode_pinjam(kode_pinjam)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_pinjam = self.txtKode_pinjam.get()
        obj = Peminjaman()
        res = obj.get_by_kode_pinjam(kode_pinjam)
        self.txtKode_pinjam.delete(0,END)
        self.txtKode_pinjam.insert(END,obj.kode_pinjam)
        self.txtTgl_pinjam.delete(0,END)
        self.txtTgl_pinjam.insert(END,obj.tgl_pinjam)
        self.txtTgl_kembali.delete(0,END)
        self.txtTgl_kembali.insert(END,obj.tgl_kembali)
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,obj.kode_buku)
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,obj.kode_anggota)
        self.txtKode_petugas.delete(0,END)
        self.txtKode_petugas.insert(END,obj.kode_petugas)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_pinjam = self.txtKode_pinjam.get()
        tgl_pinjam = self.txtTgl_pinjam.get()
        tgl_kembali = self.txtTgl_kembali.get()
        kode_buku = self.txtKode_buku.get()
        kode_anggota = self.txtKode_anggota.get()
        kode_petugas = self.txtKode_petugas.get()
        # create new Object
        obj = Peminjaman()
        obj.kode_pinjam = kode_pinjam
        obj.tgl_pinjam = tgl_pinjam
        obj.tgl_kembali = tgl_kembali
        obj.kode_buku = kode_buku
        obj.kode_anggota = kode_anggota
        obj.kode_petugas = kode_petugas
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_pinjam(kode_pinjam)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_pinjam = self.txtKode_pinjam.get()
        obj = Peminjaman()
        obj.kode_pinjam = kode_pinjam
        if(self.ditemukan==True):
            res = obj.delete_by_kode_pinjam(kode_pinjam)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()