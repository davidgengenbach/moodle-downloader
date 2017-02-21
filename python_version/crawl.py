#!/usr/bin/env python3

import helper
import argparse
import operator
import functools
import os


def main():
    parser = argparse.ArgumentParser(description="Download moodle assets")
    parser.add_argument('--url', default='https://moodle.informatik.tu-darmstadt.de/course/view.php?id=155')
    args = parser.parse_args()
    user, password = helper.get_credentials()
    download_assets(args.url, user, password)


def sanitize_title(title):
    return title.replace(' ', '_').replace('/', '-').replace(':', '-').replace('-', '_')


def download_assets(url, username, password, out_folder='out'):
    print('Logging in')
    browser = helper.login(url, username, password)
    page = browser.get(url)
    title = sanitize_title(page.soup.find('title').text)
    print('Retrieving links')
    asset_links = page.soup.select('body .activityinstance a')
    asset_links_filtered = []
    for link in asset_links:
        if filter_element(link):
            asset_links_filtered.append(link)
        else:
            print('\tWill not get downloaded: "{}"'.format(link.text))

    folder_name = out_folder + '/' + title
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    print('Starting download')
    for asset in asset_links_filtered:
        link = asset.attrs['href']
        print('\tDownloading: "{}"'.format(asset.text))
        download_file(browser, link, folder_name)


def filter_element(link):
    ICON_WHITELIST = ['pdf-24', 'archive-24']
    icon_name = link.select('img')[0].attrs['src'].split('/')[-1]
    return icon_name in ICON_WHITELIST


def download_file(browser, url, folder):
    page = browser.get(url)
    filename = page.headers['Content-Disposition'].split('"')[-2]
    with open(folder + '/' + filename, 'wb') as f:
        f.write(page.content)

if __name__ == '__main__':
    main()
