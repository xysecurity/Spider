import requests
r=requests.session()
url = 'https://auth.bupt.edu.cn/authserver/login?service=http://my.bupt.edu.cn/index.portal'
headers = {'Referer': 'https://auth.bupt.edu.cn/authserver/login?service=http%3A%2F%2Fmy.bupt.edu.cn%2Findex.portal',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
data = {'_eventId':'submit', 'execution':'e2s10', 'lt':'LT-3234599-17d5ftdoCEfgEL61fcVljLSrK5yM3Z-1528735636755',
        'password': '15', 'rmShown': 1, 'username': '2014212999'}
cookies=dict(JSESSIONID='0001fWxAgowwQ1e9aaGmJbgrt68:1FSKNUA9B4')
req = r.post(url, data=data,cookies=cookies,headers=headers)
print(req.headers)
print(req.cookies)
print(req.text)