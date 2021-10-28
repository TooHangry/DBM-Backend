import smtplib
import ssl
import config as config


class Mail:
    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = config.EMAIL_ADDRESS
        self.password = config.EMAIL_PASSWORD

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(
            self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            result = service.sendmail(
                self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()


def send_invites(recipients, home, admin):
    subject = str(admin['fname']) + " Wants You To Join Their Home!"
    body = f'''Dear User,\n\n{admin['fname']} wants you to collaborate with them in their home!\nClick the link below to create an account. You will see the new home ({home['nickname']}) listed once you sign in!\n\nClick or copy the link http://localhost:4200/login to get started.\n\nYour pals,\nRobert, Tyler, and Brendon\nHome Manager 2021'''

    try:
        client = Mail()
        client.send(recipients, subject, body)
    except:
        print('Something went wrong while sending invites')

    return


def send_collab_notice(user, home, admin):
    subject = str(admin['fname']) + " Wants You To Join Their Home!"
    body = f'''Dear {user['fname']},\n\n{admin['fname']} has added you to their new home!\nClick the link below to sign in to your account. You will see the new home ({home['nickname']}) listed in your 'homes' tab!\n\nClick or copy the link http://localhost:4200/homes to continue.\n\nYour pals,\nRobert, Tyler, and Brendon\nHome Manager 2021'''

    try:
        client = Mail()
        client.send([user['email']], subject, body)
    except:
        print('Something went wrong while sending collab notice')

    return
