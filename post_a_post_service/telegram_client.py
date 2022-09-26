import telegram
from config import TELEGRAM_BOT_TOKEN
from models import Post


def post_video(post: Post):

    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    # chat_id = "-1001568976119"
    chat_id = "183175828"
    text = f"{post.title}\n\n{post.link}"

    response = bot.send_message(chat_id=chat_id, text=text)
    return response
