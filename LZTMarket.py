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
        await message.edit('<b>Получение ссылки...</b>')
        UserAgent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Acoo Browser; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 2.0.50727)'

        # Получение ссылки #
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not reply and not args:
            await message.edit('<b>Реплай или ссылка</b>')
            return

        url = args or reply.raw_text
        if 'lolz.guru/market' not in url and len(url) < 27:
            await message.edit('<b>Ссылки нет</b>')
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
                "Cookie": f'df_id={strbyte}',
                "Accept-Language": "ru"})
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
            return

        try:
            header = soup.find_all('h1', class_='h1Style marketItemView--titleStyle fl_l')[0].string.strip()   # Заголовок
        except:
            header = "Пустой"

        sellerCon = soup.find('a', class_='username fl_l')
        seller = sellerCon.findChildren('span')[0].string.strip()     # Селлер

        price = soup.find_all('span', class_='value')[0].string.strip()  # Цена

        try:
            accorigin = soup.find_all('abbr', class_='DateTime')[0].string.strip()
        except:
            accorigin = soup.find_all('span', class_='DateTime')[0].string.strip()    # Дата

        if 'world of tanks' in service_account.lower():
            tanks = soup.find('ul', id='wotTabs')
            tanks_child = tanks.findChildren('span', 'muted')

            tops = tanks_child[0].string.strip()
            premTanks = tanks_child[1].string.strip()
            allTanks = tanks_child[2].string.strip()

            label = soup.find_all('div', class_='label')
            region = label[0].string.strip()
            phone = label[1].string.strip()
            gold = label[2].string.strip()
            silv = label[3].string.strip()
            battles = label[4].string.strip()
            victory = label[5].string.strip()
            clan = label[6].string
            prem = label[7].string.strip()
            active = label[8].string.strip()
            reg = label[9].string.strip()
            clan = 'Неизвестно' if label[6].string is None else clan.strip()

            await message.delete()
            await message.client.send_message(message.to_id, f'<b>Информация о товаре:</b>\n🎪 Контора:  {service_account}\n🏷 Заголовок:  {header}\n👨‍💻 Продавец:  {seller}\n💵 Цена:  {price}руб\n⌛ Дата публикации:  {accorigin}\n\n <b>Информация об аккаунте World of Tanks:</b>\n🦽 Все танки:  {allTanks}\n🦽 Топы:  {tops}\n🦽 Премы:  {premTanks}\n🌎 Регион:  {region}\n📱 Привязка к телефону:  {phone}\n💰 Золото:  {gold}\n💵 Серебро:  {silv}\n⚔ Количество боёв:  {battles}\n🏆 Количество(процент побед):  {victory}\n🏳️‍🌈 Клан:  {clan}\n🥇 Премиум:  {prem}\n🤹‍♂ Последняя активность:  {active}\n💳 Дата регистрации:  {reg}\n\n🔗 Ссылка на трейд:  {link}', reply_to=await message.get_reply_message())

        elif 'вконтакте' in service_account.lower():
            label = soup.find_all('div', class_='label')
            friends = label[0].string.strip()
            subs = label[1].string.strip()
            votes = label[2].string.strip()
            auth = label[3].string.strip()
            phone = label[4].string.strip()
            email = label[5].string.strip()
            sex = label[6].string.strip()
            yo = label[7].string.strip()
            conreg = soup.find('div', class_='marketItemView--mainInfoContainer')
            reg = conreg.findChildren('span', class_='DateTime')[0].string.strip()

            await message.delete()
            await message.client.send_message(message.to_id, f'<b>Информация о товаре:</b>\n🎪 Контора:  {service_account}\n🏷 Заголовок:  {header}\n👨‍💻 Продавец:  {seller}\n💵 Цена:  {price}руб\n⌛ Дата публикации:  {accorigin}\n\n <b>Информация об аккаунте ВКонтакте:</b>\n👤 Количество друзей:  {friends}\n👥 Количество подписчиков:  {subs}\n📢 Количество голосов:  {votes}\n🛡 Двухэтапная аутентификация:  {auth}\n📱 Привязка к телефону:  {phone}\n✉ Привязка к почте:  {email}\n🤡 Пол:  {sex}\n💯 Возраст:  {yo}\n💳 Дата регистрации:  {reg}\n\n🔗 Ссылка на трейд:  {link}', reply_to=await message.get_reply_message())
                    # блять я заебался выбирать смайлы

        elif 'origin' in service_account.lower():
            gamesCon = soup.find_all('div', class_='gameTitle')
            games = ''
            for game in gamesCon:
                games += f'{game.string.strip()}, '
            games = games[:-2]

            infCon = soup.find_all('div', class_='marketItemView--counters')
            for sub in infCon:
                check = sub.findChildren('div', class_='counter ea_subscription')
                if check:
                    subscribe = check[0].findChildren('div', class_='label')[0].string.strip()
                    country = sub.findChildren('div', class_='label')[1].string.strip()
                    break

            await message.delete()
            await message.client.send_message(message.to_id, f'<b>Информация о товаре:</b>\n🎪 Контора:  {service_account}\n🏷 Заголовок:  {header}\n👨‍💻 Продавец:  {seller}\n💵 Цена:  {price}руб\n⌛ Дата публикации:  {accorigin}\n\n <b>Информация об аккаунте Origin:</b>\n🎮 Игры:  {games}\n🎫 Тип подписки:  {subscribe}\n🌎 Страна:  {country}\n\n🔗 Ссылка на трейд:  {link}', reply_to=await message.get_reply_message())
        else:
            await message.client.send_message(message.to_id, f'<b>Информация о товаре:</b>\n🎪 Контора:  {service_account}\n🏷 Заголовок:  {header}\n👨‍💻 Продавец:  {seller}\n💵 Цена:  {price}руб\n⌛ Дата публикации:  {accorigin}\n\n🔗 Ссылка на трейд:  {link}', reply_to=await message.get_reply_message())




















