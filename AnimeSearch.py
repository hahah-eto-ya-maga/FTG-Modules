# coded by Y4sperMaglot

from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageMediaPhoto

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
            await message.edit("<b>Реплай на картинку</b>")
            return

        try:
            gayPic = reply.photo
        except:
            await message.edit("<b>Реплай на картинку</b>")
            return

        await message.edit("<b>Ищу...</b>")
        bot = "@Anime_Reverse_Search_Bot"
        async with message.client.conversation(bot) as conv:
            try:
                response = conv.wait_event(events.MessageEdited(incoming=True, from_users=1644245632))
                await message.client.send_file(bot, gayPic)
                response = await response
            except YouBlockedUserError:
                await message.edit("<b>Разблокируй @Anime_Reverse_Search_Bot</b>")
                return
            
            info = response.text.replace("<strong>", "**").replace("</strong>", "**")

            if "Ничего не найдено" in info or "Nothing found" in info:
                await message.edit("<b>Ничего не найдено.</b>")
                await message.client(
                functions.messages.DeleteHistoryRequest(peer='Anime_Reverse_Search_Bot',
                                                        max_id=0,
                                                        just_clear=False,
                                                        revoke=True))
                return

            try:
                urls = '\n\n**Ссылки:**\n[{}]({})\n'.format(response.reply_markup.rows[0].buttons[0].text, response.reply_markup.rows[0].buttons[0].url)
            except: pass
            try:
                urls += '[{}]({})'.format(response.reply_markup.rows[0].buttons[1].text, response.reply_markup.rows[0].buttons[1].url)
            except: pass
            try:
                urls += '\n[{}]({})'.format(response.reply_markup.rows[1].buttons[0].text, response.reply_markup.rows[1].buttons[0].url)
            except: pass
            try:
                urls += '\n[{}]({})'.format(response.reply_markup.rows[1].buttons[1].text, response.reply_markup.rows[1].buttons[1].url)
            except: pass
            try:
                urls += '\n[{}]({})'.format(response.reply_markup.rows[2].buttons[0].text, response.reply_markup.rows[2].buttons[0].url)
            except: pass
            try:
                urls += '\n[{}]({})'.format(response.reply_markup.rows[2].buttons[1].text, response.reply_markup.rows[2].buttons[1].url)
            except: pass
            try:
                urls += '\n[{}]({})'.format(response.reply_markup.rows[3].buttons[0].text, response.reply_markup.rows[3].buttons[0].url)
            except: pass
            try:
                urls += '\n[{}]({})'.format(response.reply_markup.rows[3].buttons[1].text, response.reply_markup.rows[3].buttons[1].url)
            except: pass
            try:
                urls += '\n[{}]({})'.format(response.reply_markup.rows[4].buttons[0].text, response.reply_markup.rows[4].buttons[0].url)
            except: pass
            try:
                urls += '\n[{}]({})'.format(response.reply_markup.rows[4].buttons[1].text, response.reply_markup.rows[4].buttons[1].url)
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
