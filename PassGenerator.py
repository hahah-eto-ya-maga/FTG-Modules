
from .. import loader, utils
from random import choice as рандомыч
@loader.tds
class PassGeneratorMod(loader.Module):
    """Генератор паролей"""
    strings = {'name': 'Генератор Паролей'}
    async def passgencmd(self, message):
        """.passgen количество символов"""
        args = utils.get_args_raw(message)
        try:
            simvoli = int(args)
        except:
            await message.edit('<b>Введите число.</b>')
            return

        parol = ''
        for x in range(simvoli):
            parol = parol + рандомыч(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

        await message.edit(parol)
