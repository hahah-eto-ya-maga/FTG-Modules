from .. import loader, utils


def register(cb):
    cb(NowPlayMod())

class NowPlayMod(loader.Module):
    """Что сейчас играет."""
    strings = {'name': 'NowPlay'}

    async def npcmd(self, message):
        """Скидывает то, что сейчас играет."""
        await message.edit('Шо я щас слушаю...')
        np = await message.client.inline_query('nowplaybot', '')
        try:
        	await message.client.send_file(message.to_id, np[0].document)
        except:
        	await message.client.send_file(message.to_id, np[0].result.document)
        await message.delete()
