import requests
from lxml import etree

page = 2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
req = requests.get(url)
sele1 = etree.HTML(req.text)
print(sele1)
#author = sele1.xpath('//div[@class="author clearfix"]/a[2]/h2')
#content = sele1.xpath('//div[@class="content"]')
num=sele1.xpath('//div[@id="content-left"]/div')
content = sele1.xpath('//div[@class="content"]//span')
author=sele1.xpath('//div[@class="author clearfix"]/a[2]//h2')
print(num)
print(len(num))
for i in range(len(num)-1):
    print("序号"+str(i))
    print("作者：" + author[i].text)
    print("正文："+content[i].text)




