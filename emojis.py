# coded by Y4sperMaglot

import random

from .. import loader, utils


@loader.tds
class EmojiInTextMod(loader.Module):
    """Добавляет смайлы в предложение"""

    strings = {"name": "Emoji"}

    async def emojicmd(self, m):
        emojis = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '☺', '️', '😊', '😇', '🙂', '🙃', '😌', '😍', '🥰', '😘', '😋', '😝', '😛', '😚', '😜', '🤪', '😎', '🤯', '🥵', '😭', '😢', '🥺', '😤', '🤗', '😨', '😱', '😰', '😈', '🤠', '🤑', '😻']

        args = utils.get_args_raw(m)
        reply = await m.get_reply_message()

        def aye(line):
            while " " in line:
                line = line.replace(" ", random.choice(emojis), 1)
            return line

        if not args and not reply:
            await m.edit("<b>Реплай на сообщение</b>")
            return

        elif args and reply:
            await m.edit("<b>Реплай или текст</b>")
            return

        elif args:
            args = aye(args)
            await m.edit(args)

        try:
            reply_text = reply.text
        except: return
        
        else:
            reply_text = aye(reply_text)
            await m.edit(reply_text)