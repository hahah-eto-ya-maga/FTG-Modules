# shitcode by Y4sperMaglot

# Пока только так

from .. import loader, utils

from bs4 import BeautifulSoup as BS
import requests
import base64
from asyncio import sleep


@loader.tds
class LZTMarketMod(loader.Module):
    """Вывод содержимого аккаунта с маркета lolz"""

    strings = {'name': 'LZTMarket'}

    async def client_ready(self, client, db):
        self.client = client

    async def lolzcmd(self, message):
        """.lolz реплай или ссылка"""

        UserAgent = 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 6.0; Win64; x64; Trident/5.0; .NET CLR 3.8.50799; Media Center PC 6.0; .NET4.0E)'


        # Получение ссылки #
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not reply and not args:
            await message.edit('<b>Реплай или ссылка</b>')
            return

        url = args or reply.raw_text
        if 'lolz.guru/market/' not in url and len(url) < 27:
            await message.edit('<b>Ссылка на аккаунт в маркете невалидна</b>')
            return

        # Обход защиты парсинга #
        await message.edit('<b>Обход защиты от парсинга...</b>')

        try:
            f = requests.get('https://lolz.guru/process-qv9ypsgmv9.js', headers={
                "User-Agent": UserAgent}).text

            bytes = str(f.split(',')[6]).replace(';(function(_0x2217ae', '').replace('+', '').replace("'", "").replace(']', '')
            strbyte = str(base64.b64decode(bytes).decode('utf-8'))
            page = requests.get(url, headers={
                "User-Agent": UserAgent,
                "Cookie": f'df_id={strbyte}'})
            await message.edit('<b>Успешно</b>')
            await sleep(0.5)

        except:
            await message.edit('<b>Что-то пошло не так...</b>')
            return


        # Получение информации со страницы #
        await message.edit('<b>Получение информации страницы...</b>')

        soup = BS(page.text, 'html.parser')

        link = f'<a href="{url}">Открыть</a>'  # Ссылка

        try:
            service_account = soup.find_all('span', itemprop='title')[1].string.strip()   # Название игры или сервиса
        except:
            await message.edit('<b>Ссылка на аккаунт в маркете невалидна</b>')

        try:
            header = soup.find_all('h1', class_='h1Style marketItemView--titleStyle fl_l')[0].string.strip()   # Заголовок
        except:
            header = "Пустой"

        for count in range(0, 1000):
            try:
                find = soup.find_all('span', class_=f'style{str(count)}')
                
                if find:
                    seller = find[0].string.strip()      # Селлер
                    break
            except:
                pass

        price = soup.find_all('span', class_='value')[0].string.strip()  # Цена

        try:
            accorigin = soup.find_all('abbr', class_='DateTime')[0].string.strip()
        except:
            accorigin = soup.find_all('span', class_='DateTime')[0].string.strip()    # Дата

        await message.delete()

        await message.client.send_message(message.to_id, f'🎪 Контора: {service_account}\n🏷 Заголовок: {header}\n👨‍💻 Продавец: {seller}\n💵 Цена: {price}руб\n⌛ Дата публикации: {accorigin}\n🔗 Ссылка на трейд: {link}')




















