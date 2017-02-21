## Introduction

You can use this script to download the moodle assets.

Caveats:
It does filter the assets by their type. Currently the only types that get downloaded are
- `pdf`
- `archive`

Other types can be added pretty easy by changing `ICON_WHITELIST` in the `filter_element` function in the `crawl.py`. You have to get the icon name to add to this list on the moodle site.

## Instructions

```bash
# Only once
pip3 install -r requirements.txt

# The URL_TO_MOODLE_COURSE something like 'https://moodle.informatik.tu-darmstadt.de/course/view.php?id=155'
python3 crawl.py URL_TO_MOODLE_COURSE
# The downloaded assets will now reside in out/{course_title}

# If you don't want to enter the TUID credentials all the time,
# you can create a user.txt file with the username/password on seperate lines:
echo "TUID" > user.txt
echo "PASSWORD" >> user.txt
```