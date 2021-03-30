import requests
import json
import csv
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '326316877@qq.com'  # 发件人邮箱账号
my_password = 'furqatqxrftvbibc'  # 发件人邮箱密码
my_receiver = '326316877@qq.com'

novel_id_arr = {
    5108775,
    2132290,
    5175139,
    5259254,
    5325880,
    4470783,
    4424175,
    4219748,
    5372414,
    5309708,
    5038293,
    4862822}


def save_result(timestamp):
    result = []
    with open(timestamp + '_result.csv', 'w', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for id in novel_id_arr:
            # url = "https://android.jjwxc.net/androidapi/getnovelOtherInfo?novelId=" + str(id)
            url = "https://android.jjwxc.net/androidapi/novelbasicinfo?novelId=" + str(id)
            response = requests.get(url, verify=False)
            info = json.loads(response.content)
            csv_writer.writerow([info.get("novelName"), info.get("novelbefavoritedcount")])
            result.append([info.get("novelName"), info.get("novelbefavoritedcount")])
    return result


def send_email(subject, content):
    ret = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["聪聪", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["笨笨", my_receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = subject  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret = False
    return ret


def job():
    current_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    content = save_result(current_time)
    send_email(current_time + "记录", str(content))


job()
# print(send_email("ffff", "ceshisssfsdsfd"))
schedule.every(1).hours.do(job)
    # while True:
    #     schedule.run_pending()
