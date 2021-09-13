# coded by Y4sperMaglot
# requires: lyricsgenius

import lyricsgenius
from .. import loader, utils

@loader.tds
class SearchSongMod(loader.Module):
    """Поиск текста песен через Genius"""

    strings = {"name": "Genius"}

    async def geniuscmd(self, message):
        """.genius артист, трек"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not reply and not args:
            await message.edit("<b>Реплай или текст.</b>")
            return
        elif reply and args:
            await message.edit("<b>Только реплай или только текст.</b>")
            return
        try:
            reply = reply.text
        except: pass

        await message.edit("<b>Ищу текст песни как могу...</b>")

        if args:
            genius = lyricsgenius.Genius("GENIUS_API_TOKEN")
            aye = args.split(',')

            try:
                song = genius.search_song(aye[1], aye[0])
                await message.edit((song.lyrics).replace("EmbedShare URLCopyEmbedCopy", ""))
            except:
                await message.edit("<b>Ничего не найдено</b>")

        if reply:
            genius = lyricsgenius.Genius("GENIUS_API_TOKEN")
            aye = reply.split(',')

            try:
                song = genius.search_song(aye[1], aye[0])
                await message.edit((song.lyrics).replace("EmbedShare URLCopyEmbedCopy", ""))
            except:
                await message.edit("<b>Ничего не найдено</b>")
