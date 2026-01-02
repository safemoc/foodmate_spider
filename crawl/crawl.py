import sys

import requests
from bs4 import BeautifulSoup
import re
from units import disguise, check_status_code, logger


def articles(url):
    logger.info(f"==> 文章链接爬虫 开始获取 <==")
    response = requests.get(**disguise(url), hooks={'response': [check_status_code]})

    while response:
        logger.info(f"==> 文章链接爬虫 开始循环 <==")
        soup = BeautifulSoup(response.content, 'html.parser')
        li_elements = soup.find_all('li', class_='catlist_li')
        logger.info(f"==> 文章链接爬虫 开始获取链接链、列表 <==")
        for li in li_elements:
            a = li.find('a')
            if a and a.get('href'):
                logger.info(f"==> 文章链接爬虫 产出链接：{a['href']} <==")
                yield a['href']
        div_element = soup.find('div', class_='pages')
        if not div_element:
            break

        page_str = div_element.find('cite').get_text(strip=True)
        m = re.search(r'/(\d+)页', page_str)
        if not m:
            break

        all_page = int(m.group(1))

        logger.info(f"==> 文章链接爬虫 获取总页数为：{all_page} <==")
        now_page =div_element.select_one('#destoon_pageno')
        if not now_page.get('value'):
            break

        now_page = int(now_page.get('value'))
        logger.info(f"==> 文章链接爬虫 获取当前页数为：{now_page} <==")
        if now_page >= all_page:
            break
        next_a = div_element.find_all('a')[-1]
        logger.info(f"==> 文章链接爬虫 跳转下一页 <==")

        response = requests.get(
            **disguise(next_a['href']),
            hooks={'response': [check_status_code]}
        )


def standard():
    ...


if __name__ == '__main__':
    ...
