from models import Video
from config import YOUTUBE_API_ENDPOINT
import requests
from datetime import datetime


def get_youtube_videos(channel_id: str, api_key: str) -> dict:
    params = dict(
        key=api_key,
        channelId=channel_id,
        part='snippet',
        order='date',
        maxResults='100',
        type='video',
        # publishedAfter='2019-06-04T20:14:10Z',
    )
    videos_response = requests.get(YOUTUBE_API_ENDPOINT, params=params).json()

    return videos_response


def parse_videos(videos_dict: dict, existing_videos: list, channel_id: str) -> list[Video]:

    youtube_videos: list = []

    youtube_link_prefix = 'https://www.youtube.com/watch?v='
    for item in videos_dict['items']:
        if item['id']['videoId'] not in existing_videos:
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_published_at = datetime.strptime(item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%Sz')

            video = Video(
                id=video_id,
                youtube_link=youtube_link_prefix+video_id,
                title=video_title,
                youtube_publish_date=video_published_at,
                is_published_in_tg=False,
                channel_id=channel_id,
            )

            youtube_videos.append(video)

    return youtube_videos
