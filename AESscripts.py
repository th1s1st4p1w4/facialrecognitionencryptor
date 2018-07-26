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

    def load_file(self):
        global direname
        direname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

    def getAllFiles(self):
        try:
            dir_path = direname
            dirs = []
            for dirName, subdirList, fileList in os.walk(dir_path):
                for fname in fileList:
                    dirs.append(dirName + "\\" + fname)
        except NameError:
            messagebox.showerror("Error","Please select a directory")
        else:
            return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        if dirs is not None:
            for file_name in dirs:
                self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        if dirs is not None:
            for file_name in dirs:
                self.decrypt_file(file_name)
                
    def checkPW(self):
        if os.path.isfile('data.txt.enc'):
            while True:
                pk = K.get()
                password = pk
                enc.decrypt_file("data.txt.enc")
                p = ''
                print (p)
                with open("data.txt", "r") as f:
                    p = f.readlines()
                if p[0] == password:
                    enc.encrypt_file("data.txt")
                    enc.encrypt_all_files()
                    break

    def recog(self):
        import face_recognition_Decrypt

    def close(self):
        root.destroy()


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')

root = Tk()
root.title("Cryptofile")
root.minsize(width=250, height=100)
root.maxsize(width=250, height=100)

loadButton = Button(root, text="Load File(s)", command=enc.load_file)
encryptButton = Button(root, text="Encrypt File", command=lambda: [f() for f in [enc.checkPW]])
decryptButton = Button(root, text="Decrypt File", command=lambda: [f() for f in [enc.recog, enc.close]])

loadButton.pack()
encryptButton.pack()
decryptButton.pack()

Label(root, text="Key:").pack(side='left')
K = Entry(root, show="*")
K.pack(side='left')










