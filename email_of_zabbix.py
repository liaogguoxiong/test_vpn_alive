#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time             : 2019-10-17 14:26
# @Author           : lgx
# @project_name     : send_mail
# @File             : email_of_zabbix.py
# @Des: zabbix发送邮件的脚本

import smtplib,sys
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def send_email(receiver,subject,content):

    mail_server = 'smtp.qq.com'
    mail_user = '297979949@qq.com'
    mail_passwd = 'rhoexjltojtcbghc'
    sender = '297979949@qq.com'


    """
    构建发送人,接收人,主题
    """
    msg=MIMEMultipart("mix")
    msg['From']=Header(sender,'utf-8').encode()
    msg['To']=Header(receiver,'utf-8').encode()
    msg['Subject']=Header(subject,'utf-8').encode()


    """
    构建文本对象
    """

    email_content=MIMEText(content,'plain','utf-8')
    msg.attach(email_content)


    """
    发送邮件
    """
    smtp = smtplib.SMTP()
    smtp.connect(mail_server, 25)
    smtp.login(mail_user, mail_passwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    send_email()



