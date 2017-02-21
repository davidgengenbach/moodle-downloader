#!/usr/bin/env python3

import helper
import argparse
import operator
import functools
import os

WHITE_LIST = 'pdf Exercise Teil Präsentation Tutor Uebung Zusatz Übung Lösung Vorlesung Aufzeichnung Multiplizierer Klausur Tutorial History supplementary video pdfs interfaces'.lower(
).split(' ')
BLACK_LIST = 'Forum Gruppe Sprechstunden'.lower().split(' ')


def main():
    parser = argparse.ArgumentParser(description="Download moodle assets")
    parser.add_argument('--url', default='https://moodle.informatik.tu-darmstadt.de/course/view.php?id=155')
    args = parser.parse_args()

    if not os.path.exists('user.txt'):
        print(
            'No "user.txt" in this folder. Please put your username and password on their own line in the "user.txt" file.')
        exit(1)

    user, password = [x.strip() for x in open('user.txt').read().split() if x.strip() != '']
    download_assets(args.url, user, password)


def download_file(browser, url, folder):
    page = browser.get(url)
    filename = page.headers['Content-Disposition'].split('"')[-2]
    with open(folder + '/' + filename, 'wb') as f:
        f.write(page.content)


def sanitize_title(title):
    return title.replace(' ', '_').replace('/', '-').replace(':', '-').replace('-', '_')


def download_assets(url, username, password):
    browser = helper.login(url, username, password)
    page = browser.get(url)
    title = sanitize_title(page.soup.find('title').text)
    asset_links = page.soup.select('body .activityinstance a')
    asset_links_filtered = []
    for link in asset_links:
        if filter_element(link):
            asset_links_filtered.append(link)

    folder_name = 'out/' + title
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    for asset in asset_links_filtered:
        link = asset.attrs['href']
        download_file(browser, link, folder_name)


def filter_element(link):
    ICON_WHITELIST = ['pdf-24', 'archive-24']
    icon_name = link.select('img')[0].attrs['src'].split('/')[-1]
    return icon_name in ICON_WHITELIST

if __name__ == '__main__':
    main()
