# coded by Y4sperMaglot

from asyncio import sleep
from telethon import types

from .. import loader, utils

@loader.tds
class swmuteMod(loader.Module):
	strings={"name": "swmute"}
	
	async def client_ready(self, client, db):
		self.db = db
	
	async def swucmd(self, message):
		""".swu выводит всех юзеров"""
		users = self.db.get("bannedUsers", "users")
		if users is not None:
			id = "Забаненные кенты в этом чате:\n"
			for user in users:
				if user['chat'] == message.chat.id:
					id += f"<a href='tg://user?id={str(user['id'])}'>{str(user['id'])}</a>\n"
			await message.edit(id)
		else:
			return await message.edit("<b>Никого в муте нет.</b>")

	async def swcmd(self, message):
		""".sw on/off"""
		args = utils.get_args_raw(message)
		if "on" in args:
			self.db.set("sw", "status", True)
			return await message.edit("<b>swmute включён.</b>")
		elif "off" in args:
			self.db.set("sw", "status", False)
			return await message.edit("<b>swmute выключен.</b>")
		else: return

	async def swmutecmd(self, message):
		""".swmute reply или id"""
		args = str(utils.get_args_raw(message))
		reply = await message.get_reply_message()
		user = args if reply is None else reply.from_id

		users = self.db.get("bannedUsers", "users")
		if users is not None:
			users.append(dict(id=user, chat=message.chat.id if message.chat else None))
		else:
			users = []
			users.append(dict(id=user, chat=message.chat.id if message.chat else None))
		self.db.set("bannedUsers", "users", users)
		await message.edit(f"Юзер <a href='tg://user?id={user}'>{user}</a> в муте.")

	async def swdelcmd(self, message):
		""".swmute reply или id чтобы больше не удалять сообщения чела"""
		args = str(utils.get_args_raw(message))
		reply = await message.get_reply_message()
		user_id = args if reply is None else reply.from_id

		users = self.db.get("bannedUsers", "users")
		for user in users:
			if user['id'] == user_id and (user['chat'] == message.chat.id or not user['chat']):
				del user['id']
				del user['chat']
		self.db.set("bannedUsers", "users", users)
		await message.edit(f"Юзер <a href='tg://user?id={str(user_id)}'>{str(user_id)}</a> больше не в муте.")

	async def swclscmd(self, message):
		""".swcls размутить всех"""
		self.db.set("bannedUsers", "users", None)
		await message.edit("Никто больше не в муте")

	async def watcher(self, message: types.Message):
		if self.db.get("sw", "status", True):
			try:
				for user in self.db.get("bannedUsers", "users"):
					if not message.chat:
						if user['id'] == message.from_id:
							await message.delete()
					elif user['chat'] == message.chat.id and user['id'] == message.from_id:
						await message.delete()
			except: return
					
