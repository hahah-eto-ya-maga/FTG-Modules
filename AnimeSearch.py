# coded by Y4sperMaglot

from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageMediaDocument

from .. import loader

@loader.tds
class AnimeSearchMod(loader.Module):
    """Поиск тайтлов, аниме, персов и т.д с помощью @Anime_Reverse_Search_Bot"""
    strings = {"name": "SearchAnime"}

    async def client_ready(self, client, db):
        self.client = client

    async def findacmd(self, message):
        reply = await message.get_reply_message()

        if not reply:
            await message.edit("<b>Реплай на медиа</b>")
            return

        try:
            media = reply.media
        except:
            await message.edit("<b>Реплай на медиа</b>")
            return

        await message.edit("<b>Ищу...</b>")
        bot = "@animeu_bot"
        async with message.client.conversation(bot) as conv:
            try:
                response = conv.wait_event(events.MessageEdited(incoming=True, from_users=1644245632))
                await message.client.send_file(bot, media)
                response = await response
            except YouBlockedUserError:
                await message.edit("<b>Разблокируй @Anime_Reverse_Search_Bot</b>")
                return
            try:
                info = response.text.replace("<strong>", "**").replace("</strong>", "**").replace("[", "").replace("]", "")
            except:
                info = response.text.replace("<strong>", "**").replace("</strong>", "**")

            if "Ничего не найдено" in info or "Nothing found" in info:
                await message.edit("<b>Ничего не найдено.</b>")
                await message.client(
                functions.messages.DeleteHistoryRequest(peer='Anime_Reverse_Search_Bot',
                                                        max_id=0,
                                                        just_clear=False,
                                                        revoke=True))
                return

            urls = "\n\n**Ссылки:**\n"
            
            for i in range(str(response.reply_markup).count("buttons")):
                try:
                    urls += '[{}]({})\n'.format(response.reply_markup.rows[i].buttons[0].text, response.reply_markup.rows[i].buttons[0].url)
                    urls += '[{}]({})\n'.format(response.reply_markup.rows[i].buttons[1].text, response.reply_markup.rows[i].buttons[1].url)
                except: pass

            try:
                result = info + urls
            except:
                result = info

            await message.delete()
            await message.client.send_message(message.to_id, result, reply_to=await message.get_reply_message(), link_preview=False, parse_mode="md")
            await message.client(
                functions.messages.DeleteHistoryRequest(peer='Anime_Reverse_Search_Bot',
                                                        max_id=0,
                                                        just_clear=False,
                                                        revoke=True))
