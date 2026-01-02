import requests
from bs4 import BeautifulSoup
from units import logger, disguise, check_status_code

from main import save_data


class ArticleDown:
    def __init__(self, response: BeautifulSoup):
        self.data = None
        self.element = None
        self.resp = response
        logger.info(f"==> 文章下载器 已初始化成功 <==")
        ...

    def article_extract(self):
        element = self.resp.find('div', class_='m2')
        self.element = element.find('div', class_='left_box')
        logger.info(f"==> 文章下载器 清洗 HTML<script>标签 <==")
        for ele in element.find_all("script"):
            ele.decompose()
        logger.info(f"==> 文章下载器 清洗 HTML上宣传图片 <==")
        self.element.find('div', class_='gg_adko').decompose()
        logger.info(f"==> 文章下载器 清洗 HTML放大缩小文字按钮 <==")
        for ele in element.find_all('img', class_='c_p'):
            ele.decompose()
        logger.info(f"==> 文章下载器 清洗 HTML上下一篇文章链接 <==")
        self.element.find('div', class_='np').decompose()
        logger.info(f"==> 文章下载器 清洗 HTML相关资讯链接 <==")
        self.element.find('div', class_='related').decompose()
        logger.info(f"==> 文章下载器 清洗 HTML网站声明 <==")
        self.element.find('div', class_='shengming').decompose()
        logger.info(f"==> 文章下载器 清洗 HTML<center>标签 <==")
        self.element.find('center').decompose()
        logger.info(f"==> 文章下载器 清洗 HTML 收藏 <==")
        self.element.find('div', class_='shouc').decompose()
        logger.info(f"==> 文章下载器 清洗 HTML相关资讯导航 <==")
        self.element.find('div', class_='left_head').decompose()
        logger.info(f"==> 文章下载器 清洗 HTML占位空<div> <==")
        for ele in self.element.find_all('div', class_='b10'):
            ele.decompose()
        logger.info(f"==> 文章下载器 清洗 HTML<form>标签 <==")
        self.element.find('form').decompose()
        div_element = self.element.find('div', id="content")
        logger.info(f"==> 文章下载器 清洗 HTML 其他非内容 <div> <==")
        for div in div_element.find_all('div', recursive=False):
            class_ = div.get('class', [])
            if 'content' not in class_:
                div.decompose()
        logger.info(f"==> 文章下载器 清洗 HTML下宣传图片 <==")
        self.element.find('div', id='article').find_all('div', recursive=False)[-1].decompose()
        logger.info(f"==> 文章下载器 清洗 HTML文章日期  <==")
        self.element.find('div', class_='wzsj').decompose()
        logger.info(f"==> 文章下载器 清洗 HTML 完毕  <==")
        ...

    def article_transform(self):
        self.data = {}

        ...

    def article_load(self):
        save_data(self.data)
        ...

    def down_data(self):
        self.article_extract()
        self.article_transform()
        self.article_load()
        return


def download_article(url):
    logger.info(f"==> 获取文章详情 <==")
    response = requests.get(
        **disguise(url),
        hooks={'response': [check_status_code]}
    )
    logger.info(f"==> 已获取文章 开始启动 下载器 <==")

    launcher = ArticleDown(BeautifulSoup(response.content, 'lxml'))
    launcher.down_data()
    logger.info(f"==> 文章:{url} 处理完毕----《over》 <==")
