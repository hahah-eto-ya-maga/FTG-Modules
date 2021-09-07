# coded by @Y4sperMaglot

from telethon import events, functions
from .. import utils, loader
from telethon.errors.rpcerrorlist import YouBlockedUserError

@loader.tds
class PutinMod(loader.Module):
    """Диалог с Владимироум Владимироувичем"""
    strings = {'name': 'Путин'}

    async def client_ready(self, client, db):
        self.client = client

    async def putincmd(self, message):
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not reply and not args:
            await message.edit('<b>Реплай или текст</b>')
            return

        if args or reply:
            try:
                msg = reply.text
            except:
                msg = args

            sentences = msg.split('.')

            final_sentences = []
            for sentence in sentences:
                sentence = sentence.strip()
                if not sentence:
                    continue
                sentence = sentence.capitalize()

                final_sentences.append(sentence)
            final_text = '. '.join(final_sentences)
            msg = final_text + '.'


            bot = '@neural_chat_bot'

            await message.edit('<b>Нологи...</b>')
            async with message.client.conversation(bot) as conv:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=839509606))
                    await message.client.send_message(bot, msg)
                    response = await response
                except YouBlockedUserError:
                    await message.edit('<b>Разблокируй @neural_chat_bot</b>')
                    return

                result = f'<b>Вопрос от юзера:</b>\n {msg}\n<b>Ответ от Путина:</b>\n {response.text}'
                await message.delete()
                await message.client.send_message(message.to_id, result, reply_to=await message.get_reply_message())
    async def resetputcmd(self, message):
        await message.edit('<b>Стираем память Путину...</b>')
        bot = '@neural_chat_bot'
        async with message.client.conversation(bot) as conv:
            try:
                conv.wait_event(events.NewMessage(incoming=True, from_users=839509606))
                await message.client.send_message(bot, '/reset')
            except YouBlockedUserError:
                await message.edit('<b>Разблокируй @neural_chat_bot</b>')
                return
            await message.edit('<b>Путин не выпил таблетки и всё забыл</b>')


