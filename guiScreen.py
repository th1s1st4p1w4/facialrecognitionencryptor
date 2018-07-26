from Crypto import Random
from Crypto.Cipher import AES
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os, random
import os.path
from os import listdir
from os.path import isfile, join
import time
import sys
sys.path.append('C:/Users/Tapiwanashe Muza/Desktop/HIT200/Face-Recognition')
sys.path.append('C:/Users/Tapiwanashe Muza/Desktop/HIT200')

root = Tk()
#root.geometry("500x300")
v = StringVar()

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def  init_window(self):
        global T, P
        self.master.title("Encrypt/Decrypt File(s)")
        self.pack(fill=BOTH, expand=1)

        '''T = Text(root, height=1, width=30)
        T.pack(side='top')
        load_file_button = Button(self, text="Name of User", command=self.load_file_path)
        load_file_button.pack(side='top')'''

        setup_button = Button(self, text="Setup", command=self.fr_setup_window)
        setup_button.pack(side='top')

        
        '''clear_button = Button(self, text="Clear", command=self.delete_text_field)
        clear_button.pack(side='top')'''

        start_button = Button(self, text = "Start", command=lambda: [f() for f in [self.create_fr_window]])
        start_button.pack(side='top')

        '''Label(root, text="Choose operation:", justify = LEFT, padx = 20).pack()

        Radiobutton(root, text="Encrypt", variable=v, value=1).pack(anchor=W)
        Radiobutton(root, text="Decrypt", variable=v, value=2).pack(anchor=W)'''
        
        '''Label(root, text="Name of user ").pack(side='left')
        P = Entry(root)
        P.pack(side='left')'''

    def create_fr_window(self):
        newindow = Toplevel(root)
        newindow.title("Facial Recognition")
        newindow.geometry("400x400")
        newindow.grab_set()
        msg = Message(newindow, text="This is the page for facial recognition")
        msg.pack()
        b1 = Button(newindow, text="Recognize", command=self.recog)
        b1.pack()
        

    def fr_setup_window(self):
        global P, CP, gP, gCP
        newindow2 = Toplevel(root)
        newindow2.title("Setup Facial Recognition")
        newindow2.geometry("500x200")
        newindow2.grab_set()
        msg = Message(newindow2, text="Press the  'Enter Dataset' button to create the facial recognition dataset")
        msg.pack()
        b2 = Button(newindow2, text="Enter Dataset", command=lambda: [f() for f in [self.dataset]])
        b2.pack()
        b3 = Button(newindow2, text="Training", command=lambda: [f() for f in [self.train]])
        b3.pack()
        Label(newindow2, text="Enter password: ").pack(side='left')
        P = Entry(newindow2, show='*')
        P.pack(side='left')
        Label(newindow2, text="Confirm password: ").pack(side='left')
        CP = Entry(newindow2, show='*')
        CP.pack(side='left')
        b4 = Button(newindow2, text="Enter", command=lambda: [f() for f in [self.checkNULL]])
        b4.pack()

    def delete_text_field(self):
        T.delete(1.0, END)

    def load_file_path(self):
        global direname
        direname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
        if len(direname ) > 0:
            T.insert(END, direname)

    def checkNULL(self):
        global gP, gCP
        gP = P.get()
        gCP = CP.get()
        if gP == "" or gCP == "":
            messagebox.showerror("Error","Please enter something")
        else:
            Window.pwCompare(self)

    def pwCompare(self):
        if gP == gCP:
            f = open("data.txt", "w+")
            f.write(gP)
            f.close()
            messagebox.showinfo("Error","Password been saved")
            enc.encrypt_file("data.txt")
        else:
            messagebox.showwarning("Error","Passwords Mismatched!")

    def sel(self):
        global username
        username = P.get()
        print (username)

    def sel2(self):
        global x
        x = v.get()
        print (x)

    def sel3(self):
        print (direname)

    def hide(self):
        self.withdraw()

    def recog(self):
        import face_recognition_Copy

    def dataset(self):
        import face_datasets

    def train (self):
        import training

    def close (self):
        self.destroy()

enc = Encryptor(key)

label = Label(root)
label.pack()
app = Window(root)
root.mainloop()
