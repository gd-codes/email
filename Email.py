# _____________________________________________________________________________________________________________________________________________________________________________

#                                                                              Email
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Python 3
# Gautam D - 2018
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import smtplib
from time import sleep
import sys
import getpass as gp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


if __name__ == '__main__':

    print("Send a test email over gmail's server")
    print("  Loading...\n")    

    try :
        try :
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
        except Exception :
            print("Process failed - No internet connection")
            sleep(5)
            sys.exit()

        from_addr = input("Enter your complete gmail id to login with : ")
        pwd = gp.getpass("Enter Password for '{}' [No characters will be displayed on screen for security] : ".format(from_addr))
        # Note : This will raise a warning and display the password if run from IDLE - run this script from the Python terminal.
        
        try :
            print("  Signing in...")
            server.login(from_addr, pwd)
            del pwd 
        except smtplib.SMTPAuthenticationError :
            print("\nProcess failed due to either :\n1. Invalid email id or password; or\n2. Your Gmail account not being configured to allow 'less secure app access'")
            print("   [visit 'https://myaccount.google.com/lesssecureapps' and login to switch on/off app access]")
            server.quit()
            sleep(20)
            sys.exit()
    
        to_addr = input("\nEnter recipient(s)' full email address(es) below [Example : abc@def.com, recipient@domain.in, etc@addr.info] \nMail To : ")
        to_list = to_addr.split(',')
        subj = input("Enter Email Subject : ")

        print("\nEnter your message below line by line [Enter 2 consecutive blank lines to end the message] :")
        message_body = """"""
        consecutive_blanks = 0
        while True:
            msg = input("    ")
            if len(msg) != 0:
                msg += '\n'
                message_body += msg
                consecutive_blanks = 0
            elif len(msg) == 0 and consecutive_blanks == 0 :
                message_body += '\n'
                consecutive_blanks = 1
            elif len(msg) == 0 and consecutive_blanks == 1 :
                message_body += '\n'
                print("  Processing...")
                break

        message = MIMEMultipart()
        message['From'] = from_addr
        message['To'] = to_addr
        message['Subject'] = subj
        message.attach( MIMEText(message_body, 'plain') )
        

        try :
            server.sendmail( from_addr, to_list, message.as_string() )
        except smtplib.SMTPRecipientsRefused :
            print("Process failed - Invalid recipient's email address")
            server.quit()
            sleep(3)
            sys.exit()
            
        print("Successfully sent !")
        sleep(1)

    finally :
        print("  Signing out...")
        server.quit()
        sleep(1.5)
        
#______________________________________________________________________________________________________________________________________________________________________________  
    
