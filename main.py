from NewsSubscriber import Subscriber
from ReaderSpider import ReaderSpider
from ScanningLogic import WXGZH
import asyncio

subscribeUrls = [
    'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzkwMzE4NTU3MQ==&scene=124#wechat_redirect', # 财经
    'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=Mzg3ODYwMjA3NA==&scene=124#wechat_redirect', # 黑夜批判公社
]

async def test():
    rs = ReaderSpider(apiMode='r', respondMode='markdown')

    subscriber = Subscriber(rs, logsLength = 20)
    with open("output.txt", "w", encoding="utf-8") as f:
        for url in subscribeUrls:
            articles = await subscriber.getNewsFromChannel(url, WXGZH)
            f.write(str(articles) + "\n")

asyncio.run(test())