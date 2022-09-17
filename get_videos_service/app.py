from youtube_client import get_youtube_videos, parse_videos
from db_client import get_channels, get_videos, save_new_videos
from config import YOUTUBE_API_KEY

channels = get_channels()


videos_in_bd = get_videos()
ids_of_videos_in_bd = [video.id for video in videos_in_bd]

new_videos: list = []
for channel in channels:
    youtube_response = get_youtube_videos(channel, YOUTUBE_API_KEY)
    channel_videos = parse_videos(youtube_response, ids_of_videos_in_bd, channel)
    new_videos.append(channel_videos)

save_new_videos(new_videos)
