import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

from common import email_config as email
from util import logger


class Email:
    def __init__(self):
        self.__sender = email['sender']  # 发件人邮箱账号
        self.__password = email['secure']  # 发件人邮箱密码
        self.__receivers = email['receivers']  # 收件人邮箱账号，我这边发送给自己
        self.__charset = email['charset']

    def send_emil(self, title, text, sub_type='plain', receivers=None):
        server = smtplib.SMTP_SSL(email['host'], email['ssl_port'] if email['user_ssl'] else email['port'])
        server.login(self.__sender[0], self.__password)
        msg = MIMEText(text, sub_type, self.__charset)
        msg['From'] = formataddr(self.__sender)
        msg['Subject'] = Header(title, 'utf-8')
        if not receivers:
            receivers = self.__receivers
        assert len(receivers), 'parameter `receivers` is empty'
        for receiver in receivers:
            msg['To'] = formataddr(receiver)
            self.__send_email(self.__sender[0], receiver[0], msg.as_string(), title, server)
        server.quit()  # 关闭连接

    @staticmethod
    def __send_email(sender, receiver, msg, title, server):
        try:
            server.sendmail(sender, receiver, msg)
            logger.info('发送邮件 - {} 给 {} 成功'.format(receiver, title))
        except smtplib.SMTPException:
            logger.error('发送邮件 - {} 给 {} 失败'.format(receiver, title))
