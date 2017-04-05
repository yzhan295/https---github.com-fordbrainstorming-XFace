import requests

url = 'http://mylincolnmobile.cn:88/myford-poc/face/photo/verify/vin'
path = u'C:/temp/tmac4.jpg'
print path
data = {
    'vin': 'LVSH11231241241'
}
files = {'file': open(path, 'rb')}
r = requests.post(url, data=data, files=files)
print r.url,r.text