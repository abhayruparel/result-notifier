from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import smtplib
import mimetypes
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart


def sendMail():

    msg = MIMEMultipart()
    user = 'gdrivebot12@gmail.com' #Enter sender's email address
    passwd = 'qwerty@123'
    msg['Subject'] = "Sem-V Result is now live!"
    msg['From'] = f'Result notifier <{user}>'
    msg['To'] = "abhayruparel2000@gmail.com, rushil.rc@gmail.com" #Enter receiver's email address
    msgContent = "https://result.ganpatuniversity.ac.in/"
    Content = MIMEText(msgContent,'plain')
    msg.attach(Content)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(user,passwd)
        smtp.send_message(msg)
    print("E-Mail Sent!")


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
mainDriver = webdriver.Chrome(executable_path='chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
mainDriver.get('https://result.ganpatuniversity.ac.in/')
mainDriver.find_element_by_xpath("//select[@name='ddlInst']/option[text()='16 - ICT']").click()
mainDriver.find_element_by_xpath("//select[@name='ddlDegree']/option[text()='B.TECH-CSE(CS)']").click()
mainDriver.find_element_by_xpath("//select[@name='ddlSem']/option[text()='V']").click()
examsList = Select(mainDriver.find_element_by_xpath("//select[@name='ddlScheduleExam']")).options
for i in examsList:
    print(i.text)
mainDriver.close()
if len(examsList) > 3:
    print('Result for SEM V has been declared.')
    sendMail()
else:
    print('Result has not yet been declared.')
