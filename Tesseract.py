# coded by Y4sperMaglot
# requires: pytesseract pillow

from telethon.tl.types import MessageMediaPhoto
from telethon import events
import pytesseract
from PIL import Image
import io

from .. import utils, loader

@loader.tds
class TesseractMod(loader.Module):
    """Распознавание текста с картинки с помощью Tesseract
    Зависимости: Pillow, pytesseract, tesseract"""

    strings = {'name': 'Tesseract'}

    async def client_ready(self, client, db):
        self.client = client

    async def ocrcmd(self, message):
        """.ocr язык"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not reply:
            await message.edit('<b>Реплай на картинку</b>')
            return
        if not args:
            await message.edit('<b>Укажите язык</b>')
            return

        try:
            reply = reply.photo
        except:
            await message.edit('<b>Реплай на картинку</b>')

        if reply and args:
            await message.edit('<b>Распознаю...</b>')
            file = io.BytesIO(await self.client.download_file(reply))
            tes = pytesseract.image_to_string(Image.open(file), lang=args)

            await message.delete()
            await message.client.send_message(message.to_id, f'<b>[OCR]</b>{tes}<b>[OCR]</b>', reply_to=await message.get_reply_message())


