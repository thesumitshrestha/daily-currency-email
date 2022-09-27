from email import header
from email.mime.text import MIMEText
from math import prod
from re import T
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import datetime as dt
import smtplib
from email.mime.multipart import MIMEMultipart
import time

content = ''


def review_count_scrape():
    # url = "https://www.amazon.com/Best-Sellers/zgbs"
    url = "https://www.laxmibank.com/rates/forex/"
    headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, features='lxml')
    print(r.status_code)

    gdp_table = soup.find("table", attrs={
                          "id": "lb-forex-table-0"})
    gdp_table_td = gdp_table.find_all('td')
    currency_list = []
    for i in gdp_table_td:
        currency_list.append(i.text)

    return currency_list


currency_data = review_count_scrape()
currency_list = []
dollar = currency_data[0:5]
euro = currency_data[5:10]
today = date.today()

for i in currency_data:
    currency_list.append(dollar)
    currency_list.append(euro)

df = pd.DataFrame(currency_list, columns=["Currency", "Unit",
                                          "Buy Below 50", "By Above 50", "Selling"])

currency_content = """\
<html>
  <head></head>
  <body>
    <p> Hi Sumit, </p>
    
    <p> Here is the dollar rate table. </p>
    {0}

    <p> Thank You, <br> Python Script </p>
  </body>
</html>
""".format(df.head(2).to_html())


def send_email():
    # Sending email
    print("Composing Email...")

    SERVER = "smtp.gmail.com"
    PORT = 587
    FROM = 'devsumitest@gmail.com'
    TO = 'summitshrestha8@gmail.com'
    PASS = 'tmuonaezprppfbss'
    SUBJECT = "Dollar Rate of " + str(date.today().strftime("%B %d, %Y"))

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO

    msg.attach(MIMEText(currency_content, 'html'))

    print("Initializing Server")

    server = smtplib.SMTP(SERVER, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()

    server.login(FROM, PASS)
    server.sendmail(FROM, TO, msg.as_string())

    print('Email Sent...')

    server.quit()


send_email()


def send_email_at(send_time):
    print("Timestamp is", send_time.timestamp())
    print("Time is", time.time())
    print("Difference is", send_time.timestamp() - time.time())
    time.sleep(send_time.timestamp() - time.time())
    send_email()


# first_email_time = dt.datetime(2022, 9, 26, 20, 25, 0)
# interval = dt.timedelta(minutes=2*60)

# send_time = first_email_time

# while True:
#     send_email_at(send_time)
#     send_time = send_time + interval
