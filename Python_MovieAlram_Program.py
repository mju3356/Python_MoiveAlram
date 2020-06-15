import requests
from bs4 import BeautifulSoup
import sys,io
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

bot=telegram.Bot(token='')
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200614&screencodes=&screenratingcode=&regioncode='

def job_function():
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'html.parser')
    movieList=soup.select_one('span.imax')
    if movieList:
        #imax=movieList.find_parent('div',class_='col-times')
        #MTitle=(imax.select_one('a > strong').text.strip())
        MTitle=movieList.find_parent('div',class_='col-times').select_one('a > strong').text.strip()
        bot.sendMessage(chat_id=,text=MTitle+' IMAX 예매가 열렸습니다.')
        #print(MTitle+' IMAX 오픈')
        sched.pause()

sched=BlockingScheduler()
sched.add_job(job_function,'interval',seconds=30)
sched.start()
