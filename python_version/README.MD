## Introduction

You can use this script to download the moodle assets.

Caveats:
It does filter the assets by their type. Currently the only types that get downloaded are
- `pdf`
- `archive`
- `sourcecode`
- `mpeg`
- `powerpoint`.



Other types can be added pretty easy by changing `ICON_WHITELIST` in the `filter_element` function in the `crawl.py`. You have to get the icon name to add to this list on the moodle site.

Downloading folders is currently not implemented.

## Instructions

Execute these commands:

```bash
# Or download the repo manually
git clone git@github.com:davidgengenbach/moodle-downloader.git

cd moodle-downloader/python_version

# Only once
pip3 install -r requirements.txt

# The URL_TO_MOODLE_COURSE something like 'https://moodle.informatik.tu-darmstadt.de/course/view.php?id=155'
python3 crawl.py --url URL_TO_MOODLE_COURSE
# The downloaded assets will now reside in out/{course_title}

# If you don't want to enter the TUID credentials all the time,
# you can create a user.txt file with the username/password on seperate lines:
echo "TUID" > user.txt
echo "PASSWORD" >> user.txt
```