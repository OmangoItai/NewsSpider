from typing import Dict, List
from ReaderSpider import ReaderSpider
from ScanningLogic import ScanningLogicType

class Subscriber:

    def __init__(self,readerSpider: ReaderSpider, logsLength = 20, ) -> None:
        self.readerSpider = readerSpider
        self.logsLength = logsLength
        self.subscribeList: List[Dict[str, ScanningLogicType]] = []
        self.newsLogs: Dict[str, List[str]] = {}

    def isNew(self, newsUrl: str, channelUrl: str) -> bool:
        if channelUrl not in self.newsLogs:
            self.newsLogs[channelUrl] = []
        if newsUrl not in self.newsLogs[channelUrl]:
            self.newsLogs[channelUrl].append(newsUrl)
            if len(self.newsLogs[channelUrl]) > self.logsLength:
                self.newsLogs[channelUrl].pop()
            return True
        return False

    async def getNewsFromChannel(self, channelUrl: str, scanningLogic: ScanningLogicType):
        channelNews = []
        urlList = scanningLogic(channelUrl)
        for url in urlList:
            if self.isNew(newsUrl=url, channelUrl=channelUrl):
                res = await self.readerSpider.getTextFromUrl(url, returnType='json')
                channelNews.append(res)
                # 如果你需要的并非增量更新新闻，而是最新的 top x 篇文章
                # else:
                #     read from local storage
                #     channelNews.append(local article)
                
        return channelNews
