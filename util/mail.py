import smtplib
from util import logger
from email.header import Header
from email.utils import formataddr
from email.mime.text import MIMEText
from common import email_config as config


class Email:
    def __init__(self):
        self.__sender = config['sender']  # 发件人邮箱账号
        self.__password = config['secure']  # 发件人邮箱密码
        self.__receivers = config['receivers']  # 收件人邮箱账号，我这边发送给自己
        self.__charset = config['charset']

    def send_emil(self, title, text, sub_type='plain', receivers=None):
        server = smtplib.SMTP_SSL(config['host'], config['ssl_port'] if config['user_ssl'] else config['port'])
        server.login(self.__sender[0], self.__password)
        msg = MIMEText(text, sub_type, self.__charset)
        msg['From'] = formataddr(self.__sender)
        msg['Subject'] = Header(title, self.__charset)
        if not receivers:
            receivers = self.__receivers
        assert len(receivers), '参数 receivers 不能为空'
        for receiver in receivers:
            msg['To'] = formataddr(receiver)
            self.__send_email(self.__sender[0], receiver[0], msg.as_string(), title, server)
        server.quit()  # 关闭连接

    @staticmethod
    def __send_email(sender, receiver, msg, title, server):
        try:
            server.sendmail(sender, receiver, msg)
            logger.info('发送邮件 - {} 给 {} 成功'.format(title, receiver))
        except smtplib.SMTPException:
            logger.error('发送邮件 - {} 给 {} 失败'.format(title, receiver))


email = Email()
