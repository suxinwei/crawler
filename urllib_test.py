import socket
import urllib.request
import urllib.parse
import urllib.error
from urllib.parse import urlparse

# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.getheaders())
# print(response.getheader('server'))

# data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('https://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# try:
#     response2 = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)
#     print(response2.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
