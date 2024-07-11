import smtplib
from email.mime.text import MIMEText

# Gmail account credentials
username = 'muaztalib345@gmail.com'
password = 'qxst mvmt vuvh adoy'

# Email content
msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test Email'
msg['From'] = username
msg['To'] = username

# Sending email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, [username], msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
