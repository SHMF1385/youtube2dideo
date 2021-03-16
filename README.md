# Youtube2Dideo

This program converts youtube video links to dideo.ir  

## Installation  

### Requirements:

* requests library  

install the requirements using this command:  

```batch
$ pip install -r requirements.txt
```

and then run the setup script (run as super user for system install) :

```batch
$ python3 setup.py install 
```

* youtube-dl (optional)   
If installed program can download the video.   
Install the program using your OS package manager.   

## Usage

You can use this program like this:

```batch
$ python3 -m convert-dideo [video_url] [--options]
```

### Options

* `--check` : checks if the link is not broken (by sending a request to the server) 
* `--open-in-browser` : opens the generated link in your default browser (CAN ONLY USED WHEN CHECK OPTION IS ENABLE)
* `--download` : downloads the video using youtube-dl (CAN ONLY USED WHEN CHECK OPTION IS ENABLE)

### Special thanks to:
[MSKF](https://github.com/mskf1383)  
[Amohammadi2](https://github.com/Amohammadi2)  
For improving the program!  

### Highly recommended
I highly recommend to don't even bother checking the dideo website and just download the video.   
They're selling the FREE videos to you :|   
