######## This is a mail application ######################################
import tkinter as tk
from tkinter import scrolledtext 
from tkinter import messagebox
#for sending mail#####################
#import getpass-----uncomment it when you are using getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
#############################################################################
###########GUI MAIL###########################################################
window = tk.Tk()
window.title("SEND MAIL")
window.geometry('550x550')
sendto_label = tk.Label(window, text = "Send To: ").grid(row = 1, column = 0)
sendfr_label = tk.Label(window, text = "Sent From: ").grid(row = 2, column = 0)
subj_label = tk.Label(window, text = "Subject: ").grid(row = 3, column = 0)
msg_label = tk.Label(window, text = "message: ").grid(row = 4, column = 0)
passw_label = tk.Label(window, text = "password: ").grid(row = 5, column = 0)
txt = scrolledtext.ScrolledText( window, width = 50, height = 30)
sendto_entry = tk.Entry(window, width = 50, bd = 5)
sendfr_entry = tk.Entry(window, width = 50, bd = 5)
passw_entry = tk.Entry(window, width = 50, bd = 5)
subj_entry = tk.Entry(window, width = 50, bd = 5)
sendto_entry.grid(row = 1, column = 1)
sendfr_entry.grid(row = 2, column = 1)
subj_entry.grid(row = 3, column = 1)
txt.grid(row = 4, column = 1)
passw_entry.grid(row = 5, column = 1)
################SMTP SEND#######################################################
def clicked():
    sender = sendto_entry.get()
    receiver = sendfr_entry.get()
    password = passw_entry.get()
    subject = subj_entry.get()
    message = txt.get('1.0',tk.END)
    def mail_sending(sender,receiver,password,subject,message):
        ### MAKING A E-MAIL PACKET
        msg = MIMEMultipart()
        msg['To'] = receiver
        msg['From'] = sender
        msg['Subject'] = subject
        part = MIMEText('text','plain')
        part.set_payload(message)
        msg.attach(part)
        ### CREATING SESSION WITH USING SMTP 
        session = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        session.ehlo()
        session.starttls()
        #password = getpass.getpass(password)
        session.login(sender,password)
        session.set_debuglevel(1)
        session.sendmail(sender,receiver, msg.as_string())
        session.quit()
    
    def delete_entry():
        sendto_entry.delete(0,'end')
        sendfr_entry.delete(0,'end')
        subj_entry.delete(0,'end')
        passw_entry.delete(0,'end')
        txt.delete('1.0',tk.END )
        
    mail_sending(sender,receiver,password,subject,message)
    messagebox.showinfo("Success","mail sent")
    delete_entry()
send_butn = tk.Button( window, text = "SEND", command = clicked ).grid(row = 6, column = 1)    

    
window.mainloop()


################################### NOTE #####################################
### This app will only work when you change your gmail settings to receive ###
### mail from less secure applications.                                    ###
###                                                                        ###
### Sorry for the inconvenience working on it.                             ###
##############################################################################
