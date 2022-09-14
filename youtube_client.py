from models import Video
from config import YOUTUBE_API_ENDPOINT
import requests
import datetime


def get_youtube_videos(channel_id: str, existing_videos: list, api_key: str) -> list[Video]:
    params = dict(
        key=api_key,
        channelId=channel_id,
        part='snippet',
        order='date',
        maxResults='10',
        type='video',
        # publishedAfter='2020-06-04T20:14:10Z'
    )
    videos_response = requests.get(YOUTUBE_API_ENDPOINT, params=params).json()

    youtube_videos: list = []

    for item in videos_response['items']:
        if item['id']['videoId'] not in existing_videos:
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_published_at = item['snippet']['publishedAt']
            # video = (video_id, video_title, video_published_at)

            video = Video(
                id=video_id,
                title=video_title,
                youtube_publish_date=datetime.datetime.utcnow(),
                # youtube_publish_date=video_published_at,
                is_published_in_tg=False,
                channel_id=channel_id,
            )

            youtube_videos.append(video)

    return youtube_videos
