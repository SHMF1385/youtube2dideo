import sys
import argparse
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


parser = argparse.ArgumentParser(description="converts youtube links into dideo links")
parser.add_argument("url", help="youtube video url")
parser.add_argument("--check", dest="check", action="store_const", const=True, default=False)
parser.add_argument("--open-in-browser", dest="open", action="store_const", const=True, default=False)
args = parser.parse_args()


def main():
    video_code = args.url.split('?v=')[1]
    video_url = "https://www.dideo.ir/v/yt/{}/".format(video_code)
    print(video_url)
    if args.check and CheckUrl(video_url) and args.open: 
        open_browser(video_url)

if __name__ == "__main__": main()