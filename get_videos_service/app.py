from youtube_client import get_youtube_videos
from db_client import get_channels, get_videos, save_new_videos
from config import YOUTUBE_API_KEY

channels_ids = get_channels()


videos_in_bd = get_videos()
ids_of_videos_in_bd = [video.id for video in videos_in_bd]

new_videos: list = []
for id in channels_ids:
    videos = get_youtube_videos(id, ids_of_videos_in_bd, YOUTUBE_API_KEY)
    new_videos.append(videos)

save_new_videos(new_videos)
