import requests
import urllib.parse
import random

token = "54e88bca11504c90b8a184e06c3d89ac7814f7e9a4d"

link = "https://luglawhaulsano.net/4/8605030"

targetUrl = urllib.parse.quote(link)

#super = "true"

geoCode = "de"

#regionalGeoCode = "europe"
#asia 亚洲 europe 欧洲 africa 非洲  oceania 大洋洲 northamerica 北美 southamerica 南美洲  
sessionId = str(random.randint(2000, 4000))

timeout = "120000"   # 5000 毫秒和 120000 毫秒

device = "mobile"   # desktop 和 mobile 

customWait = "35000"

render = "true"

height = "1280"
width = "720"

blockResources = "false"

#url = "http://api.scrape.do?token={}&url={}&super={}&geoCode={}&sessionId={}&timeout={}&device={}&customWait={}&render={}&blockResources={}&height={}&width={}".format(token, targetUrl, super, geoCode, sessionId, timeout, device, customWait, render, blockResources, height, width)
url = "http://api.scrape.do?token={}&url={}&geoCode={}&sessionId={}&timeout={}&device={}&customWait={}&render={}&blockResources={}&height={}&width={}".format(token, targetUrl, geoCode, sessionId, timeout, device, customWait, render, blockResources, height, width)
response = requests.request("GET", url)

print(response.text)
















