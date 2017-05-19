#! python3
#爬“得到”分享的网页。

import logging,os,re
from urllib.request import urlopen
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.INFO)

#先输入目标网址
UrlO = "https://m.igetget.com/share/audio/aid/4PqPxQPcfkdTSjdQAoSF"
url1 = urlopen(UrlO)
bsObj = BeautifulSoup(url1,'lxml')

title = str(bsObj.h1.get_text())
content1 = str(bsObj.findAll(class_="text"))
#正则匹配时[需要转义
reg = re.compile(r'(</p><p>|<br/>|</p>|\[<div class="text"> <p>)')
content = reg.sub('\n',content1)

logging.debug(content)
logging.debug(str(title))

#保存爬取内容在指定目录下。
os.chdir('C:\\1')
logging.debug(os.getcwd())
f = open(title+'.txt','w')
f.write(content)
f.close()
