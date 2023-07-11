import os
from googleapiclient.discovery import build


def fetch_yt_channels_detail_from_api(channel_id):
    """
    Fetch the details of a YouTube channel
    """
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.channels().list(
            part="snippet,contentDetails,statistics", id=channel_id)
    response = request.execute()
    return response


def split_list(a_list, x):
    """
    Split a list into chunks of x items
    """
    return [a_list[i:i + x] for i
            in range(0, len(a_list), x)] 


def fetch_channels_detail(channels_id):
    channels_detail = []
    for channels_id_chunk in split_list(channels_id, 50):
        channels_detail.append(fetch_yt_channels_detail_from_api(channels_id_chunk)["items"])
    return channels_detail
