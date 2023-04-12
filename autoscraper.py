from autoscraper import AutoScraper
import requests
import schedule
import time
import datetime


url = ''         #URL WEBSITE
bot_token =  ''  # YOUR_BOT_TOKEN
bot_chatID = ''  # TELEGRAM_USER_CHAT_ID
wanted_list = ['target','words']


def checktime():
    timecurrent = datetime.datetime.now()
    #displaytime = timecurrent.strftime("%H:%M")
    timecheck1 = "02:10"
    timecheck2 = "02:18"
    if display_time > timecheck1 and display_time < timecheck2:
        print ("time to sleep")
        time.sleep(20000)
    else:
        print("")
        report_url()


def use_scraper():
    scraper = AutoScraper()
    result = scraper.build(url, wanted_list, update=True)
    print("I got:")
    print(result)
    stringtext = str(result)
    return stringtext


def report_url():
    stringtext = use_scraper()    
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + stringtext
    response = requests.get(send_text)
    return response.json()
    print("")    
    

report_url()
#checktime()

schedule.every(160).seconds.do(report_url)
#schedule.every(160).seconds.do(checktime)
while True:
    schedule.run_pending()
    time.sleep(1)
    