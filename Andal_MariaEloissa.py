#Andal, Maria Eloissa
#BSIS-2AB

from tkinter import *
from tkinter import messagebox

master = Tk()
master.geometry('300x400')
master.config(bg="#231F20")

class CRYPTOGRAPHY(Frame):

    def __init__(master):
        
        Frame.__init__(master)
        master.master.title("The Encryptor-Decryptor")
        master.config(bg="#231F20")
        master.pack()

        master.LblCrypt = Label(master, text = "CRYPTOGRAPHY", bg ="#231F20", fg ="#F4EAD1", font = ("Verdana", 18, "bold")) 
        master.LblCrypt.pack(pady = 20)

        master.iMessageEntry = Entry(master, font = ("Courier", 12), width=15) 
        master.iMessageEntry.pack(pady = 20)

        master.keyVar1 = IntVar() 
        master.iMessageEntry1 = Entry(master, font = ("Courier", 12), width=15, textvariable = master.keyVar1) 
        master.iMessageEntry1.pack(pady = 20)
        
        master.bN1 = Button(master, text = "ENCRYPT", bg ="#F0A5BB", fg ="black", font = ("Fixedsys", 15), width=11, command = master.encryption) 
        master.bN1.pack(pady = 20)

        master.bN2 = Button(master, text = "DECRYPT", bg ="#EAA0A0", fg ="black", font = ("Fixedsys", 15), width=11, command = master.decryption) 
        master.bN2.pack(pady = 20)


    def encryption(master):
        try:
            text = master.iMessageEntry.get()
            encryptionKey  = int(master.keyVar1.get())
            asciiValue = []
            for eachCharacter in text:
                ordinalValue = ord(eachCharacter)
                encryptedText = ordinalValue + encryptionKey
                asciiValue.append(encryptedText)
            for ch in asciiValue:
                print(ch, end = ", ")

            messagebox.showinfo("The value of your encrypted message", f"The Values are: {asciiValue}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a message or a word!")

    def decryption(master):   
        try:
            code = master.iMessageEntry.get()
            num = int(master.keyVar1.get())
            text = ""
            for ch in code:
                ordinalValue = ord(ch)
                cipherVal = ordinalValue - num
                if cipherVal < ord('0'):
                    cipherVal = ord('Z') + num + \
                        (ord('a') - ordinalValue + 1 )
                text += chr(cipherVal)
                print(text)

            messagebox.showinfo("Your decrypted message is", f"The Character Equivalents: {text}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a message or a word!")

def main():

    CRYPTOGRAPHY().mainloop()
main()

