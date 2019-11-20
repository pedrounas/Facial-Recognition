import smtplib


gmail_user = 'mail@gmail.com'
#problema de segurança, pass do mail do sender em plaintext
gmail_password = 'passowrd'

sent_from = 'saraferreira.p3@gmail.com'
to = ['saraferreira.p3@gmail.com']
subject = 'Subject test'
body = "Body test"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    #Secure connection
    server.starttls()
    #Para isto dar é preciso Allowing less secure apps to access your account
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print('Something went wrong...')

