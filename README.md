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

## Usage

you can use this program like this:

```batch
$ python3 -m convert-dideo [video_url] [--options]
```

### Options

* `--check` : checks if the link is not broken (by sending a request to the server)
* `--open-in-browser` : opens the generated link in your default browser

### Special thanks to:
[MSKF](https://github.com/mskf1383)  
[Amohammadi2](https://github.com/Amohammadi2)  
For improving the program!  
