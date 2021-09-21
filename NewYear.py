from .. import loader
import datetime
from time import strftime

@loader.tds
class DaysDateMod(loader.Module):
    """Сколько там до нового года"""
    strings = {'name': 'Ждем новый год всем фтг комьюнити'}

    async def nycmd(self, message):
        """.ny"""
        now = datetime.datetime.today()
        NY = datetime.datetime(int(strftime('%Y')) + 1, 1, 1)
        d = NY - now
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        result = '❄ До нового года: {} д. {} час. {} мин. {} сек.'.format(d.days, hh, mm, ss)
        await message.edit(result)
