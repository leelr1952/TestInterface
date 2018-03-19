import smtplib
from email.mime.text import MIMEText


class SendMail(object):
    def __init__(self):
        self.send_user = 'mushishi_xu@163.com'
        self.password = 'xu221168'
        self.host = 'smtp.163.com'

    def sendmail(self, user_list, sub, content):
        user = "Mushishi" + "<" + self.send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ';'.join(user_list)
        server = smtplib.SMTP()
        server.connect(self.host)
        server.login(self.send_user, self.password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def sendmain(self, pass_list, fail_list):
        receive_user = ['22436411@qq.com']
        sub = "这是自动化测试报告"
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        total_num = pass_num + fail_num

        pass_result = "%.2f%%" % (pass_num / total_num * 100)
        fail_result = "%.2f%%" % (fail_num / total_num * 100)

        content = "这次一共测试了%s个接口，通过了%s个，失败了%s个，通过率为%s" % (total_num, pass_num, fail_num, pass_result)

        self.sendmail(receive_user, sub, content)


if __name__ == '__main__':
    sen = SendMail()
    sen.sendmail(['22436411@qq.com'], "Test测试邮件", "这是第一封测试哟见，请不要554")