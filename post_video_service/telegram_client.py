import telegram

def send_video(video):
    pass

TOKEN = '5500578534:AAFyplzRMKZnasizeiouBHi8yOlnhsJnZQ4'

bot = telegram.Bot(token=TOKEN)

chat_id = '-1001568976119'

bot.send_message(chat_id=chat_id, text='Взлёт и падение - Эдди Мерфи \n https://www.youtube.com/watch?v=wFb6SlgBu-c')

