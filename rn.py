# Coded by D4n1l3k300
# t.me/D4n13l3k00

from telethon import functions, types, events
from .. import loader, utils
from telethon.errors.rpcerrorlist import YouBlockedUserError
import datetime
import random
from asyncio import sleep
def register(cb):
    cb(EyefGodMod())
class EyefGodMod(loader.Module):
    """RndNsfw"""
    strings = {'name': 'RndNsfw'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()
    async def crncmd(self, message):
        """
        Random pic from @wallhaven_nsfw
        """
        await message.edit("<b>_-*Wallhaven_NSFW*-_</b>")
        chat = '@wallhaven_nsfw'
        result = await message.client(functions.messages.GetHistoryRequest(
        peer=chat,
        offset_id=0,
        offset_date=datetime.datetime.now(),
        add_offset=random.choice([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99,101]),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
        ))
        await message.delete()
        await message.client.send_file(message.to_id, result.messages[0].media)
    async def crdcmd(self, message):
        """
        Random post from @dvach18
        """
        await message.edit("<b>_-*2ch_18+*-_</b>")
        chat = '@dvach18'
        result = await message.client(functions.messages.GetHistoryRequest(
        peer=chat,
        offset_id=0,
        offset_date=datetime.datetime.now(),
        add_offset=random.randint(0, 1000),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
        ))
        await message.delete()
        await message.client.send_message(message.to_id, result.messages[0])
    async def crdbcmd(self, message):
        """
        Random post from @ru2ch_ban
        """
        await message.edit("<b>_-*2ch_Ban*-_</b>")
        chat = '@ru2ch_ban'
        result = await message.client(functions.messages.GetHistoryRequest(
        peer=chat,
        offset_id=0,
        offset_date=datetime.datetime.now(),
        add_offset=random.randint(0, 1000),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
        ))
        await message.delete()
        await message.client.send_message(message.to_id, result.messages[0])
    async def crhcmd(self, message):
        """
        Random Hentai from channels
        """
        await message.edit("<b>_-*Hentai*-_</b>")
        chat = '@hentai'
        result = await message.client(functions.messages.GetHistoryRequest(
        peer=chat,
        offset_id=0,
        offset_date=datetime.datetime.now(),
        add_offset=random.randint(0, 1000),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
        ))
        await message.delete()
        await message.client.send_message(message.to_id, result.messages[0])
    async def rh2dcmd(self, message):
        """
        Random Hentai2D pic/gif from @murglar_bot
        You can type category as argument(mustn't)
        """
        chat = '@murglar_bot'
        args = utils.get_args_raw(message)
        if args:
            arg = args
        else:
            arg = None
        await message.edit("<b>_-*Hentai_2D*-_</b>")
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=507490514))
                if arg:
                    m1 = await message.client.send_message(chat, f'/nudes2d {arg}')
                else:
                    m1 = await message.client.send_message(chat, f'/nudes2d')
                response = await response
            except YouBlockedUserError:
                await message.reply('<code>Unblock @murglar_bot</code>')
                return
            await message.client.send_message(message.to_id, response.message)
    async def rn3dcmd(self, message):
        """
        Random Nudes3D from @murglar_bot
        """
        chat = '@murglar_bot'
        await message.edit("<b>_-*Nudes_3D*-_</b>")
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=507490514))
                m1 = await message.client.send_message(chat, '/nudes3d')
                response = await response
            except YouBlockedUserError:
                await message.reply('<code>Unblock @murglar_bot</code>')
                return
            await message.client.send_message(message.to_id, response.message)
    
            
