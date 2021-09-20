# Код дерьма by Y4sperMaglot

from .. import loader, utils
import time
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import functions
from asyncio import sleep

@loader.tds
class AutonameMod(loader.Module):
    """Музыка в био"""
    string = {'name': 'AutoNameTime'}

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def autonamefscmd(self, message):
        """.autonamefs name, {time} or {time}, name"""

        name = utils.get_args_raw(message)
        nametime = name.split(',')

        if '{time}' in nametime[0]:
            name = nametime[1]
        else:
            name = nametime[0]
        if not self.db.get("Autonamefs", "status", False):
            self.db.set("Autonamefs", "status", True)
            seconds = time.strftime("%S")
            start = 60 - int(seconds)
            await message.edit('<b>Старт через {} сек...</b>'.format(start))
            await sleep(start)
            await message.delete()
            while self.db.get("Autonamefs", "status", True):
                ctime = time.strftime('%H:%M')
                if '{time}' in nametime[0]:
                    name = '{} {}'.format(ctime, nametime[1])
                else:
                    name = '{} {}'.format(nametime[0], ctime)
                await self.client(functions.account.UpdateProfileRequest(first_name=name))
                await sleep(60)
        else:
            self.db.set("Autonamefs", "status", False)
            await message.edit('<b>Деактивировано.</b>')
            await self.client(functions.account.UpdateProfileRequest(first_name=name))
