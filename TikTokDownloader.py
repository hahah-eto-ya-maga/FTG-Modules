from telethon import functions, events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import utils, loader

@loader.tds
class TikTokDownloaderMod(loader.Module):
	"TikTokDownloader without watermark"
	strings = {'name': 'TikTokDownloader'}

	async def client_ready(self, client, db):
		self.client = client

	async def ttcmd(self, message):
		""".tt url"""
		url = utils.get_args_raw(message)
		if 'tiktok.com/' not in url:
			return await message.edit('<b>Give me url.</b>')
		bot = '@TIKTOKDOWNLOADROBOT'

		await message.edit('<b>Downloading...</b>')
		async with message.client.conversation(bot) as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True, from_users=1598492699))
				await message.client.send_message(bot, url)
				response = await response
			except YouBlockedUserError:
				return await message.edit(f'<b>Разблокируй {bot}</b>')

			await message.delete()
			await message.client.send_file(message.to_id, response.media, reply_to=await message.get_reply_message())
			await message.client(
                 functions.messages.DeleteHistoryRequest(peer='TIKTOKDOWNLOADROBOT', max_id=0, just_clear=False, revoke=True))


