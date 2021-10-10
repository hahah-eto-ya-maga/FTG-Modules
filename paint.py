# coded by Y4sperMaglot

from telethon.tl.types import MessageMediaDocument
from telethon.errors.rpcerrorlist import YouBlockedUserError, TimeoutError
from telethon import events, functions
from .. import loader, utils

@loader.tds
class KrasitelEbatMod(loader.Module):
    """Закрасит вашу черно-белую фотографию"""
    strings = {'name': 'Paint'}

    async def paintcmd(self, message):
        reply = await message.get_reply_message()

        async def client_ready(self, client, db):
            self.client = client

        if not reply:
            return await message.edit('<b>Реплай на картинку</b>')
            
        try:
            photo = reply.media
        except:
            return await message.edit('<b>Реплай на картинку</b>')
            
        bot = '@ColoriZatioN_Bot'
        await message.edit('<b>Работаем работаем...</b>')

        async with message.client.conversation(bot) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, pattern='Пушистая', from_users=1076532061))

                await message.client.send_file(bot, photo)
                response = await response
            except YouBlockedUserError:
                return await message.reply('<b>Разблокируй @ColoriZatioN_Bot</b>')
            except TimeoutError:
                return await message.edit("<b>Бот @ColoriZatioN_Bot сдох</b>")

            await message.delete()
            await message.client.send_file(message.to_id, response.media, reply_to=await message.get_reply_message())
            await message.client(
                functions.messages.DeleteHistoryRequest(peer='ColoriZatioN_Bot',
                                                        max_id=0,
                                                        just_clear=False,
                                                        revoke=True))