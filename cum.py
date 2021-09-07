# coded by Y4sperMaglot

from telethon.tl.types import MessageMediaPhoto
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events, functions
from asyncio import sleep
import random
from .. import loader, utils

@loader.tds
class CummingMod(loader.Module):
    """Хуй знает мне похуй"""
    strings = {'name': 'Cumer'}

    async def cumcmd(self, message):
        """.cum VK или Telegram или пусто"""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)

        async def client_ready(self, client, db):
            self.client = client

        if not reply:
            await message.edit('<b>Реплай на картинку</b>')
            return

        if 'Telegram' not in args and 'VK' not in args:
            rnd_args = ['Telegram', 'VK']
            args = random.choice(rnd_args)

        try:
            photo = reply.photo
        except:
            await message.edit('<b>Реплай на картинку</b>')
            return

        bot = '@sperm0_bot'
        await message.edit('<b>Cumming...</b>')

        async with message.client.conversation(bot) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, pattern='Я КОНЧИЛ!', from_users=1951341661))
                await message.client.send_message(bot, args)
                await sleep(1)
                await message.client.send_file(bot, photo)
                response = await response
            except YouBlockedUserError:
                await message.reply('<b>Разблокируй @sperm0_bot и подпишись на https://t.me/origache</b>')
                return

            await message.delete()
            await message.client.send_file(message.to_id, response.media, reply_to=await message.get_reply_message())
            await message.client(
                functions.messages.DeleteHistoryRequest(peer='sperm0_bot',
                                                        max_id=0,
                                                        just_clear=False,
                                                        revoke=True))