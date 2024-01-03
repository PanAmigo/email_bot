import smtplib

onet_user = 'u_c0ewfp@op.pl'
onet_password = 'l^VAb1#)nIx'

sent_from = onet_user
to = ['bartlomiej.filoda@edu.uni.lodz.pl']
subject = 'mail testowy'
body = 'tekst tekst tekst tekst'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.poczta.onet.pl', 465)
    smtp_server.ehlo()
    smtp_server.login(onet_user, onet_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Udało się!")
except Exception as ex:
    print("Coś psozło nie tak...",ex)