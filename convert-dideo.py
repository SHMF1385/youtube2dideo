import sys
import argparse
import subprocess
from webbrowser import open as open_browser

def CheckUrl(url):
    try:
        import requests
        
        print("Checking for possible errors ...")
        respons = requests.get(url)
        
        if respons.ok:
            print("No errors")
            return True

        raise Exception("Not ok respons")

    except ModuleNotFoundError:
        print("Please install 'requests' first.")
        return False

    except Exception:
        print("Link is broken.")
        return False

def DownloadVideo(url):
    print("Ruuning youtube-dl with given url ...")
    command = ['youtube-dl',url]
    try:
        print("Ruuning youtube-dl with given url ...")
        subprocess.run(command)
    except FileNotFoundError:
        print("Youtube-dl not found!")



parser = argparse.ArgumentParser(description="converts youtube links into dideo links")
parser.add_argument("url", help="youtube video url")
parser.add_argument("--check", dest="check", action="store_const", const=True, default=False,help='Checks if the link is broken')
parser.add_argument("--open-in-browser", dest="open", action="store_const", const=True, default=False,help='Opens the converted link in browser')
parser.add_argument("--download", dest="download", action="store_const", const=True, default=False,help='Downloads the video with youtube-dl')
args = parser.parse_args()


def main():
    if 'list' in args.url:
        args.url = args.url.split("&list=")[0]
    
    video_code = args.url.split('?v=')[1]
    video_url = f"https://www.dideo.ir/v/yt/{video_code}/"
    print(video_url)
    if CheckUrl(video_url) and args.open: 
        open_browser(video_url)
    if args.download and CheckUrl(video_url):
        DownloadVideo(video_url)


if __name__ == "__main__": main()
