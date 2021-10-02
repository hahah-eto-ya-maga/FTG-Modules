# coded by Y4sperMaglot

from io import BytesIO
import speech_recognition as srec
from pydub import AudioSegment as auds

from .. import loader, utils

@loader.tds
class AutoVoiceToTextMod(loader.Module):
    """Автоматическое распознавание текста из отправленного вами ГС"""
    strings = {'name': 'AutoVoiceToText'}

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def attoncmd(self, message):
        """.atton Включить распознавание речи"""
        self.db.set("VoiceToText", "status", True)
        return await message.edit('<b>Автоматическое распознавание включено.</b>')
        
    async def attoffcmd(self, message):
        """.attoff Выключить распознавание речи"""
        self.db.set("VoiceToText", "status", False)
        return await message.edit('<b>Автоматическое распознавание выключено.</b>')


    async def watcher(self, m):
        if self.db.get("VoiceToText", "status", True):
            try:
                if m.file.mime_type.split('/')[0] == 'audio':
                    source = BytesIO(await m.download_media(bytes))
                    source.name = m.file.name
                    out = BytesIO()
                    out.name = 'recog.wav'
                    auds.from_file(source).export(out, 'wav')
                    out.seek(0)
                    recog = srec.Recognizer()
                    sample_audio = srec.AudioFile(out)
                    with sample_audio as audio_file:
                        audio_content = recog.record(audio_file)
                    rec = recog.recognize_google(audio_content, language='ru-RU')
                    await m.edit(rec)
            except: pass