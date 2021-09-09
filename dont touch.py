# coded by Y4sperMaglot

from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events, functions
from asyncio import sleep
from .. import loader, utils

@loader.tds
class SexMod(loader.Module):
    """"""
    strings = {'name': 'Гениальное - просто'}

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def anamecmd(self, message):
        """"""
        emojis = ['👉', '👈']
        name = 'Фернандо Санчес'

        if not self.db.get("NameEmoji", "status"):
            self.db.set("NameEmoji", "status", True)
            await message.edit("<b>Активировано</b>")
            while self.db.get("NameEmoji", "status"):
                await self.client(functions.account.UpdateProfileRequest(first_name=f'{name} {emojis[0]}{emojis[1]}‍‌‌‌‌‍‌‌‌‌‌‌‌‍‍‍‍‍‍‍‍‍‍‍', last_name=''))
                await sleep(5)
                await self.client(functions.account.UpdateProfileRequest(first_name=f'{name} {emojis[0]}    {emojis[1]}‍‌‌‌‌‍‌‌‌‌‌‌‌‍‍‍‍‍‍‍‍‍‍‍', last_name=''))
                await sleep(5)



        else:
            self.db.set("NameEmoji", "status", False)
            await message.edit("<b>Деактивировано</b>")
            await self.client(functions.account.UpdateProfileRequest(first_name=f'{name}‍‌‌‌‌‍‌‌‌‌‌‌‌‍‍‍‍‍‍‍‍‍‍‍', last_name=''))

