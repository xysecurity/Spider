import requests
url = 'http://example.com/some/cookie/setting/url'
headers={'user-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
jar=requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
print(requests.get(url).cookies)