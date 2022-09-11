import requests
from config import YOUTUBE_API_KEY, YOUTUBE_API_ENDPOINT


def get_youtube_videos(channel_id: str, api_key: str) -> list[tuple]:
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
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        video_published_at = item['snippet']['publishedAt']
        video = (video_id, video_title, video_published_at)
        youtube_videos.append(video)

    return youtube_videos

# channelId = 'UC7iatzobQFSzdnpO35PbLuw'
