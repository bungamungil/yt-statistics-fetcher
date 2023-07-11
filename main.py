from dotenv import load_dotenv
from fetch_channels_id import fetch_channels_id
from fetch_channels_detail import fetch_channels_detail


def main():
    load_dotenv()
    channels_id = fetch_channels_id()
    channels_detail = fetch_channels_detail(channels_id)
    for channel_detail in channels_detail:
        for channel in channel_detail:
            print(channel["snippet"]["title"])


if __name__ == "__main__":
    main()
