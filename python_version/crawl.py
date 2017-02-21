#!/usr/bin/env python3

import helper
import argparse
import mechanicalsoup

WHITE_LIST = 'pdf Exercise Teil Präsentation Tutor Uebung Zusatz Übung Lösung Vorlesung Aufzeichnung Multiplizierer Klausur Tutorial History supplementary video pdfs interfaces'.lower().split(' ')
BLACK_LIST = 'Forum Gruppe Sprechstunden'.lower().split(' ');

def main():
    parser = argparse.ArgumentParser(description="Download moodle assets")
    parser.add_argument('--url', default='https://moodle.informatik.tu-darmstadt.de/course/view.php?id=155')
    args = parser.parse_args()
    user, password = [x.strip() for x in open('user.txt').read().split() if x.strip() != '']

    download_assets(args.url, user, password)

def download_assets(url, username, password):
    browser = login(url, username, password)
    page = browser.get(url)
    asset_links = page.soup.select('body .activityinstance a')
    asset_links2 = []
    for link in asset_links:
        print(link.text.lower())
        if link.text.lower() in WHITE_LIST:
            print(link)
    #with open('yes.html', 'w') as f:
    #    f.write(page.text)


def login(url, username, password):
    browser = mechanicalsoup.Browser()
    page = browser.get(url)
    link = page.soup.select('.loginpanel a:nth-of-type(1)')[0].attrs['href']
    login_page = browser.get(link)
    link_domain = "/".join(login_page.url.split('/')[0:3])
    form = login_page.soup.select('form#fm1')[0]
    submit_url = link_domain + form.attrs['action']
    form.select('#username')[0].attrs['value'] = username
    form.select('#password')[0].attrs['value'] = password
    page = browser.submit(form, submit_url)
    return browser

if __name__ == '__main__':
    main()
