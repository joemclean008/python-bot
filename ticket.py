import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time

def ticket():
    url = 'https://iticket.az/events/teknofest/teknofest'
    session = HTMLSession()
    resp = session.get(url)

    resp.html.render()

    soup = BeautifulSoup(resp.html.html , "lxml")
    result = soup.find("div", {"id":"icalendar"})
    string = str(result)
    date="29.05.2022"
    if(date in string):
        TOKEN = "5447684727:AAGVyYPtp9uASSc6eyoBGDoHvicNbAv3_kU"
        chat_id = "-1001755062989"
        text = f"{date} shows on https://iticket.az/events/teknofest/teknofest"
        bot_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
        requests.get(bot_url)

while True:
    ticket()
    time.sleep(600)
