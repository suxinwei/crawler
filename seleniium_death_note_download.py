import os

import requests
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'http://www.zzzfun.com'
video_pages_url = 'http://www.zzzfun.com/vod-detail-id-51.html'


def get_video_download_pages(url):
    doc = pq(url=url)
    items = doc('.episode.clearfix')
    a = items.find('a')
    for item in a.items():
        yield item.attr('href')


def get_video_download_url(url):
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 60)
        until = wait.until(EC.presence_of_element_located((By.ID, 'playleft')))
        browser.switch_to.frame(until.find_element_by_tag_name('iframe'))
        download_url = browser.find_element_by_tag_name('source').get_attribute('src')
        return download_url
    except NoSuchElementException as e:
        print('Error', e.args)
        browser.close()


def save_video(url):
    dir = 'F:/多媒体/死亡笔记'
    if not os.path.exists(dir):
        os.mkdir(dir)
    try:
        find = url.find('.mp4')
        file_name = url[find - 2:find]
        file_path = dir + '/' + '{0}.{1}'.format(file_name, 'mp4')
        if not os.path.isfile(file_path):
            response = requests.get(url)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
        else:
            print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Video')


if __name__ == '__main__':
    browser = webdriver.Chrome()
    video_download_pages = get_video_download_pages(video_pages_url)
    for video_download_page in video_download_pages:
        video_download_url = get_video_download_url(base_url + video_download_page)
        save_video(video_download_url)
    browser.close()
