import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Weather:
	"""
	Класс для работы с API "m3o.com" по поиску информации о погоде в разных регионах.
	"""
	@staticmethod
	def weather_forecast(amount_day: str, city: str) -> str:
		"""
		Статический метод класса,
		по переданным параметрам ищет актуальную информацию по прогнозу погоды.

		:param amount_day: [str] -  количество дней, на которые сделать прогноз, задаётся пользователем.
		:param city: [str] - город, в котором провести поиск, задаётся пользователем.
		:return: [str] - пользователю возвращается найденная информация.
		"""
		url = "https://api.m3o.com/v1/weather/Forecast"
		headers = {
			"Content-Type": "application/json",
			"Authorization": os.getenv('API_TOKEN'),
		}
		data = {
			"days": amount_day,
			"location": city
		}
		my_req = requests.post(url=url, headers=headers, json=data)

		result = list()

		for elem in my_req.json()['forecast']:
			result.append(f'Дата: {elem["date"]}, средняя температура воздуха: {elem["avg_temp_c"]} C')

		response = "\n".join(result)
		return f'Погода в г.{city} на {amount_day} дня:\n' \
			f'{response}'

	@staticmethod
	def weather_now(city: str) -> str:
		"""
		Статический метод класса,
		по переданным параметрам ищет актуальную информацию по актуальной погоде.

		:param city: [str] - город, в котором провести поиск, задаётся пользователем.
		:return: [str] - пользователю возвращается найденная информация.
		"""
		url = "https://api.m3o.com/v1/weather/Now"
		headers = {
			"Content-Type": "application/json",
			"Authorization": os.getenv('API_TOKEN'),
		}
		data = {
			"location": city
		}
		my_req = requests.post(url=url, headers=headers, json=data)
		result = my_req.json()["temp_c"]
		return f'Температура воздуха в г. {city} сейчас: {result} C'
