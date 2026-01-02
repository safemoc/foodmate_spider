from units import Response
from units import logger


def disguise(url, header=None, *args, **kwargs):
    if header is None:
        header = {"User-Agent": "Mozilla/5.0"}

    return {'url': url, 'headers': header, }


def print_status_code(resp: Response, *args, **kwargs):
    print(f"状态码：{resp.status_code}\n")
    print(f"请求链接：{resp.url}\n")

    return resp


def check_status_code(resp: Response, *args, **kwargs):
    if resp.status_code in ("404", "502"):
        raise Exception()
    return resp


def test(func):
    def wrapper(*args, **kwargs):
        logger.info(f"==> 启动调试function：{func.__name__} <==")
        return func(*args, **kwargs)

    return wrapper
