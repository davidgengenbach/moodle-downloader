import mechanicalsoup

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
