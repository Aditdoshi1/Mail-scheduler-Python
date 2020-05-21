# Mail-scheduler-Python
A Gmail Scheduler that can send mails at the users specified time. Multiple Instances can be made to send multiple mails to a particular user at the same time.

All the input of a Compose Mail Fields are included ie. To, Subject, Body.(Can be further improved to include attachments).
To Run, there are some limitations:- You have to sign in your Gmail Account and allow less secure 3rd party application to login to mail.(This is necessary because Gmail blocks Sign-in through 3rd party program unless the program is verified)
To turn on less Secure access, goto - https://myaccount.google.com/lesssecureapps and sign-in to your google account and turn on less secure access.

I would suggest you to include 2-step-authentication and then allow less secure application access, to allow 3rd party applications to access gmail without downgrading your security.

Once everything is done, You have to run setup.py, this file will ask you to enter Email-id & password of your gmail account and will save the credentials on your pc in id.txt & pass.txt file.(You can even create 2 files named - id.txt & pass.txt and store your credentials manually)
This has to be done only once

Once Credentials are stored, Run the main file - Mail_scheduler.py.
