import telegram
from models import Video


def post_video(video: Video):

    TOKEN = "5500578534:AAFyplzRMKZnasizeiouBHi8yOlnhsJnZQ4"
    bot = telegram.Bot(token=TOKEN)
    chat_id = "-1001568976119"
    text = f"{video.title}\n{video.youtube_link}"

    response = bot.send_message(chat_id=chat_id, text=text)
    return response
