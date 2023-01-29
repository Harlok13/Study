import aiohttp
import asyncio
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.data = None
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    def __iter__(self):
        self.index = -1
        return self
    def __next__(self):
        if self.index >= len(self.data)-1:
            raise StopIteration
        else:
            self.index += 1
            return self.data[self.index]
    def get_data(self, html):
        soup = BeautifulSoup(html, 'lxml')
        shop_items = soup.find('div', class_='container mt-4').find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for i in shop_items:
            img = 'https://scrapingclub.com/' + i.find('div', class_='card').find('img').get('src')
            url = 'https://scrapingclub.com/' + i.find('div', class_='card').find('a').get('href')
            text = i.find('h4').text.strip()
            price = i.find('h5').text.strip()
            data = {'img': img, "url": url, 'text': text, 'price': price}
            yield data

    async def get_html(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                s = self.get_data(await response.text())
                return s

    async def main(self):
        sp = []
        for i in range(1, 8):
            task = asyncio.create_task(self.get_html(f'https://scrapingclub.com/exercise/list_basic/?page={i}'))
            sp.append(task)
        s = await asyncio.gather(*sp)
        self.data = s
