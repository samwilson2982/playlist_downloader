import argparse
from src.controllers.app_controller import AppController
parser = argparse.ArgumentParser(description='tool to download a single youtube video, or a playlist, and then convert them to both mp4 and mp3')

parser.add_argument('-p', '--playlist',
                    action ='store_true',
                    help ='a flag to denote if the url given is a playlist')

parser.add_argument('-u', '--url',
                    required = True,
                    action ='store',
                    help ='a youtube video you want to download, or the 1st video in a playlist')

args = parser.parse_args()

if args.playlist is None:
    args.playlist = False

app = AppController(video_url=args.url, playlist=args.playlist)
