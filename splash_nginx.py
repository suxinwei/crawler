from time import sleep

import requests
from urllib.parse import quote
import re


def test():
    lua = '''
    function main(splash, args)
        local treat = require("treat")
        local response = splash:http_get("http://httpbin.org/get")
        return treat.as_string(response.body)
    end 
    '''
    url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
    response = requests.get(url, auth=('admin', '930615'))
    ip = re.search('(\d+\.\d+\.\d+\.\d+)', response.text).group(1)
    print(ip)


if __name__ == '__main__':
    while 1:
        test()
        sleep(1)
