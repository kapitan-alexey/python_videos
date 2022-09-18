import requests
from get_videos_service.youtube_client import get_youtube_videos


def test_get_youtube_videos_WHEN_request_sent_THEN_got_response(monkeypatch):

    # GIVEN
    class Mock:
        def __init__(self):
            self.response = {
                "items": [{
                    "id": {
                        "videoId": "test_video_id"},
                    "snippet": {
                        "publishedAt": "2019-10-16T04:12:22Z",
                        "title": "test_title"
                    }}]}

        def json(self):
            return self.response

    response = Mock()

    def mock_return(*args, **kwargs):
        return response

    channel_id = "some_channel_id"
    api_key = "some_api_key"

    expected = [("test_video_id", "test_title", "2019-10-16T04:12:22Z")]

    # WHEN
    monkeypatch.setattr(requests, "get", mock_return)
    result = get_youtube_videos(channel_id, api_key)

    # THEN

    assert expected == result
