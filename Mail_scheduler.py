import datetime
import time
import schedule
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *

def gmail_sch():
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	ExpectedTime = time1.get()
	while current_time != ExpectedTime:
	    print("sleeping")
	    time.sleep(1)
	    t = time.localtime()
	    current_time = time.strftime("%H:%M:%S", t)
	    print(current_time)
	if current_time == ExpectedTime:
		"""Take input from files for login"""
		with open("id.txt","r") as log:
        		loginid = log.read()
		with open("pass.txt","r") as pas:
			loginpass = pas.read()

		"""Collect all Information required for sending mail"""
		sender_address = loginid
		sender_pass = loginpass
		receiver_address = to_id.get()
		mailsub = sub.get()
		mail_content = body.get()
    
		"""Setup MINE"""
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = mailsub

		"""Send Mail"""
		message.attach(MIMEText(mail_content, 'plain'))
		session = smtplib.SMTP('smtp.gmail.com', 587) 
		session.starttls()
		session.login(sender_address, sender_pass)
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print('Mail Sent Successfully')

r = Tk()
r.geometry("1000x600")
r.title('Gmail Scheduler') 
Label(r, text='To:').grid(row=1,pady=20)
Label(r, text='Subject:').grid(row=2,pady=20)
Label(r, text='Body:').grid(row=3,pady=20)
Label(r, text='Time:').grid(row=4,column=0,pady=20)
from_id = Entry(r)
to_id = Entry(r)
sub = Entry(r)
body = Entry(r)
time1 = Entry(r) 
to_id.grid(row=1, column=1,ipadx=150,ipady=5)
sub.grid(row=2, column=1,ipadx=150,ipady=5)
body.grid(row=3, column=1,ipadx=150, ipady=80)
time1.grid(row=4, column=1,ipadx=50,ipady=5) 
v = IntVar()
v.set(1)
buttonP = Button(r, text='Schedule', width=25, command=gmail_sch) 
buttonP.grid(row=8,padx=120,ipadx=80,ipady=20)
buttonS = Button(r, text='Exit', width=25, command=r.destroy) 
buttonS.grid(row=8,column=1,ipadx=80,ipady=20)
r.mainloop()


    