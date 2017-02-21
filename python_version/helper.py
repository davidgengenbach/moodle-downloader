import mechanicalsoup
import getpass

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

def get_credentials():
    CREDENTIALS_FILE = 'user.txt'
    def get_by_file():
        with open(CREDENTIALS_FILE, 'r') as f:
            contents = [x.strip() for x in f.readlines() if x.strip() != '']
            if len(contents) != 2:
                raise Exception('Error retrieving username/password: File {} does not have two lines. Content: "{}"'.format(CREDENTIALS_FILE, '\n'.join(contents)))
            return contents

    def ask_user():
        username = None
        password = None
        while username is None:
            username = input('TUID: ')
        while password is None:
            password = getpass.getpass('Password: ')
        return username, password

    # First try to get the user credentials by file, afterwards by programm arguments
    try:
        return get_by_file()
    except:
        pass

    try:
        return ask_user()
    except:
        pass
    raise(Exception('Could not retreive username/password. Are you doing this on purpose?'))