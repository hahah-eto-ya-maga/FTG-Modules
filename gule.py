from .. import loader, utils


@loader.tds
class ThousandMinusSevenMod(loader.Module):
    string = {'name': 'Я гуль...'}
    async def gulecmd(self, message):
        thousand = 1000
        while thousand > 0:
            thousand = thousand - 7
            await message.edit(f'{str(thousand)} - 7')
        await message.edit('<b>Я гуль...</b>')