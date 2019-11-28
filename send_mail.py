    import smtplib
import ssl
from datetime import  date

gmail_user = 'missing.students.cv'
# problema de segurança, pass do mail do sender em plaintext
gmail_password = '52S[rheG'

sent_from = 'missing.students.cv@gmail.com'
# to = ['saraferreira.p3@gmail.com', 'pedrommunas@gmail.com']
to = ['missing.students.cv@gmail.com'] # Para testar
subject = 'Attendence for the class of ' + str(date.today().strftime("%d/%m/%Y"))
body = None

with open('./attendance.txt') as fp:
    body = fp.read()

message = """\
From: %s
To: %s
Subject: %s
\n%s
""" % (sent_from, ", ".join(to), subject, body)


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("missing.students.cv", "52S[rheG")
    server.sendmail(
        sent_from,
        sent_from,
        message)
    server.quit()
    print('Email sent!')

except:
    print('Something went wrong...')
