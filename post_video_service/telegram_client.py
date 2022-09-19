import telegram
from config import TELEGRAM_BOT_TOKEN
from models import Video


def post_video(video: Video):

    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    chat_id = "-1001568976119"
    text = f"{video.title}\n{video.youtube_link}"

    response = bot.send_message(chat_id=chat_id, text=text)
    return response
