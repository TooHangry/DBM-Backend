import datetime
import smtplib
import ssl
import config as config

class Mail:
    def __init__(self):
        self.port = 587
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = config.EMAIL_ADDRESS
        self.password = config.EMAIL_PASSWORD

    def send(self, emails, subject, content):
        context = ssl.create_default_context()
        server = smtplib.SMTP(self.smtp_server_domain_name, self.port)

        try: 
            server.connect(self.smtp_server_domain_name, 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.sender_mail, self.password)
            for email in emails:
                server.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")
        except Exception as e:
            return e
        finally:
            server.quit()

def send_invites(recipients, home, admin):
    subject = str(admin['fname']) + " Wants You To Join Their Home!"
    body = f'''Dear User,\n\n{admin['fname']} wants you to collaborate with them in their home!\nClick the link below to create an account. You will see the new home ({home['nickname']}) listed once you sign in!\n\nClick or copy the link http://174.104.209.51:3000/login to get started.\n\nYour pals,\nRobert, Tyler, and Brendon\nHome Manager 2021'''

    try:
        client = Mail()
        client.send(recipients, subject, body)
    except:
        print('Something went wrong while sending invites')

    return


def send_collab_notice(user, home, admin):
    subject = str(admin['fname']) + " Wants You To Join Their Home!"
    body = f'''Dear {user['fname']},\n\n{admin['fname']} has added you to their new home!\nClick the link below to create a new account using this email. Once you finish, you will see the new home ("{home['nickname']}") listed in your "homes" tab!\n\nClick or copy the link http://174.104.209.51:3000/homes to continue.\n\nYour pals,\nRobert, Tyler, and Brendon\nHome Manager 2021'''

    try:
        client = Mail()
        client.send([user['email']], subject, body)
    except:
        print('Something went wrong while sending collab notice')
    return

def send_list_notice(user, home, title, end):
    subject = f"New Shopping List for {home['nickname']}!"
    body = f'''Dear {user['fname']},\n\nYou have been assigned to a new shopping list due by {datetime.date.strftime(end, "%m/%d/%Y")}.\nClick the link below to view your lists. You will see the new list ("{title}") listed in your "lists" tab!\n\nClick or copy the link http://174.104.209.51:3000/lists to continue.\n\nYour pals,\nRobert, Tyler, and Brendon\nHome Manager 2021'''

    try:
        client = Mail()
        client.send([user['email']], subject, body)
    except:
        print('Something went wrong while sending collab notice')
    return