# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: sendemail
@time: 2020/2/18 15:59
"""


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr


def automail(title, msg, receivers, file):
    # 第三方 SMTP 服务
    mail_host="smtp.163.com"  #设置服务器
    mail_user="luojiarui2@163.com"    #用户名
    mail_pass="*****"   #口令


    print("daozheli")

    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = formataddr(["Jarrett", mail_user]) #括号里对应收件人邮箱昵称发件人邮箱账号
    message['To'] = formataddr([receivers,receivers])
    subject = title #邮件主题，也就是说是标题
    message['Subject'] = Header(subject, 'utf-8')

    #邮件正文内容
    message.attach(MIMEText(msg, 'plain', 'utf-8'))

    print(file)

    #构造附件1，传送当前目录下的文件
    att2 = MIMEText(open('微信图片_20200221221814.jpg', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="微信图片_20200221221814.jpg"'
    message.attach(att2)
    print(att2)

    try:
        sever = smtplib.SMTP(mail_host,25) #发件人邮箱中的SMTP服务器
        sever.login(mail_user,mail_pass)
        sever.sendmail(mail_user, [receivers], message.as_string()) #sendmail的第二个参数必须是list，可以发送多个用户
        print("邮件发送成功")
        sever.quit() #关闭连接
        #return 101
    except smtplib.SMTPException:
        print("Error: 无法发送邮件至"+receivers)
        #return 102


CNKI_file_name = "微信图片_20200221221814.jpg"

title = "dierci"
msg = "测-试-测-试"
receivers = "jiarui.luo@hirain.com"
file = CNKI_file_name

automail(title, msg, receivers, file)



