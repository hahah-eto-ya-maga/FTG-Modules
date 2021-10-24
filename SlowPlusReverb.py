from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageMediaDocument
from .. import loader


@loader.tds
class SlowPlusReverbMod(loader.Module):
    """SlowReverb"""

    strings = {'name': 'Slow+Reverb'}

    async def client_ready(self, client, db):
        self._client = client

    async def slowrevcmd(self, message):
        """.slowrev реплай на трек
        Бот реально годный"""
        
        reply = await message.get_reply_message()
        if not reply:
            return await message.edit("<b>Реплай на аудио</b>")
        try:
           media = reply.media
        except:
            return await message.edit("<b>Реплай только на аудио</b>")

        chat = '@slowreverbbot'
        await message.edit('sʟᴏᴡed & ʀᴇᴠᴇʀʙ ...')
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1934970779))
                await message.client.send_file(chat, media)  
                response = await response
            except YouBlockedUserError:
                return await message.edit(f'<b>Разблокируй {chat}</b>')
            if 'Подпишись, пожалуйста, на мой канал' in response.text:
                return await message.edit('<b>Перейди в диалог с ботом и сделай действия которые просит бот</b>')

            if response.media is None:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1934970779))
                response = await response

            await message.delete()
            await message.client.send_file(message.to_id, response.media, caption="<a href='tg://user?id=1934970779'>sʟᴏᴡᴇᴅ & ʀᴇᴠᴇʀʙ</a>", reply_to=await message.get_reply_message())
            await message.client(
                 functions.messages.DeleteHistoryRequest(peer='slowreverbbot', max_id=0, just_clear=False, revoke=True))
            
            