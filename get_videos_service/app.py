from config import YOUTUBE_API_KEY
from db_client import get_channels, get_videos, save_new_videos
from youtube_client import get_youtube_videos, parse_videos

channels = get_channels()


videos_in_bd = get_videos()
youtube_links_of_videos = [video.youtube_link for video in videos_in_bd]
youtube_videos_ids = [video_link.split('=')[1] for video_link in youtube_links_of_videos]

new_videos: list = []
for channel in channels:
    youtube_response = get_youtube_videos(channel, YOUTUBE_API_KEY)
    channel_videos = parse_videos(youtube_response, youtube_videos_ids, channel)
    new_videos.append(channel_videos)

save_new_videos(new_videos)
