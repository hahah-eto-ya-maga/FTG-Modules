from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError, TimeoutError
from telethon.tl.types import MessageMediaDocument
from .. import loader, utils
from asyncio import sleep


def register(cb):
	cb(demotivator2Mod())


class demotivator2Mod(loader.Module):
    """Демотиватор 2.0 @super_rjaka_demotivator_bot"""

    strings = {'name': 'Демотиватор2.0'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def demcmd(self, message):
        """ .dem фото или гиф"""
        
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not reply:
            return await message.edit("<b>Реплай на медиа</b>")
        try:
           media = reply.media
        except:
            return await message.edit("<b>Реплай только на медиа</b>")
        delGif = False    
        gifs = await message.client(functions.messages.GetSavedGifsRequest(hash=0))
        for gif in gifs.gifs:
            try:
                if gif.id == media.document.id:
                    delGif = False
                    break
                else: 
                    delGif = True
                    break
            except: break

        chat = '@super_rjaka_demotivator_bot'
        await message.edit('<b>Дединсайд...</b>')
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1016409811))
                await message.client.send_file(chat, media, caption=args)  
                response = await response
            except YouBlockedUserError:
                return await message.edit(f'<b>Разблокируй {chat}</b>')
            except TimeoutError:
                return await message.edit(f'<b>Бот {chat} сдох</b>')

            if response.media is None:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1016409811))
                response = await response

            await message.delete()
            await message.client.send_file(message.to_id, response.media, reply_to=await message.get_reply_message())
            await message.client(
                functions.messages.DeleteHistoryRequest(peer='super_rjaka_demotivator_bot', max_id=0, just_clear=False, revoke=True))
            await message.client(functions.messages.SaveGifRequest(id=response.media, unsave=True))
            if delGif:
                await message.client(functions.messages.SaveGifRequest(id=media, unsave=True))