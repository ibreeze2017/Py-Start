import urllib
import http.cookiejar
from urllib import request
from urllib import error

# url = 'http://ixvz.io/sync/test/http.php'
url = 'http://api.assure.com/api/passport/getUserInfo?token=0bb9d4a9808c446bd8e21fcfe1ab0ede5e81d826af30a0c7f4292a1861b9e77cffd79c46164b7e1d6021a21f790eafd0ba4747fe5a8b94e17588c7b5755f9c29ba4452f50620363c624651bfcf3f304c2702a4dc9632c2d32f07e1b027a0613bbb69803c1703b73af06626f932e21c8356241bf9fe8eb2553afffcef322ad41fbf960e90ddb4ffa91777bc0ae354553a8b0c3ad75859526d1ccefa43a1157867fa7c484d4db1f5f4840a5154051fdc1f120a2221b8e12c938ea0e0b2404a4fe1&account=wenwen&password=wenwen'

password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, 'wind', 'wind')
handler = request.HTTPBasicAuthHandler(password_mgr)

cookie_file = 'auth.cookie'
cookie = http.cookiejar.MozillaCookieJar(cookie_file)
handler2 = urllib.request.HTTPCookieProcessor(cookie)

opener = request.build_opener(handler, handler2)
opener.open(url)
cookie.save(ignore_discard=True, ignore_expires=True)

request.install_opener(opener)

try:
    response = request.urlopen(url)
    print(response.read().decode('utf-8'))
except error.HTTPError as e:
    print('HTTP:' + str(e.code) + '->' + e.msg)
finally:
    print('-------------------END-------------------------------')
