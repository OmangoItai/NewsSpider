import aiohttp

class ReaderSpider:
    def __init__(self, apiMode: str = 'r', respondMode: str = 'markdown', ) -> None:
        if respondMode != 'markdown' and respondMode != 'text' and respondMode != 'html' and respondMode != 'screenshot':
            raise(ValueError('ReaderSpider constructor(): arg \"respondMode\" must be \"markdown\", \"text\", \"html\" or \"screenshot\".'))
        self.ReaderApi = f'https://{apiMode}.jina.ai/'
        self.headers = {'x-respond-with': respondMode}
    
    async def getTextFromUrl(self, url: str, returnType: str = 'json'):
        if url == '':
            raise(ValueError('ReaderSpider fetch(): arg \"url\" can not be empty.'))
        # todo: more returnType
        if returnType != 'text' and returnType != 'json':
            raise(ValueError('ReaderSpider fetch(): arg \"returnType\" must be \"text\" or \"json\".'))

        if(returnType == 'json'):
            self.headers['Accept'] = 'application/json'

        url = f'{self.ReaderApi}{url}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as res:
                if res.status == 200:
                    if(returnType == 'text'):
                        return await res.text()
                    elif(returnType == 'json'):
                        return await res.json()
                else:
                    return f'JinaReader API fail with statusCode: {res.status}'