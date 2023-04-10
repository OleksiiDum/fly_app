import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from fly_app.helpers import html_template
from email import encoders


class Mailer:

    SERVER = 'smtp.gmail.com'
    PORT = 465
    PASSWORD = '***'
    LOGIN = '***'

    connection = smtplib.SMTP_SSL(SERVER, PORT)
    connection.login(LOGIN, PASSWORD)

    def __init__(self, user, text, subject, file=None, image=None):
        self.user = user #???
        self.text = text
        self.subject = subject
        self.file = file
        self.image = image
    
    def send_text_mail(self):
        message = MIMEText(self.text)
        message['Subject'] = self.subject
        message['From'] = self.LOGIN
        message['To'] = self.user

        self.connection.sendmail(self.LOGIN, self.user, message.as_string())
        # self.connection.quit()
    
    def send_html(self):
        message = MIMEMultipart()
        message['Subject'] = self.subject
        message['From'] = self.LOGIN
        message['To'] = self.user
        html_message = MIMEText(html_template(self.text), 'html')
        message.attach(html_message)

        self.connection.sendmail(self.LOGIN, self.PASSWORD, message.as_string())
        # self.connection.quit()
    
    def send_file(self):
        message = MIMEMultipart()
        message['Subject'] = self.subject
        message['From'] = self.LOGIN
        message['To'] = self.user

        for_sending_file = open(self.file, 'rb')
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((for_sending_file).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=self.file)
        message.attach(payload)
        for_sending_file.close()

        self.connection.sendmail(self.LOGIN, self.PASSWORD, message.as_string())
        # self.connection.quit()
    
    def send_image(self):
        message = MIMEMultipart()
        message['Subject'] = self.subject
        message['From'] = self.LOGIN
        message['To'] = self.user

        file = open(self.image, 'rb')
        data = file.read()
        file.close()

        image = MIMEImage(data)
        message.attach(image)

        self.connection.sendmail(self.LOGIN, self.PASSWORD, message.as_string())
        # self.connection.quit()
