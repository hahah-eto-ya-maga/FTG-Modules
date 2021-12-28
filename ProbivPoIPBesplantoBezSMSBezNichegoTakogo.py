# Coded by Y4sperMaglot
# requires: python-whois

import requests
import json
from whois import whois

from .. import utils, loader

@loader.tds
class ProbivPoIPMod(loader.Module):
	"Jestkii Probiv Po IP"
	strings = {'name': 'ProbivPoIP'}

	async def client_ready(self, client, db):
		self.client = client

	async def ipcmd(self, message):
		""".ip тут ip """
		args = utils.get_args_raw(message)
		if args == '':
			return await message.edit('<b>Чел, ip дай</b>')

		await message.edit('<b>Загрузка...</b>')

		ip = requests.get("http://ip-api.com/json/{}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query".format(args)).text
		lookup = json.loads(ip)

		fixed_lookup = {}
		for key, value in lookup.items():
			special = {'query': 'IP-Адрес', 'continent': 'Континент', 'continentCode': 'Код континента', 'country': 'Страна', 'countryCode': 'Код страны', 'regionName': 'Регион', 'lat': 'Широта', 'lon': 'Долгота', 'timezone': 'Часовой пояс', 'currency': 'Валюта', 'isp': 'Интернет-провайдер', 'org': 'Организация', 'as': 'AS', 'asname': 'ASName', 'mobile': 'Мобильная (сотовая) связь', 'hosting': 'Хостинг', 'proxy': 'Используется прокси (не точное определение)'}
			if key in special:
		            fixed_lookup[special[key]] = str(value)

		text = ""
		for key, value in fixed_lookup.items():
		    text += f"\n<b>{key}:</b> <code>{value}</code>"

		rw = whois(args)
		text += f"\n\n<b>Зарегестрирован:</b> <code>{rw['org']}</code> "
		text += f"(<code>{rw['domain_name']}</code>)"

		text = text.replace('False', 'Нет').replace("True", 'Да')

		await message.delete()
		await message.client.send_message(message.to_id, text, reply_to=await message.get_reply_message(), parse_mode='html')
