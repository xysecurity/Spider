import requests
r=requests.session()
url = 'http://10.3.8.211'
headers={'Referer':'https://auth.bupt.edu.cn/authserver/login?service=http%3A%2F%2Fmy.bupt.edu.cn%2Findex.portal','User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/58.0'}
data = {'DDDDD': '2014212999', 'upass': 'WANG654321','0MKKey':''}
req = r.post(url=url, data=data)
print(req.text)
