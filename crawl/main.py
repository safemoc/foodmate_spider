import requests
from bs4 import BeautifulSoup
from units import logger,disguise, check_status_code, print_status_code
from download import download_article
from crawl import articles

def news(url):
    logger.info(f"==> 执行任务:{news.__name__}<==")
    logger.info(f"==> 发送请求 url:{url} <==")
    response = requests.get(**disguise(url), hooks={'response': [check_status_code]})
    logger.info(f"==> 开始解析HTML Response:{f"状态码：{response.status_code}"}<==")
    soup = BeautifulSoup(response.content, 'lxml')
    tags = soup.find('div', class_='menu').find_all('a')
    nav = []
    for a in tags:
        if a['href'] == '/':
            continue
        nav.append({"name": a.get_text(strip=True), "value": f"{url[:-1]}{a['href']}"})

    sub = soup.find('div', class_='a_title').find('a')
    nav.append(
        {"name": sub.get_text(strip=True), "value": sub['href']})
    logger.info(f"==> 获取主题分类 总计捕获: {len(nav)}个分类 <==")
    other = {
        '食品专题': "数据价值不高",
        '食品网刊': "数据价值不高",
        '进出口': "数据价值不高",
    }
    for i in nav:
        logger.info(f"==> 启动资讯链接爬虫器 {i['name']}分类 开始获取 <==")
        if i['name'] in other:
            # 其他专题的 下载器执行
            ...

        for article in articles(i['value']):
            logger.info(f"==> 启动文章下载器 当前文章链接为：{article} <==")
            download_article(article)

    ...


def policy(url):
    logger.info(f"==> 执行任务:{policy.__name__}<==")
    ...


def report(url):
    logger.info(f"==> 执行任务:{report.__name__}<==")
    ...


def science(url):
    logger.info(f"==> 执行任务:{science.__name__}<==")
    ...


def standard(url):
    logger.info(f"==> 执行任务:{standard.__name__}<==")
    logger.info(f"==> 发送请求 url:{url} <==")
    response = requests.get(**disguise(url), hooks={'response': [check_status_code]})
    logger.info(f"==> 开始解析HTML Response:{f"状态码：{response.status_code}"}<==")
    ...


def yielding(url):
    logger.info(f"==> 执行任务:{yielding.__name__}<==")

    ...
