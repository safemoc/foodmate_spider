import sys

from units import *
from crawl import *
from download import *


@test
def out_detail(item):
    with open('./tmp.html', 'wb') as f:
        f.write(item)
    return ...


@test
def save_data(*args, **kwargs):
    print(args, kwargs)


def main():
    logger.info(f"==> 函数开始执行 {main.__name__} <==")
    logger.info(f"==> 发送请求 url:https://www.foodmate.net/ <==")
    response = requests.get(**disguise('https://www.foodmate.net/'), hooks={"response": check_status_code})
    logger.info(f"==> 开始解析HTML Response:{f"状态码：{response.status_code}"}<==")
    soup = BeautifulSoup(response.content, 'html.parser')
    tags = soup.select('a.col_nav_title[href]')
    urls = map(lambda i: (i.get_text(strip=True), i["href"]), tags)
    mapping = {
        "食品资讯": news,
        "食品标准": standard,  # 未开发
        "政策法规": policy,  # 未开发
        "生产技术": yielding,  # 未开发
        "行业报告": report,  # 未开发
        "食品科普": science,  # 未开发
    }
    for info in urls:
        title = info[0]
        url_link = info[1]
        handler = mapping.get(title)
        logger.info(f"==> 获取调度器:{handler.__name__}<==")
        if handler:
            logger.info(f"==> 执行调度器:{handler.__name__}<==")
            handler(url_link)


if __name__ == '__main__':
    main()

    # main()
