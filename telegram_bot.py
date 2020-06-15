import telegram
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

bot=telegram.Bot(token='')

#for i in bot.getUpdates():
    #print(i.message) #받은 메세지 확인

bot.sendMessage(chat_id=1298235907,text='테스트입니다')
